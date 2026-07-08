# Niche Offer Package Template

The hydrated output of `/fitd-builder contextualize`. Write one file per niche to the resolved
output path (default `./niche-offers/{niche-slug}.md`; Extendly-internal:
`partner/offeriq/niche_contex/{niche-slug}.md`).

Conventions: `{curly}` = variable to replace; `[square]` = prose to write. Remove all
placeholder brackets in the final file. **No em dashes anywhere.** Keep the
**attraction hook** (ad/headline) distinct from the **call hook** (pillar 2).

---

```template
# FITD Offer - {Niche} × {Offer Name}

> Built {date} · Offer: `{offer-id}` · Menu source: {live | snapshot}

## 0. Snapshot
- **Niche:** [the specific niche, tight: vertical + size/revenue band]
- **Offer (from menu):** {Offer Name} - [one line]
- **The one belief (Big Domino):** [one sentence]
- **Attraction hook (headline):** [the single best opportunity-switch headline]

---

## 1. Niche definition
- **Who exactly:** [vertical + size + revenue band; tighter than "{Niche}"]
- **Where they congregate:** [channels, groups, associations, search terms]
- **Current vehicle:** [how they try to solve this today, and why it underdelivers]
- **Vocabulary:** [the words/phrases the owner actually uses - pulled from research]
- **Dollars at stake:** [what the problem costs them, in their numbers]

## 2. The one specific problem (OfferIQ Pillar 1)
> "When [trigger], my [type of customer] loses [money outcome]." - in the niche's words

- **Why it's close to the money:** [the revenue line it moves]
- **Verifiable:** [receipts: prospects asking, or a competing product/hire + price]
- **$100-300/mo check:** [why it lands in the wedge band for this niche]

## 3. Narrative (the hook + story)

### 3a. New opportunity
- **Who/What:** "I help {niche} [new result/vehicle]."
- **The new vehicle (not improvement):** [the mechanism reframed for the niche]

### 3b. The Big Domino (the one belief)
[If {niche} believes {new opportunity} is the key to {desire} and only attainable
through {offer}, all other objections fall.]

### 3c. The story (Epiphany Bridge)
[The 8-beat story for a relatable owner in {niche}: backstory · desires (external +
internal) · the wall · the epiphany · the plan · the conflict · the achievement · the
transformation. Draft-ready prose, third-grade clarity, feelings staged not summarized.]

### 3d. The 3 Secrets (false beliefs → reframes)
1. **Vehicle -** False belief: [it won't work for {niche}]. Secret: [reframe + proof].
2. **Internal -** False belief: [I can't pull it off]. Secret: [done-for-you reliever].
3. **External -** False belief: [outside force stops me]. Secret: [excuse dissolved].

## 4. The offer - 7 OfferIQ pillars, hydrated for {niche}
| # | Pillar | Hydrated for {niche} | Passes? |
|---|--------|----------------------|---------|
| 1 | One close-to-money problem | [from §2] | [y/n] |
| 2 | Lead magnet (+ call hook) | [the free personalized result for this vertical] | [y/n] |
| 3 | <5 min intake | [the niche-specific fast fields] | [y/n] |
| 4 | 15-min training block | [the HighLevel surface] | [y/n] |
| 5 | <3 human-hours implementation | [the steps + time] | [y/n] |
| 6 | 15-min test & launch | [the proof + go-live for this niche] | [y/n] |
| 7 | Ascension hook | [the next problem this niche will feel] | [y/n] |

## 5. Deployable assets

### 5a. Ad hook lines
[5-10 scroll-stopping attraction-hook variants across the 5 curiosity angles
(curiosity / fear / desire). Each one line, in the niche's voice.]

### 5b. VSL / story script
[The spoken-form Epiphany Bridge from §3c, written to be read aloud: open with a hook,
walk the 8 beats, land the Big Domino, knock down the 3 secrets, transition to the
offer. Keep it tight.]

### 5c. Landing page copy
- **Headline:** [attraction hook]
- **Subhead:** [the promise in the niche's words]
- **Problem / agitate:** [from §2, in their language]
- **The new opportunity:** [from §3a]
- **Proof / secrets:** [the 3 secrets as objection-handling blocks]
- **The offer:** [what they get, framed by result-value]
- **CTA:** [the single next action - book the call]

---

## Build notes
- [Menu source used, research gaps, anything left TBD, compliance flags from the offer]
```

---

## Field documentation

| Field | Source |
|-------|--------|
| `{Offer Name}`, `{offer-id}`, pillar seeds | the resolved offer menu record |
| §1 Niche definition, §2 verifiability, §3d false beliefs | the research stage |
| §3 narrative | `frameworks/narrative-engine.md` applied to the niche |
| §4 pillars | `frameworks/offeriq-pillars.md` + the menu record's `pillars` block |
| `{date}` | stamp at write time |

## Section notes
- This markdown package is the source of truth. After it is approved, stage 6 renders
  the same §0-§5 content as a visual, self-contained HTML artifact via
  `frameworks/artifact-rendering.md` + `templates/offer-package-artifact.html`.
- §0 Snapshot is the at-a-glance summary; fill it last from the finished sections.
- §3 and §5 share content by design: §3 is the strategy, §5 is the deployable form of
  the same hook + story. They must stay consistent.
- The pillar table's "Passes?" column is gated by `checklists/offer-quality.md`. Any
  `n` must be resolved or flagged in Build notes before delivery.
