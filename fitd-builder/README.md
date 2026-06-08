# FITD Builder

A niche-specific **foot-in-the-door offer** builder for Claude Code. It turns a niche plus a chosen
offer into one complete, deployable package: the **hook + story** (built on Russell Brunson's Expert
Secrets) that makes a specific owner stop and pay attention, the **OfferIQ 7-pillar mechanics**
hydrated for that niche, and **ready-to-run copy** (ad hooks, a VSL/story script, and landing-page
copy).

The idea: a foot-in-the-door offer only attracts when its hook and story speak to a specific person
with a specific problem. OfferIQ defines the offer mechanics; FITD Builder adds the niche narrative
that makes those mechanics magnetic.

## Easiest install: let Claude do it

From the root of the `partner-resources` repo, start Claude and say **"Set up the partner tools for
me."** Claude follows the repo's onboarding runbook, shows you what's available, and installs
fitd-builder (no token, no extra prerequisites). See the repo [README](../README.md).

## Manual install

```bash
# from inside your clone of partner-resources
claude plugin marketplace add .
claude plugin install fitd-builder@extendly-partner-resources
```

That's it. No token, no MCP, no restart. Full setup notes: [`ONBOARDING.md`](./ONBOARDING.md).

## Commands

- `/fitd-builder` - open the skill
- `/fitd-builder:build <niche + offer>` - full package: hook + story + 7 hydrated pillars + ad/VSL/landing copy
- `/fitd-builder:research <niche + offer>` - just the niche research (pains, vocabulary, vehicle, dollars, objections)

Example: `/fitd-builder:build single-location med spas + Speed-to-Lead`

## How it works

1. **Resolve the offer menu.** Each run fetches the live offer menu from
   `partner.extendly.com/offeriq/offer_menu/offers.yaml` (falling back to a bundled snapshot when
   offline), so the available offers are always current without updating the plugin.
2. **Research the niche** for its pains, vocabulary, current vehicle, dollars at stake, and objections.
3. **Build the narrative** (new opportunity, the one belief, the epiphany-bridge story, the 3 secrets).
4. **Hydrate the 7 OfferIQ pillars** for the niche.
5. **Produce the assets** (ad hook lines, VSL/story script, landing copy) and write the package to a file.

## Output

Each build writes one markdown file, by default to `./niche-offers/<niche>.md` in your current
folder. The skill confirms the path before writing.
