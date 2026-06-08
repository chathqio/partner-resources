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
- Otherwise add it from the repo root (the dir containing `.claude-plugin/marketplace.json`):
  `claude plugin marketplace add <absolute path to this repo>`

## Step 4 - Show available vs installed, then let the user choose

1. **Enumerate available plugins** from `.claude-plugin/marketplace.json` (read the `plugins` array:
   name + description).
2. **Enumerate installed plugins** via `claude plugin list`.
3. **Diff them.** Present a short table: each available plugin, its one-line description, and whether
   it is already installed. For each not-yet-installed plugin, note its setup cost from the table
   below (e.g. "needs a Meta token" vs "install and go").
4. **Ask the user which plugins to install** (they may pick several, or all, or none). Respect their
   choice; do not install plugins they did not ask for.

| Plugin | Setup cost |
|---|---|
| `fitd-builder` | Install and go. No token, no extra prerequisites. |
| `monster-meta` | Needs `uv` and a Meta access token; requires one Claude Code restart. |

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
| Plugin-specific failure | Open that plugin's `<plugin>/ONBOARDING.md` "if something breaks" section. |
