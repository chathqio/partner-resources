# Offer Quality Checklist (contextualize)

**Purpose:** Gate a hydrated niche offer package from `/fitd-builder contextualize` before
delivery. (For the from-scratch `/fitd-builder build`, use `offer-mechanics.md` instead.)
Every item is pass/fail. Any fail must be fixed or explicitly flagged in the package's
Build notes.

## Inputs & fit
- [ ] The chosen offer exists on the resolved menu and is `status: active`
- [ ] The menu source used (live / snapshot) is stated in the package
- [ ] The niche is specific (vertical + size/revenue band), not a broad category

## The one problem (Pillar 1)
- [ ] Stated as one sentence, in the niche's own words, no "and/plus/as well as"
- [ ] Close to the money: the revenue line it moves is named
- [ ] Verifiable: receipts (prospects asking) or a competing product/hire with a price
- [ ] Lands in the $100-300/mo wedge band (not a flagship, not too small)

## Narrative (hook + story)
- [ ] New opportunity is a new vehicle, not an improvement of what they already do
- [ ] Big Domino is a single belief that, if held, makes other objections irrelevant
- [ ] Epiphany Bridge story has both journeys (achievement + transformation)
- [ ] Story uses the niche's vocabulary and stages feelings (not summarized emotion)
- [ ] 3 Secrets cover vehicle, internal, and external false beliefs, each with a shatter
- [ ] **Attraction hook** (ad/headline) is distinct from the **call hook** (Pillar 2)

## The 7 pillars
- [ ] All seven pillars hydrated for the niche, each marked pass/fail
- [ ] No pillar constraint was bent to fit the narrative
- [ ] Any failing pillar is resolved, or flagged in Build notes with the reason
- [ ] Compliance flags carried from the offer record are surfaced (not dropped)

## Deployable assets
- [ ] Ad hook lines: 5-10 variants, one line each, in the niche's voice
- [ ] VSL/story script is read-aloud ready and matches the §3 narrative
- [ ] Landing copy has headline, subhead, problem/agitate, new opportunity, secrets,
      offer, and a single CTA
- [ ] AI Studio brief (§5d): paste-ready Build-mode prompt with purpose, audience,
      messaging (reusing §5c copy), structure, style, and CTA; Assist map + checklist
      present; consistent with §5c (same headline, offer, CTA)
- [ ] Assets are consistent with the narrative (same hook + story, deployable form)

## House style
- [ ] No em dashes anywhere in the package
- [ ] Markdown output written to the confirmed path, named `{niche-slug}.md`

## Visual artifact (stage 6)
- [ ] Rendered from `templates/offer-package-artifact.html`; `<style>`, icon `<defs>`, and `<script>` left untouched
- [ ] CSP-clean: no external hosts (no CDN script, webfont, remote image, or fetch)
- [ ] Content matches the approved package (same hook + story), in the niche's vocabulary, no em dashes
- [ ] Scorecard visual matches the real pass/fail (failing pillars use the flag variant)
- [ ] §5d brief in the artifact is the truncated Build-mode prompt (flush-left, ASCII arrows), matching §5c
- [ ] Delivered as a native Artifact, or as the wrapped `{niche-slug}.html` fallback file
