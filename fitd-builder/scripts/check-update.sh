#!/usr/bin/env bash
#
# Extendly partner-resources - skill self-update check.
#
# WHERE THIS LIVES
#   Canonical copy: scripts/check-update.sh (this file).
#   Byte-identical copies at <plugin>/scripts/check-update.sh, because a plugin hook can
#   only reference paths inside its own ${CLAUDE_PLUGIN_ROOT}: on install the plugin is
#   copied into ~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/, where a
#   ../../scripts/ sibling does not exist. Run scripts/sync-plugin-scripts.sh after editing.
#
# HOW IT RUNS
#   Wired as an async plugin hook (see <plugin>/hooks/hooks.json) on PreToolUse(Skill) and
#   UserPromptExpansion, so it fires when the plugin's skill or one of its commands is
#   invoked. asyncRewake means it runs in the background: loading a skill is never delayed,
#   and the only way this script speaks is by exiting 2, which wakes Claude with the stderr
#   text as a system reminder.
#
#   Runs wherever Claude Code runs, including cloud sessions (claude.ai/code): those run hooks
#   from the cloned repo, and a plugin declared in the repo's .claude/settings.json is installed
#   at session start with its hooks intact. The one surface it cannot reach is claude.ai chat and
#   Cowork, where the skill is uploaded to an account and there is no hook system at all. See
#   claude-ai/README.md for how those users stay current.
#
# CONTRACT
#   exit 0, silent   -> up to date, or the check could not run. Say nothing.
#   exit 2 + stderr  -> out of date. stderr is an instruction for Claude to act on.
#   Any failure (offline, no auth, no marketplace, malformed JSON) exits 0 silently.
#   A version check must never be the reason a skill fails to load.
#
# USAGE
#   check-update.sh <plugin-root>              hook mode (reads hook JSON on stdin)
#   check-update.sh <plugin-root> --verbose     human mode: print status, always exit 0,
#                                               ignore the throttle. Use for acceptance checks.
#
# ENVIRONMENT
#   EXTENDLY_SKILL_UPDATE_CHECK=off      disable the check entirely
#   EXTENDLY_SKILL_UPDATE_CHECK=notify   report the update but tell Claude not to install it
#   EXTENDLY_SKILL_UPDATE_TTL=<seconds>  minimum seconds between checks (default 14400 = 4h)
#
# NOTE ON git fetch
#   To learn the upstream version this runs `git fetch` in the marketplace clone. That only
#   updates remote-tracking refs (refs/remotes/origin/*). It never touches a working tree or
#   a local branch. If the marketplace was added from a local path, the clone it fetches in
#   is the user's own checkout of this repo.

set -uo pipefail

MARKETPLACE_NAME='extendly-partner-resources'
DEFAULT_TTL=14400

plugin_root="${1:-${CLAUDE_PLUGIN_ROOT:-}}"
verbose=0
[ "${2:-}" = '--verbose' ] && verbose=1

say() { [ "$verbose" -eq 1 ] && printf '%s\n' "$*"; return 0; }

# Give up quietly. In verbose mode explain why, so a human can debug it.
bail() { say "check skipped: $*"; exit 0; }

mode="${EXTENDLY_SKILL_UPDATE_CHECK:-update}"
[ "$mode" = 'off' ] && bail 'disabled by EXTENDLY_SKILL_UPDATE_CHECK=off'

[ -n "$plugin_root" ] || bail 'no plugin root given and CLAUDE_PLUGIN_ROOT is unset'
manifest="$plugin_root/.claude-plugin/plugin.json"
[ -f "$manifest" ] || bail "no plugin.json at $manifest"

# --- read our own identity -------------------------------------------------------------
# plugin.json is a flat hand-maintained manifest, so a targeted grep is sufficient and
# keeps this script free of a jq or python dependency.
json_string_field() {  # $1 = file, $2 = key
    sed -n "s/.*\"$2\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p" "$1" | head -n 1
}

plugin_name=$(json_string_field "$manifest" name)
installed_version=$(json_string_field "$manifest" version)
[ -n "$plugin_name" ] || bail 'could not read plugin name from plugin.json'
[ -n "$installed_version" ] || bail 'could not read plugin version from plugin.json'

# --- only act on our own skill --------------------------------------------------------
# PreToolUse(Skill) fires for every skill invocation in the session, including other
# plugins'. Rather than guess at the tool_input key name, look for our plugin name
# anywhere in the hook payload. A false positive costs one throttled no-op.
if [ "$verbose" -eq 0 ]; then
    payload=$(cat 2>/dev/null)
    if [ -n "$payload" ]; then
        case "$payload" in
            *"$plugin_name"*) ;;
            *) exit 0 ;;
        esac
    fi
fi

# --- throttle -------------------------------------------------------------------------
ttl="${EXTENDLY_SKILL_UPDATE_TTL:-$DEFAULT_TTL}"
case "$ttl" in ''|*[!0-9]*) ttl="$DEFAULT_TTL" ;; esac

# CLAUDE_PLUGIN_DATA survives plugin updates; CLAUDE_PLUGIN_ROOT does not.
stamp_dir="${CLAUDE_PLUGIN_DATA:-$plugin_root/.cache}"
stamp="$stamp_dir/update-check.stamp"

file_mtime() { stat -f %m "$1" 2>/dev/null || stat -c %Y "$1" 2>/dev/null; }

now=$(date +%s)
if [ "$verbose" -eq 0 ] && [ -f "$stamp" ]; then
    last=$(file_mtime "$stamp")
    case "$last" in ''|*[!0-9]*) last=0 ;; esac
    if [ "$last" -gt 0 ] && [ $((now - last)) -lt "$ttl" ]; then
        exit 0
    fi
fi
# Stamp before the network work, not after: a hung or failing check must not re-fire on
# every single skill load.
mkdir -p "$stamp_dir" 2>/dev/null && : >"$stamp" 2>/dev/null

# --- locate the marketplace copy ------------------------------------------------------
marketplace_dir=''

# Predictable layout first: <plugins-dir>/marketplaces/<name>. Seed dirs (containers, CI)
# take precedence over the user config dir, matching how Claude Code probes them.
resolve_marketplace_dir() {
    local base candidate
    local -a bases=()
    if [ -n "${CLAUDE_CODE_PLUGIN_SEED_DIR:-}" ]; then
        local -a seeds=()
        IFS=':' read -r -a seeds <<<"$CLAUDE_CODE_PLUGIN_SEED_DIR"
        for base in "${seeds[@]}"; do
            [ -n "$base" ] && bases+=("$base")
        done
    fi
    bases+=("${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins")
    for base in "${bases[@]}"; do
        candidate="$base/marketplaces/$MARKETPLACE_NAME"
        if [ -d "$candidate" ]; then
            printf '%s\n' "$candidate"
            return 0
        fi
    done
    return 1
}

# Fallback: ask the CLI where it put the marketplace. Needs python3 to read the JSON.
resolve_marketplace_dir_via_cli() {
    command -v claude >/dev/null 2>&1 || return 1
    command -v python3 >/dev/null 2>&1 || return 1
    claude plugin marketplace list --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
except Exception:
    sys.exit(1)
for row in rows if isinstance(rows, list) else []:
    if row.get("name") == sys.argv[1] and row.get("installLocation"):
        print(row["installLocation"])
        sys.exit(0)
sys.exit(1)
' "$MARKETPLACE_NAME"
}

marketplace_dir=$(resolve_marketplace_dir) || marketplace_dir=$(resolve_marketplace_dir_via_cli) || marketplace_dir=''
[ -n "$marketplace_dir" ] || bail "marketplace '$MARKETPLACE_NAME' not found on disk"
say "marketplace: $marketplace_dir"

# --- read the upstream VERSIONS.json --------------------------------------------------
read_upstream_versions() {
    local dir="$1" ref
    if [ -d "$dir/.git" ]; then
        GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=true SSH_ASKPASS=true \
        GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=15 \
            git -C "$dir" fetch --quiet --no-tags origin >/dev/null 2>&1
        # If the fetch failed (offline, no GitHub auth) these refs still resolve to the
        # last successful fetch. Stale beats nothing.
        for ref in origin/HEAD origin/master origin/main; do
            if git -C "$dir" cat-file -e "$ref:VERSIONS.json" 2>/dev/null; then
                git -C "$dir" show "$ref:VERSIONS.json" 2>/dev/null && return 0
            fi
        done
    fi
    # Directory-source marketplaces may be a plain copy with no git metadata.
    if [ -f "$dir/VERSIONS.json" ]; then
        cat "$dir/VERSIONS.json"
        return 0
    fi
    return 1
}

versions_json=$(read_upstream_versions "$marketplace_dir") || bail 'could not read upstream VERSIONS.json'
[ -n "$versions_json" ] || bail 'upstream VERSIONS.json was empty'

# Pull plugins.<name>.version. Relies on VERSIONS.json keeping "version" as the first key
# inside each plugin object, which the file documents in its own $comment.
extract_upstream_version() {
    local name="$1" pat
    pat="\"$name\"[[:space:]]*:[[:space:]]*\\{"
    printf '%s\n' "$versions_json" | awk -v pat="$pat" '
        $0 ~ pat { found = 1; next }
        found && /"version"[[:space:]]*:/ {
            line = $0
            sub(/.*"version"[[:space:]]*:[[:space:]]*"/, "", line)
            sub(/".*/, "", line)
            print line
            exit
        }
    '
}

upstream_version=$(extract_upstream_version "$plugin_name")
[ -n "$upstream_version" ] || bail "no version for '$plugin_name' in upstream VERSIONS.json"
say "installed: $installed_version   upstream: $upstream_version"

# --- compare --------------------------------------------------------------------------
version_gt() {  # returns 0 when $1 > $2, comparing up to three numeric components
    local -a a=() b=()
    local i x y
    IFS='.' read -r -a a <<<"${1%%[-+]*}"
    IFS='.' read -r -a b <<<"${2%%[-+]*}"
    for i in 0 1 2; do
        x="${a[i]:-0}"; y="${b[i]:-0}"
        x="${x//[!0-9]/}"; y="${y//[!0-9]/}"
        x="${x:-0}";     y="${y:-0}"
        if [ "$((10#$x))" -gt "$((10#$y))" ]; then return 0; fi
        if [ "$((10#$x))" -lt "$((10#$y))" ]; then return 1; fi
    done
    return 1
}

if ! version_gt "$upstream_version" "$installed_version"; then
    say "up to date ($installed_version)"
    exit 0
fi

# --- out of date ----------------------------------------------------------------------
if [ "$verbose" -eq 1 ]; then
    cat <<EOF
UPDATE AVAILABLE: $plugin_name $installed_version -> $upstream_version
  claude plugin marketplace update $MARKETPLACE_NAME
  claude plugin update $plugin_name
  then /reload-plugins (or restart Claude Code)
EOF
    exit 0
fi

if [ "$mode" = 'notify' ]; then
    cat >&2 <<EOF
Extendly plugin update available: $plugin_name $installed_version -> $upstream_version.

EXTENDLY_SKILL_UPDATE_CHECK is set to 'notify', so do NOT install it yourself. Tell the
user an update is available and give them these commands to run when convenient:

  claude plugin marketplace update $MARKETPLACE_NAME
  claude plugin update $plugin_name
  /reload-plugins

Then carry on with what they asked.
EOF
    exit 2
fi

cat >&2 <<EOF
Extendly plugin update available: $plugin_name $installed_version -> $upstream_version.

Install it now, in this order:

  claude plugin marketplace update $MARKETPLACE_NAME
  claude plugin update $plugin_name

Then tell the user to run /reload-plugins (or restart Claude Code) so $upstream_version
actually loads: an updated plugin keeps using the old directory until it is reloaded.

Two things to be straight with the user about:
  - The skill already loaded in this session is still $installed_version, so anything it
    produces before the reload comes from the older version.
  - If the update command fails on GitHub authentication, they need to run
    'gh auth login' themselves. Say so rather than retrying.

After the update, continue with what the user originally asked for. Do not restart their
task from scratch.
EOF
exit 2
