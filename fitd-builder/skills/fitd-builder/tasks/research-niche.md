<purpose>
Dig the niche so every downstream stage (problem, narrative, pillars, assets) is
grounded in how the niche owner actually thinks, talks, and loses money - not in
generic assumptions. Anchored to a chosen offer so the research stays on-target.
</purpose>

<user-story>
As an agency partner building a FITD offer, I want a fast, evidence-based read on a
niche - its pains, vocabulary, current vehicle, dollars at stake, and objections - so
that the offer I build speaks to a specific person with a specific problem.
</user-story>

<when-to-use>
- The user runs /fitd-builder research, or asks to understand a niche before building
- Stage 1 of /fitd-builder build (the build task calls this first)
</when-to-use>

<references>
@context/offer-menu.md (resolve the chosen offer first)
@frameworks/narrative-engine.md (what the 3-secrets / false-belief research must surface)
</references>

<steps>

<step name="resolve_offer_and_niche" priority="first">
1. Resolve the offer menu per `context/offer-menu.md` (live URL → local → bundled
   snapshot). Tell the user which source you used.
2. Confirm the two inputs:
   - **Niche** - push for specificity (vertical + size/revenue band). If it's broad
     ("med spas"), propose a tighter cut ("single-location med spas at $40-80k/mo") and
     confirm.
   - **Offer** - must be an `active` offer on the menu. If the user didn't name one,
     list the active offers and ask. Load that offer's full record (one_problem,
     target_market, proof, pillars) as the anchor.

**Wait for confirmation of niche + offer before researching.**
</step>

<step name="research_the_niche">
Research the niche against the chosen offer's problem. Use WebSearch / WebFetch for
real signal (industry forums, review sites, association pages, job posts, competitor
copy, Reddit/Facebook groups), and ask the user for any insider knowledge they hold.
Produce findings under these headings:

1. **Pains** - the specific, money-adjacent pains in this niche related to the offer's
   problem. Rank by how close to the money they sit.
2. **Vocabulary** - the exact words and phrases owners use (for the problem, the
   workaround, the desired result). Quote them.
3. **Current vehicle** - how they try to solve it today and why it underdelivers (this
   is the "old vehicle" the new opportunity replaces).
4. **Dollars at stake** - what the problem costs in the niche's own numbers; what they
   already pay to mitigate it (the market anchor for Pillar 1's $100-300/mo).
5. **Objections / false beliefs** - sorted into the 3 buckets the narrative needs:
   - **Vehicle:** "this won't work for {niche} specifically"
   - **Internal:** "I can't pull it off / too busy / not techy"
   - **External:** "no time/money, my customers won't, my market's different"
   Capture each as the niche owner would actually say it, with the root experience if
   you can find it.

Cite sources inline where a claim comes from the web. Flag thin spots rather than
inventing detail.
</step>

<step name="review_and_deliver">
Present the research as a tight brief under the five headings above, plus a one-line
read on whether the chosen offer is a strong fit for this niche (and if not, what
might fit better).

Ask: "Does this match what you know about {niche}? Anything to correct or add?"

**Wait for approval or corrections.** If invoked standalone, stop here. If invoked as
stage 1 of a build, hand the approved brief forward.
</step>

</steps>

<output>
A niche research brief: pains, vocabulary, current vehicle, dollars at stake, and
objections (sorted vehicle/internal/external), anchored to the chosen offer, with
sources cited and gaps flagged.
</output>

<acceptance-criteria>
- [ ] Offer menu resolved and source (live/snapshot) reported
- [ ] Niche tightened to a specific vertical + band; offer is an active menu offer
- [ ] All five research headings filled, in the niche's own vocabulary
- [ ] Objections sorted into vehicle / internal / external
- [ ] Web claims cited; thin spots flagged, not invented
- [ ] User approved the brief
</acceptance-criteria>
