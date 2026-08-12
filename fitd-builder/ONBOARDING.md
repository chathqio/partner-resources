# fitd-builder - plugin onboarding runbook

This is the **fitd-builder** plugin's own setup runbook. The marketplace orchestrator (the repo root
`CLAUDE.md`) delegates here once the user chooses to install fitd-builder. Setup is trivial: there is
no token, no MCP, and no restart. Install it and it works.

## Step 0 - which surface?

fitd-builder is the one plugin here that runs everywhere, but *how* you install it differs.

- **Claude Code on the user's machine** (terminal, IDE, desktop): follow this file.
- **A Claude Code cloud session on this repo**: already handled. This repo's
  `.claude/settings.json` enables `fitd-builder@extendly-partner-resources`, so the plugin installs
  at session start. Confirm with `claude plugin list`, then jump to **Step 3 - First run**.
- **claude.ai chat or Cowork**: you have no shell and cannot install a plugin. Stop here and work
  through [`../claude-ai/README.md`](../claude-ai/README.md) with the user instead: build the
  bundle with `./scripts/build-skill-bundle.py fitd-builder`, or have them compress
  `fitd-builder/skills/fitd-builder/` by hand, then upload it at claude.ai under
  Settings > Capabilities > Skills.

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

It also keeps itself current. Whenever the skill or one of its commands is invoked, a background
hook compares the installed version against `VERSIONS.json` upstream and updates the plugin when it
is behind, then asks the user to run `/reload-plugins`. Nothing to configure; see
**Skill self-update** in the root [`CLAUDE.md`](../CLAUDE.md) for the escape hatches. To confirm it
works, run:

```bash
./fitd-builder/scripts/check-update.sh "$PWD/fitd-builder" --verbose
```

It should print the installed and upstream versions and say `up to date`. "check skipped" plus a
reason is also a pass on a fresh clone: the marketplace may not be on disk yet, or GitHub auth may
be missing. The check is designed to fail silently rather than ever block a skill from loading.

## Step 2 - (Optional) choose where output is written

All output is markdown, written cwd-relative: `contextualize` -> `./niche-offers/<niche>.md`,
`build` -> `./offer-drafts/<offer-slug>.md`. You don't need to set anything; just run from the folder
where you want the output. The skill confirms the path before writing.

## Step 3 - First run

```
/fitd-builder:contextualize single-location med spas + Speed-to-Lead
```

The skill resolves the offer menu, tightens the niche with you, researches the vertical, and walks
through gated stages (problem, narrative, pillars, assets) before writing the markdown package and
rendering it as a visual, self-contained HTML artifact (a native Artifact, or a `.html` file when
Artifact is unavailable). To create a new offer from scratch instead, run
`/fitd-builder:build <what you deliver + who it's for>`; for just the niche dig,
`/fitd-builder:research <niche + menu offer>`.

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
| Update check never fires | `scripts/check-update.sh` must be executable. Run `./scripts/sync-plugin-scripts.sh` from the repo root, and check `EXTENDLY_SKILL_UPDATE_CHECK` is not `off`. |
| claude.ai upload rejected with `Unexpected key(s) in SKILL.md frontmatter` | The zipped `SKILL.md` has a field claude.ai does not allow. Pull the latest of this repo and rebuild with `./scripts/build-skill-bundle.py fitd-builder`; run `./scripts/validate.py` if you edited the skill yourself. |
| claude.ai upload rejected, or the skill never triggers there | The zip's top level is wrong. It must be one folder with `SKILL.md` directly inside. Compress `fitd-builder/skills/fitd-builder/`, not the plugin folder at the repo root. |
| `/fitd-builder:contextualize` does nothing on claude.ai | Correct, there are no slash commands there. Ask in plain language: "adapt Speed-to-Lead for single-location med spas". |
