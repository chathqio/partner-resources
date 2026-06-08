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

## Step 2 - (Optional) choose where offers are written

By default the skill writes each finished offer package to `./niche-offers/<niche>.md` in your
current folder. You don't need to set anything; just run a build from the folder where you want the
output. If asked, the skill confirms the output path before writing.

## Step 3 - First run

```
/fitd-builder:build single-location med spas + Speed-to-Lead
```

The skill resolves the offer menu, tightens the niche with you, researches the vertical, and walks
through gated stages (problem, narrative, pillars, assets) before writing the package. Or run
`/fitd-builder:research <niche + offer>` to do just the niche research.

## Done

Tell the user fitd-builder is ready and they can:
- `/fitd-builder` - open the skill
- `/fitd-builder:build <niche + offer>` - build a full niche offer package
- `/fitd-builder:research <niche + offer>` - just the niche research

## If something breaks

| Symptom | Fix |
|---|---|
| `/fitd-builder` not found after install | Confirm `claude plugin list` shows it; some setups need a new Claude Code session to pick up freshly installed commands. |
| "couldn't reach the live offer menu" | Expected when offline; the skill falls back to its bundled snapshot and tells you which source it used. |
| Plugin not updating | Authenticate to GitHub (`gh auth login`) so `claude plugin update fitd-builder` can reach the private repo. |
