# AI Studio Brief - the paste-ready HighLevel landing-page brief

The last deployable asset of a contextualize package (§5d). It turns the niche
package into a **design brief a partner pastes into HighLevel's AI Studio** (the
Funnels & Websites AI builder, Build mode) to generate the niche landing page.
Everything in the brief comes from data already in the package, so nothing is
invented here; the brief just re-projects it into the shape AI Studio rewards.

The guiding principle from the research: **AI Studio rewards detail.** A thin,
one-shot prompt yields generic pages. So the brief front-loads who/what/why, the
actual copy, explicit visual direction, and structure.

## Two forms of the same brief

- **Full (markdown package §5d).** The complete Build-mode prompt + an Assist-mode
  field map + a short pre-generation checklist. This is the source of truth.
- **Truncated (artifact §5d).** A condensed **rewrite** of the same Build-mode prompt
  (about one screen), not a mechanical copy of the full one. To condense: drop the
  Assist map and the checklist; keep about three benefits; fold the objection into the
  AUDIENCE sentence; shorten labels if you like. **Field labels are not
  load-bearing** - AI Studio reads the prose, so "Hero headline" vs "Headline" makes
  no difference; keep the meaning, not the exact wording. Same offer, price, and CTA
  as the full brief and as §5c.

## The Build-mode prompt anatomy

HighLevel's Build mode wants four things - **purpose, audience, messaging, style** -
plus structure and a CTA. Fill this shape:

```
Build a landing page for {business / the agency's client}, a {niche} business.

PURPOSE: get {audience} to {primary action, e.g. book a 15-minute call}.

AUDIENCE: {who, tight}. They struggle with {core pain} and want {desired
outcome}. Main objection: {objection}; address it head-on.

MESSAGING (use as the backbone; improve wording, keep meaning):
  - Hero headline: "{§5c headline}"
  - Subheadline: "{§5c subhead}"
  - Core benefits: {benefit 1}, {benefit 2}, {benefit 3 [, 4, 5 in the full brief]}
  - Offer: {what they get}, {price / guarantee / turnaround}
  - Proof: {proof point / stat / result}
  - Primary CTA: "{§5c CTA button text}"

STRUCTURE (in order): Hero -> Problem -> New opportunity -> Benefits -> Proof ->
Offer -> FAQ -> Final CTA with {calendar booking widget | lead form}.

STYLE: Typography {style}; Layout {direction}; Palette {mood in words}. {reference
URL / brand-asset note}.

Generate SEO meta title, description, and image alt text.
```

## Where each field comes from in the package

| Brief field | Source in the package |
|---|---|
| business / niche | §0 offer + §1 niche definition |
| PURPOSE / primary action | the offer's conversion goal (Pillar 2 lead magnet books a call; §5c CTA) |
| AUDIENCE (who) | §1 "who exactly" |
| core pain / desired outcome | §1 current vehicle + dollars-at-stake, and §2 the one problem |
| objection | §3d the 3 secrets (the vehicle/internal/external false beliefs) |
| headline / subhead / CTA | §5c landing-page copy (headline = the attraction hook) |
| core benefits | outcome-led lines from the §3 secrets' reframes + the offer's result-value |
| offer + price | §4 Pillar 2 + the $100-300/mo band |
| proof | §2 verifiable / research stat |
| STRUCTURE | fixed spine: Hero -> Problem -> New opportunity -> Benefits -> Proof -> Offer -> FAQ -> CTA |
| STYLE | see visual direction below |

## Visual direction (the STYLE line)

AI Studio picks palettes from **swatches, so describe the palette as a mood in
words - no hex codes.** Choose niche-appropriate defaults and tell the partner to
adjust in-app:

- **Typography** - one of: modern, clean, premium, creative, editorial, energetic.
- **Layout** - one of: grid, split, editorial, gallery, section-based.
- **Palette** - a mood phrase fit to the niche (e.g. "trustworthy deep green + warm
  neutral" for lawn/landscape; "clean clinical white + calm teal" for med spas).
- **Reference / assets** - tell the partner to paste a reference URL for structure
  inspiration and upload the client's logo + brand images.

## Assist-mode field map (full brief only)

For partners who use the guided path instead of a free-text prompt:

| Assist field | Value |
|---|---|
| Name of the funnel page | a descriptive internal name |
| Business niche | the niche |
| Goal of the funnel page | the single primary conversion goal |
| Target audience | who + core pain |
| What is being offered | the offer, plainly + price/guarantee |
| Language / Tone / Layout | language / tone words / layout direction |

## Pre-generation checklist (full brief only)

- **Set a Brand Voice profile** before generating so copy sounds like the client.
- **Upload the logo and brand images.** AI-generated images are DALL-E-class, so
  keep any critical text as real page text, not baked into a generated image.
- **Provide a reference URL** for structure/layout/style inspiration (treat any
  "clone this site" behavior as unconfirmed; expect inspiration, not a pixel copy).
- **Form won't connect by name?** Paste its Form ID: "Use this form: {ID}".
- **Refine in Chat one change at a time** rather than re-prompting from scratch, and
  give the auto-generated SEO meta a brand/keyword pass before publishing.

## House style

- No em dashes. Write in the niche's own vocabulary.
- The hero headline is the **attraction hook** (what stops the niche), kept distinct
  from the call hook (Pillar 2's sales-call hook).
- Keep the brief honest to the package: same offer, same price band, same proof.

## Caveat to carry

HighLevel AI Studio is Labs-stage and its surface names, modes (Assist/Build/Chat),
and fields shift. The brief targets **Build mode** because that is where a strong
brief pays off most; the Assist map is the fallback for the guided path.
