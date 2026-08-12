#!/usr/bin/env bash
#
# Copy the canonical scripts/check-update.sh into every plugin.
#
# Each plugin needs its own copy because a plugin hook can only reference paths under its
# own ${CLAUDE_PLUGIN_ROOT}. On install the plugin directory is copied into
# ~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/, so a repo-root sibling like
# ../../scripts/check-update.sh is simply not there. The script is plugin-agnostic (it reads
# its identity from the plugin.json next to it), so the copies are byte-identical.
#
#   ./scripts/sync-plugin-scripts.sh           copy into every plugin
#   ./scripts/sync-plugin-scripts.sh --check   verify copies match, exit 1 if not

set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
source_script="$repo_root/scripts/check-update.sh"
plugins=(fitd-builder monster-meta)

check_only=0
[ "${1:-}" = '--check' ] && check_only=1

[ -f "$source_script" ] || { echo "missing $source_script" >&2; exit 1; }

status=0
for plugin in "${plugins[@]}"; do
    target="$repo_root/$plugin/scripts/check-update.sh"
    if [ "$check_only" -eq 1 ]; then
        if [ ! -f "$target" ]; then
            echo "MISSING  $plugin/scripts/check-update.sh"
            status=1
        elif ! cmp -s "$source_script" "$target"; then
            echo "STALE    $plugin/scripts/check-update.sh (run ./scripts/sync-plugin-scripts.sh)"
            status=1
        elif [ ! -x "$target" ]; then
            echo "NOT EXEC $plugin/scripts/check-update.sh (hooks will not fire)"
            status=1
        else
            echo "ok       $plugin/scripts/check-update.sh"
        fi
    else
        mkdir -p "$(dirname "$target")"
        cp "$source_script" "$target"
        chmod +x "$target"
        echo "synced   $plugin/scripts/check-update.sh"
    fi
done

exit "$status"
