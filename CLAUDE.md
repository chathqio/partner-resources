# Onboarding runbook - read this first

You (Claude) have been handed the **Extendly partner-resources** repo: a Claude Code **plugin
marketplace**. Your job is to get the user set up with the plugins they want, one at a time, and
confirm each works. This file is the **marketplace-level orchestrator**; each plugin carries its own
detailed runbook at `<plugin>/ONBOARDING.md`, which you delegate to.

The user may be brand new to Claude Code. **Operate on their behalf**: run every command you can
yourself, explain what you are doing in plain language, and pause only when a step physically
requires the human (a GitHub login, creating a token, restarting Claude Code).

This runbook is **resumable**. On every session, first detect current state, then continue from the
first unfinished step. Never redo completed work.

---

## Step 0 - Which surface are you on?

Not every plugin here runs everywhere, so establish this **before** promising anything. The
authoritative reference is [`PLATFORMS.md`](./PLATFORMS.md); `VERSIONS.json` carries the same
facts as data, in each plugin's `platforms` array.

| You are on | How you can tell | What to do |
|---|---|---|
| **CLI** - Claude Code on the user's machine | `claude plugin list` works and you can run local commands | Everything below applies. This is the full-capability path |
| **Cloud** - a Claude Code cloud session (`claude.ai/code`, `claude --cloud`, a routine) | You are in a cloned repo but there is no local `~/.claude` state carried over from the user | `fitd-builder` is already installed via this repo's `.claude/settings.json`. Verify with `claude plugin list`, then just use it. Do not attempt monster-meta |
| **claude.ai** - chat or Cowork | You have no shell at all | You cannot install plugins. Point the user at [`claude-ai/README.md`](./claude-ai/README.md) and help them build and upload the fitd-builder bundle |

If the user asks for **monster-meta** on cloud or claude.ai, say plainly that it is CLI only and
why: it needs a local MCP server process and a long-lived Meta token, and there is no safe place
for that token in a cloud environment. Offer the CLI path. Do not attempt a workaround.

---

## On session start: assess, then act

Run this quietly, then act on what you find.

| # | Check | Done when |
|---|---|---|
| 1 | `git --version`, `claude --version` | Prereqs present (need a recent Claude Code that supports plugin `userConfig`, v2.1.x+) |
| 2 | `claude plugin marketplace list` | `extendly-partner-resources` is listed |
| 3 | `claude plugin list` | The plugins the user wants are installed |
| 4 | Per installed plugin: its own `ONBOARDING.md` acceptance check passes | Each chosen plugin is fully set up |

If everything the user wants is installed and set up, tell them what they can do and stop. Otherwise
start at the first unfinished step. If the user handed you the repo to "get going," just proceed; if
they have not asked yet, say what you found and offer to set things up.

---

## Step 1 - Prerequisites (marketplace level)

- Confirm `git --version` and `claude --version`. If Claude Code is too old to support plugin
  `userConfig`, tell the user to update it.
- **Do not** install per-plugin prerequisites here (e.g. `uv` for monster-meta). Those belong to the
  plugin's own onboarding and are only needed if the user installs that plugin.

## Step 2 - GitHub access (for updates)

You install from the **local clone** the user already has, so no GitHub auth is needed to install
now. It **is** needed later for `claude plugin update` to pull new versions from the private repo.
- Check `gh auth status`. If not authenticated, mention it and offer to let them run `gh auth login`
  themselves (suggest `! gh auth login` so it runs in this session). Don't block initial install.

## Step 3 - Add the marketplace

This repo *is* the marketplace.
- Check `claude plugin marketplace list`; if `extendly-partner-resources` is present, skip.
- Otherwise prefer the **GitHub source**, which matches this repo's `.claude/settings.json` and is
  the only source `claude plugin update` can pull new versions from:
  `claude plugin marketplace add chathqio/partner-resources`
- If that fails because the user has not authenticated to GitHub yet, fall back to the **local
  clone** so they are not blocked: `claude plugin marketplace add <absolute path to this repo>`.
  Tell them updates will not work until they run `gh auth login`, and that they can re-point the
  marketplace at GitHub later with `claude plugin marketplace remove extendly-partner-resources`
  followed by the GitHub `add` above.

Either source works with the self-update check below.

## Step 4 - Show available vs installed, then let the user choose

1. **Enumerate available plugins** from `.claude-plugin/marketplace.json` (read the `plugins` array:
   name + description).
2. **Enumerate installed plugins** via `claude plugin list`.
3. **Diff them.** Present a short table: each available plugin, its one-line description, and whether
   it is already installed. For each not-yet-installed plugin, note its setup cost from the table
   below (e.g. "needs a Meta token" vs "install and go").
4. **Ask the user which plugins to install** (they may pick several, or all, or none). Respect their
   choice; do not install plugins they did not ask for.

| Plugin | Runs on | Setup cost |
|---|---|---|
| `fitd-builder` | CLI, cloud, claude.ai | Install and go. No token, no extra prerequisites. |
| `monster-meta` | CLI only | Needs `uv` and a Meta access token; requires one Claude Code restart. |

## Step 5 - Install and onboard each chosen plugin, one at a time

Loop over the user's selected plugins **sequentially**. For each plugin:

1. Read that plugin's `<plugin>/ONBOARDING.md` - it is the authoritative, plugin-specific runbook
   (prerequisites, install command, any token/config, verification, and its own acceptance check).
2. Follow it to completion, pausing for the human only where it says to.
3. Confirm that plugin's acceptance check passes before moving to the next plugin.

Finish one plugin before starting the next so the user is never juggling two setups at once. If a
plugin's onboarding requires a restart (e.g. monster-meta loads an MCP at launch), tell the user;
after the restart this runbook re-runs, re-detects state, and resumes with the next unfinished
plugin.

---

## Skill self-update

Every plugin here checks its own version whenever its skill or one of its commands is invoked, and
updates itself when it is behind. You do not have to remember to do this, but you do have to know
how to respond when it fires.

**How it fires.** Each plugin ships `hooks/hooks.json` wiring `scripts/check-update.sh` to
`PreToolUse(Skill)` and `UserPromptExpansion`. The hook is `asyncRewake`, so it runs in the
background and never delays a skill from loading. It compares the installed
`.claude-plugin/plugin.json` version against `plugins.<name>.version` in `VERSIONS.json` at the
marketplace's `origin/HEAD`. Silence means up to date, or that the check could not run (offline, no
GitHub auth, no marketplace on disk). It is throttled to one real check every 4 hours per plugin.

**What you do when it speaks.** You get a system reminder telling you the plugin is out of date,
with the two commands to run. Run them, then tell the user to `/reload-plugins` (or restart), then
**continue the task they actually asked for**. Do not restart their work from scratch. Two things
to be honest about: the skill already loaded in this session is still the old version, and if the
update fails on GitHub auth the user has to run `gh auth login` themselves.

**Escape hatches**, if a user finds the check intrusive:

| Setting | Effect |
|---|---|
| `EXTENDLY_SKILL_UPDATE_CHECK=off` | No check at all |
| `EXTENDLY_SKILL_UPDATE_CHECK=notify` | Report the update, never install it |
| `EXTENDLY_SKILL_UPDATE_TTL=<seconds>` | Change the 4-hour throttle |

To see the check's reasoning directly, run it by hand:
`./fitd-builder/scripts/check-update.sh "$PWD/fitd-builder" --verbose`

**Where this works.** Local Claude Code and Claude Code cloud sessions both run it: cloud sessions
run hooks from the cloned repo, and a plugin declared in the repo's `.claude/settings.json` is
installed at session start with its hooks intact. A fresh cloud session is already on the current
version, so the check is usually a silent no-op there, but it still catches a resumed session that
has drifted.

The one gap is **claude.ai chat and Cowork**, where a skill is uploaded to the user's account and
there is no hook system at all. Those users update manually; see
[`claude-ai/README.md`](./claude-ai/README.md).

### Maintainer: releasing a new version

A version lives in three places and they must agree, or partners get told to update to a version
that installs as something else. In one commit:

1. `VERSIONS.json` -> `plugins.<name>.version`
2. `<plugin>/.claude-plugin/plugin.json` -> `version`
3. `<plugin>/skills/<name>/SKILL.md` -> `metadata.version`

Then run `./scripts/validate.py`. It checks all three agree, that claude.ai-capable skills still
have spec-compliant frontmatter, and that each plugin's copy of the update script is in sync.

`scripts/check-update.sh` is the canonical script; `<plugin>/scripts/check-update.sh` are
byte-identical copies, because a plugin hook can only reach paths inside its own installed
directory. After editing the canonical one, run `./scripts/sync-plugin-scripts.sh`.

---

## Done

When every chosen plugin passes its acceptance check, tell the user they are set up and show what
each installed plugin can do (pull the command list from each plugin's README). Remind them they can
re-run this any time ("set up the partner tools") to add more plugins later.

## If something breaks

| Symptom | Fix |
|---|---|
| Marketplace not listed after `add` | Re-run `claude plugin marketplace add <repo root>` from the dir containing `.claude-plugin/marketplace.json`. |
| A plugin's commands/tools missing after install | Some plugins need a restart (those with an MCP). Restart Claude Code; this runbook resumes. |
| Plugin not updating | Authenticate to GitHub (`gh auth login`) so `claude plugin update <plugin>` can reach the private repo. |
| `marketplace add` says it already exists with a different source | The user added it from a local path and this repo's `.claude/settings.json` declares the GitHub source. `claude plugin marketplace remove extendly-partner-resources`, then re-add from GitHub. |
| Update check never fires | Confirm `<plugin>/scripts/check-update.sh` is executable (`./scripts/sync-plugin-scripts.sh` sets this) and that `EXTENDLY_SKILL_UPDATE_CHECK` is not `off`. Run it with `--verbose` to see why it is skipping. |
| Update check fires every time | The throttle stamp cannot be written. It goes to `$CLAUDE_PLUGIN_DATA`, falling back to `<plugin>/.cache/`. Check permissions on both. |
| `Unexpected key(s) in SKILL.md frontmatter` on claude.ai | A skill has a non-spec frontmatter field. Run `./scripts/validate.py`, then see [`PLATFORMS.md`](./PLATFORMS.md). |
| User wants monster-meta on claude.ai or in a cloud session | Not possible, and not a bug. Explain why (local MCP server, no secret store) and offer the CLI path. |
| Plugin-specific failure | Open that plugin's `<plugin>/ONBOARDING.md` "if something breaks" section. |
