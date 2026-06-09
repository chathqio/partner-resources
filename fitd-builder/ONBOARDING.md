# fitd-builder - plugin onboarding runbook

This is the **fitd-builder** plugin's own setup runbook. The marketplace orchestrator (the repo root
`CLAUDE.md`) delegates here once the user chooses to install fitd-builder. Setup is trivial: there is
no token, no MCP, and no restart. Install it and it works.

## On session start: assess, then act

| # | Check | Done when |
|---|---|---|
| 1 | `claude plugin marketplace list` shows `extendly-partner-resources` | Marketplace added (root runbook handles this) |
| 2 | `claude plugin list` shows `fitd-builder` | Plugin installed |

If both pass, fitd-builder is ready - show the user what they can do (see **Done**) and stop.

## Step 1 - Install

```bash
claude plugin install fitd-builder@extendly-partner-resources
```

No configuration is required. The plugin ships with a bundled snapshot of the offer menu, and on
each run it also tries to fetch the live menu from
`https://partner.extendly.com/offeriq/offer_menu/offers.yaml`, so it always has the latest offers.

## Step 2 - (Optional) choose where output is written

All output is markdown, written cwd-relative: `contextualize` -> `./niche-offers/<niche>.md`,
`build` -> `./offer-drafts/<offer-slug>.md`. You don't need to set anything; just run from the folder
where you want the output. The skill confirms the path before writing.

## Step 3 - First run

```
/fitd-builder:contextualize single-location med spas + Speed-to-Lead
```

The skill resolves the offer menu, tightens the niche with you, researches the vertical, and walks
through gated stages (problem, narrative, pillars, assets) before writing the package. To create a
new offer from scratch instead, run `/fitd-builder:build <what you deliver + who it's for>`; for just
the niche dig, `/fitd-builder:research <niche + menu offer>`.

## Done

Tell the user fitd-builder is ready and they can:
- `/fitd-builder` - open the skill
- `/fitd-builder:contextualize <niche + menu offer>` - adapt a menu offer to a niche (full package)
- `/fitd-builder:build <what you deliver + who it's for>` - construct a new offer (submission packet)
- `/fitd-builder:research <niche + menu offer>` - just the niche research

## If something breaks

| Symptom | Fix |
|---|---|
| `/fitd-builder` not found after install | Confirm `claude plugin list` shows it; some setups need a new Claude Code session to pick up freshly installed commands. |
| "couldn't reach the live offer menu" | Expected when offline; the skill falls back to its bundled snapshot and tells you which source it used. |
| Plugin not updating | Authenticate to GitHub (`gh auth login`) so `claude plugin update fitd-builder` can reach the private repo. |
