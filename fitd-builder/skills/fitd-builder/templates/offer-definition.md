# Offer Definition Template (submission packet)

The output of `/fitd-builder build`. A niche-agnostic FITD offer defined against the
OfferIQ 7-pillar standard, written as markdown an agency submits to Extendly for review.
Write to the resolved output path (default `./offer-drafts/{offer-slug}.md`).

Conventions: `{curly}` = variable to replace; `[square]` = prose to write. Remove all
placeholder brackets in the final file. **No em dashes.** This packet defines the offer
*mechanics* only - no hook/story/ad copy (that is `contextualize`) and no YAML (Extendly
adds approved offers to the menu manually).

---

```template
# Offer Definition - {Offer Name}

> Submitted by {agency / partner} · {date} · for Extendly OfferIQ review
> Proposed id: `{offer-slug}` · Status: proposed

## Summary
[One or two sentences: what this offer is.]

## Target market
- **Niche:** [the vertical / ICP this offer serves at the menu level]
- **Fits:** [who inside that market it is for, and the situation that makes them a buyer]

## Pillar 1 - The one close-to-the-money problem
> "When [trigger], my [type of customer] loses [money outcome]."

- **Why it's close to the money:** [the revenue line it moves]
- **Market anchor (verifiable):** [what competing tools or a hire cost to solve this, with
  a cited source] -> supports the $100-300/mo wedge band
- **Pass/fail:** [pass | fail - reason]

## Proof concept (lead-magnet / launch demo)
- **Title:** [the personalized result the prospect sees]
- **Lines:**
  - [what it shows]
  - [what it shows]
- **Close:** [the moment it earns the "turn it on" / books the call]

## The 7 pillars
| # | Pillar | The offer's answer | Pass/fail + reason |
|---|--------|--------------------|--------------------|
| 1 | One close-to-money problem | [from above] | [pass/fail - reason] |
| 2 | Lead magnet (+ call hook) | [free, automated, personalized result; books call; arms owner] | [pass/fail - reason] |
| 3 | <5 min intake | [the fast added fields] | [pass/fail - reason] |
| 4 | 15-min training block | [the single HighLevel surface] | [pass/fail - reason] |
| 5 | <3 human-hours implementation | [the human steps + total time; templated?] | [pass/fail - reason] |
| 6 | 15-min test & launch | [prove the result + go-live plan] | [pass/fail - reason] |
| 7 | Ascension hook | [the next problem delivery surfaces] | [pass/fail - reason] |

## Verdict
- **Pillars passing:** [n]/7
- **Open gaps / flags:** [anything not yet satisfied, stated honestly - or "none"]
- **Ready to submit:** [yes | not yet - what's left]

## Build notes
- [Menu source used for exemplars, research/citations for the market anchor, feasibility
  pressure-tests, decisions the partner consciously accepted.]
```

---

## Field documentation

| Field | Source |
|-------|--------|
| Summary, target market, proof, pillar answers | the build interview (`tasks/build-offer.md`) |
| Pillar constraints / pass-fail standard | `frameworks/offeriq-pillars.md` |
| Market anchor citation | WebSearch/WebFetch during Pillar 1 |
| `{date}` | stamp at write time |

## Section notes
- This packet defines a **niche-agnostic** offer (the mechanics). Narrative and
  go-to-market copy are produced later by `contextualize` once an offer exists.
- Keep pass/fail honest. A flagged gap recorded in Verdict / Build notes is more useful to
  Extendly than a forced "pass."
- Mirrors the data-only `offers.yaml` field set (summary, one_problem, target_market,
  proof, pillars) so an approved packet maps cleanly when Extendly adds it to the menu.
