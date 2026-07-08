# FITD Builder

A **foot-in-the-door offer** builder for Claude Code, with two modes:

- **contextualize** - take an existing Extendly menu offer and adapt it to a specific niche: the
  **hook + story** (built on Russell Brunson's Expert Secrets) that makes a specific owner stop, the
  **OfferIQ 7-pillar mechanics** retuned for that niche, and **ready-to-run copy** (ad hooks, a
  VSL/story script, landing-page copy). You get a markdown package **and a visual, self-contained
  HTML artifact** of it (a native Artifact, or a `.html` file when Artifact is unavailable).
- **build** - construct a brand-new offer from scratch against the OfferIQ 7-pillar standard, as a
  markdown submission packet you send to Extendly for review.

The idea: a foot-in-the-door offer only attracts when its hook and story speak to a specific person
with a specific problem. OfferIQ defines the offer mechanics; FITD Builder helps you build new ones
that hold to the standard, and adds the niche narrative that makes them magnetic.

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
- `/fitd-builder:contextualize <niche + menu offer>` - adapt an existing menu offer to a niche: hook + story + 7 hydrated pillars + ad/VSL/landing copy, delivered as a markdown package plus a visual HTML artifact
- `/fitd-builder:build <what you deliver + who it's for>` - construct a new offer from scratch against the OfferIQ 7-pillar standard (a submission packet for Extendly)
- `/fitd-builder:research <niche + menu offer>` - just the niche research (pains, vocabulary, vehicle, dollars, objections)

Example: `/fitd-builder:contextualize single-location med spas + Speed-to-Lead`

## How it works

**contextualize** (adapt an existing offer to a niche):
1. **Resolve the offer menu.** Each run fetches the live menu from
   `partner.extendly.com/offeriq/offer_menu/offers.yaml` (falling back to a bundled snapshot when
   offline), so the available offers are always current without updating the plugin.
2. **Research the niche** for its pains, vocabulary, current vehicle, dollars at stake, and objections.
3. **Build the narrative** (new opportunity, the one belief, the epiphany-bridge story, the 3 secrets).
4. **Hydrate the 7 OfferIQ pillars** for the niche.
5. **Produce the assets** (ad hook lines, VSL/story script, landing copy) and write the package.
6. **Render the visual artifact** - the same package as a self-contained HTML document (navy cover,
   section rail, 7-pillar scorecard, copy-to-clipboard assets), published as a native Artifact or
   saved as a `.html` file. No CDNs or external hosts: everything is inlined so it works offline and
   inside the strict Artifact sandbox.

**build** (create a new offer from scratch): a critical-coach flow that holds every OfferIQ pillar to
its standard, pushes back on weak answers, and researches to verify (especially the Pillar 1 market
anchor), then writes a niche-agnostic offer-definition / submission packet you send to Extendly. If
approved, Extendly adds it to the menu. No narrative, no copy, no YAML.

## Output

`contextualize` writes a niche package to `./niche-offers/<niche>.md` and renders a visual artifact of
it (a native Artifact, or `./niche-offers/<niche>.html` when Artifact is unavailable). `build` writes a
markdown submission packet to `./offer-drafts/<offer-slug>.md`. The skill confirms the path before
writing.
