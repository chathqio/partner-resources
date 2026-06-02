# Onboarding runbook — read this first

You (Claude) have been handed the **Extendly partner-resources** repo. Your job: get the
**monster-meta** skill and its **meta-graph MCP** server fully working for this user, end to end,
then confirm it works. This file is your runbook.

The user may be brand new to Claude Code. **Operate on their behalf**: run every command you can
yourself, explain what you're doing in plain language, and pause only at the three steps you
physically cannot do for them (marked **PAUSE — human** below): a GitHub login, creating their Meta
token, and restarting Claude Code.

This runbook is **resumable**. Installing the MCP requires a restart, after which this file is read
again. So on every session, first detect what's already done and continue from there — never redo a
completed step.

---

## On session start: assess state, then act

Run this quick state check (quietly), then jump to the first unfinished step.

| # | State check | Done when |
|---|---|---|
| 1 | `uv --version` | uv is installed |
| 2 | `claude plugin marketplace list` | `extendly-partner-resources` is listed |
| 3 | `claude plugin list` | `monster-meta` is installed |
| 4 | Is the `mcp__meta-graph__whoami` tool available, and does calling it return a valid token? | MCP is loaded **and** the token works |
| 5 | `monster-meta/skills/monster-meta/context/account-config.md` in the **installed** plugin is filled in (not the "NOT CONFIGURED" stub) | account config written |

- If all five pass → tell the user Monster Meta is ready and show them what they can do (see **Done**). Stop.
- Otherwise → start at the first step that isn't done. If the user hasn't explicitly asked to set up,
  say what you found and offer to run the setup now; if they handed you this repo to get going, just proceed.

Decline to do unrelated work until setup is complete, unless the user asks.

---

## Step 1 — Prerequisites

**uv** runs the MCP server (no manual virtualenv needed).
- Check: `uv --version`.
- If missing, install it yourself:
  - macOS with Homebrew: `brew install uv`
  - macOS/Linux without Homebrew: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows (PowerShell): `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Also confirm `git --version` and `claude --version` (need a recent Claude Code that supports plugin
  `userConfig` — v2.1.x or later). If Claude Code is too old, tell the user to update it.

## Step 2 — GitHub access (only needed for future updates)

You're installing from the **local clone** the user already has, so no GitHub auth is required to
install now. It *is* required later for `claude plugin update` to pull new versions from the private
repo.
- Check: `gh auth status`.
- If not authenticated, mention it and offer: **PAUSE — human** asks them to run `gh auth login`
  themselves (suggest they type `! gh auth login` so it runs in this session). Don't block initial
  install on this.

## Step 3 — Add the marketplace

This repo *is* the marketplace.
- Check: `claude plugin marketplace list` — if `extendly-partner-resources` is present, skip.
- Do: add it from the local repo root (the directory containing `.claude-plugin/marketplace.json`):
  `claude plugin marketplace add <absolute path to this repo>`

## Step 4 — Install the plugin and set the Meta token

The plugin declares a sensitive `userConfig` value, `meta_access_token`, which Claude Code stores in
the OS keychain (never plaintext) and feeds to the MCP server.

First, the token. **PAUSE — human:** the user must create a Meta access token — you cannot do the
browser steps for them. Point them to `monster-meta/docs/meta-token-setup.md` and wait. They need a
long-lived **System User** token with `ads_management` + `business_management`.

Then install + store the token. Offer the user the secure path by default:
- **Secure (recommended):** have them run, in this Claude Code session's UI,
  `/plugin install monster-meta@extendly-partner-resources` and paste the token at the **masked**
  prompt (or, if already installed, `/plugin configure monster-meta`). The token never touches shell
  history.
- **You-driven (if they paste you the token):** run
  `claude plugin install monster-meta@extendly-partner-resources --config meta_access_token=<TOKEN>`
  Warn them this records the token in shell history; prefer the masked path, and suggest they rotate
  the token if they used this route on a shared machine.

If `claude plugin list` already shows `monster-meta` but the token isn't set yet, just set the token
via `/plugin configure monster-meta` (masked) or
`claude plugin install monster-meta@extendly-partner-resources --config meta_access_token=<TOKEN>` to
update it.

## Step 5 — Restart Claude Code

MCP servers load at launch, so the freshly installed `meta-graph` server won't be active until a
restart.
- **PAUSE — human:** ask the user to fully quit Claude Code and relaunch `claude` from this same repo
  directory. Tell them you'll automatically pick up where you left off (this runbook re-runs and
  detects the new state).

## Step 6 — Verify the MCP and the token

After the restart:
- Confirm the `mcp__meta-graph__whoami` tool exists (the MCP loaded). If it doesn't, the server didn't
  start — check that the restart happened, that `uv` is installed, and that the token was saved
  (`/plugin configure monster-meta`).
- Call `mcp__meta-graph__whoami`. A valid identity with `ads_management` + `business_management` scopes
  means the skill and MCP are wired together correctly. If it reports an invalid/expired token or
  missing scopes, send the user back to `monster-meta/docs/meta-token-setup.md` Step 4.

## Step 7 — Run the skill's setup

Run the **monster-meta** skill's setup (the `/monster-meta:setup` command, or invoke the skill's
`tasks/setup.md` workflow directly). It discovers the user's ad accounts, pages, and pixels and writes
their `account-config.md`. Help them pick a default account, UTM preference, and audit-log path.

## Step 8 — Functional check

Confirm the skill can actually drive the MCP end to end:
- Call `mcp__meta-graph__get_ad_accounts` and confirm their account(s) come back.
- Optionally do one read via the skill (e.g. `/monster-meta:audit` on the account at a high level).
If those succeed, setup is complete.

---

## Done

Tell the user Monster Meta is fully set up and they can now:
- `/monster-meta` — open the skill (plan, build, audit, scale, creative)
- `/monster-meta:plan` — design a campaign
- `/monster-meta:build` — deploy it (created PAUSED by default)
- `/monster-meta:audit` — pull performance and diagnose
- `/monster-meta:scale` / `/monster-meta:creative` — scale or build creative
- Re-run `/monster-meta:setup` any time to switch the default account or change preferences

Remind them: campaigns are created **PAUSED** by default and nothing activates without their
confirmation; their token can spend money, so they own all activity on their accounts.

## If something breaks

| Symptom | Fix |
|---|---|
| `mcp__meta-graph__*` tools not present after restart | MCP didn't load: confirm the restart, `uv --version`, and that the token is set (`/plugin configure monster-meta`). |
| `whoami` says token invalid/expired | Re-create a non-expiring System User token (`docs/meta-token-setup.md` Step 4) and update it via `/plugin configure monster-meta`. |
| `get_ad_accounts` returns nothing | The System User has no ad accounts assigned — `docs/meta-token-setup.md` Step 3. |
| Writes fail with a permissions error | Missing `ads_management`, or only View (not Manage) on the ad account. |
| `uv: command not found` | Install uv (Step 1) and restart Claude Code. |
| Plugin not updating | Authenticate to GitHub (`gh auth login`) so `claude plugin update monster-meta` can reach the private repo. |
