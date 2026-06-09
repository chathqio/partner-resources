<purpose>
Help an agency partner construct their OWN foot-in-the-door offer from scratch using the
OfferIQ 7-pillar framework, when no menu offer exists yet. The output is a niche-agnostic
offer definition (the offer mechanics, like a new menu entry) as a markdown submission
packet the partner sends to Extendly for review. This task does NOT write narrative or
ad/VSL/landing copy and does NOT touch any YAML; that niche-specific work is
`tasks/contextualize-offer.md`, and adding an approved offer to the menu is Extendly's
manual step.
</purpose>

<user-story>
As an agency partner with a capability or idea but no packaged offer, I want a critical
partner who helps me shape it into a valid OfferIQ foot-in-the-door offer - holding each
pillar to its standard - so that I can submit a real, defensible offer to Extendly.
</user-story>

<when-to-use>
- The user runs /fitd-builder build, or wants to create a new FITD offer from scratch
- There is no existing menu offer that fits what they want to deliver
</when-to-use>

<references>
@context/offer-menu.md (resolve the menu for reference exemplars + the build output path)
@frameworks/offeriq-pillars.md (the 7-pillar standard - the spec every pillar must meet)
@templates/offer-definition.md (the submission-packet output)
@checklists/offer-mechanics.md (gate before delivery)
</references>

<stance>
**You are a critical coach, not a yes-man.** Your job is to help the partner LAND each
pillar, not to rubber-stamp whatever they say. For every pillar:
- Hold the answer to its constraint in `frameworks/offeriq-pillars.md`. If it falls short,
  say so plainly and name exactly why (e.g. "that problem isn't tied to revenue," "that's
  worth more than $300/mo, so it's a flagship not a wedge," "that lead magnet needs
  per-prospect human labor, so it fails Pillar 2," "that intake makes the prospect decide
  something, which risks the form").
- Push back and iterate until the pillar genuinely passes, or the partner consciously
  accepts a flagged gap (which you record, not bury).
- **Do research when you are not confident** instead of accepting a claim. Use WebSearch /
  WebFetch to verify Pillar 1's market anchor (what competing tools or a hire actually
  cost, so the $100-300/mo is real and verifiable), to sanity-check that the problem is
  real and money-adjacent for the stated market, and to pressure-test feasibility.
- Surface uncertainty explicitly. Do not assert confidence you do not have, and do not
  invent proof.
Be direct and useful, not harsh. The goal is a stronger offer, not a graded test.
</stance>

<steps>

<step name="stage_0_exemplars" priority="first">
Resolve the offer menu per `context/offer-menu.md` (live URL → local → bundled snapshot)
and report which source you used. Here the menu is **reference material, not a selection**:
read 1-2 active offers (e.g. Speed-to-Lead, Reputation Management) as worked exemplars of
the 7 pillars done well, and use them to show the partner the bar. Do not make them pick
one.

Confirm the build inputs:
- **What they can deliver** - the capability, automation, tool, or service this offer is
  built on (for Extendly partners this is usually a HighLevel snapshot / workflow they can
  template). Get concrete: what exactly gets set up, and can it be templated/automated?
- **Target market** - who the offer serves (the ICP at the menu level, e.g. "home-services
  agencies on HighLevel"). This is the offer's general market, not a single contextualized
  niche.
- **Output path** - default `./offer-drafts/{offer-slug}.md` (create the folder if missing).

**Wait for confirmation before constructing.**
</step>

<step name="stage_1_pillar_1_problem">
Construct **Pillar 1 - the one close-to-the-money problem** with the partner, in the shape
`"When [trigger], my [type of customer] loses [money outcome]."` Then apply the stance:
- Verify it is ONE problem (no "and"), tied to revenue, and lands in the **$100-300/mo**
  wedge band.
- **Research the market anchor**: search for what competing tools or a hired role cost to
  solve this, so the price band is verifiable rather than asserted. Cite what you find.
- If it fails (feeling/internal metric, >$300 flagship, <$100 too small, no anchor), say
  why and iterate until it passes.

**Gate:** confirm the validated problem before building the rest of the offer on it.
</step>

<step name="stage_2_pillars_2_to_7">
Construct **Pillars 2-7 from scratch** against `frameworks/offeriq-pillars.md`, one at a
time, applying the stance to each. For each pillar, write the partner's answer and a short
**pass/fail with reason**:
2. **Lead magnet (+ call hook)** - free, automated, a real personalized result about the
   prospect's own business; books the call; hands the owner a hook. Push back on anything
   that needs per-prospect labor, auto-closes, or is generic.
3. **<5 min intake** - the added intake is under 5 minutes; nothing to look up or decide.
4. **15-min training block** - name the single HighLevel surface; must fit in 15 min.
5. **<3 human-hours implementation** - list the human steps and total them; pressure-test
   that it really lands under 3 hours and is templated (not a custom build per customer).
6. **15-min test & launch** - prove the working result on test data, get "turn it on," plan
   go-live.
7. **Ascension hook** - the specific second problem delivery surfaces; recorded for CS, not
   pitched at onboarding; points to something deliverable.

Also draft the offer's **summary**, **target market (niche + fits)**, and a **proof**
concept (the lead-magnet / launch demo, title + lines + close) so the packet is complete.

Flag any pillar the partner can't yet satisfy rather than papering over it.
</step>

<step name="assemble_gate_and_write">
1. Assemble everything into `templates/offer-definition.md` (offer name, summary, target
   market, the one problem + why + market anchor, proof, and the 7 pillars each with its
   pass/fail and reason, plus a pass/fail summary and any flagged gaps).
2. Run `checklists/offer-mechanics.md`. Anything failing is fixed or recorded as an open
   gap in the packet (so Extendly sees it honestly).
3. Present the finished offer definition and confirm the output path.
4. On approval, write the markdown file to the resolved path. Remind the partner this is a
   **submission to Extendly**; if approved, Extendly decides whether to add it to the menu.

Ask: "Offer definition written to {path}. Want any pillar revised before you submit?"

**Wait for approval before writing; revise on request.**
</step>

</steps>

<output>
One markdown offer-definition / submission packet at the resolved path (default
`./offer-drafts/{offer-slug}.md`): the niche-agnostic offer mechanics (summary, target
market, the one problem + market anchor, proof, all 7 OfferIQ pillars each with pass/fail
and reasoning, a pass/fail summary, and any flagged gaps). No narrative, no ad/VSL/landing
copy, no YAML.
</output>

<acceptance-criteria>
- [ ] Menu resolved and used as exemplars (source reported); no offer was "selected"
- [ ] Inputs captured: the deliverable/capability and the target market
- [ ] Pillar 1 is one sentence, revenue-tied, $100-300/mo, with a researched/cited market anchor
- [ ] Pillars 2-7 each constructed and marked pass/fail with a reason
- [ ] Weak answers were challenged (not rubber-stamped); uncertainty researched or flagged
- [ ] Packet passes offer-mechanics checklist or records honest open gaps; no em dashes
- [ ] Output is markdown only (no YAML); written to the confirmed path
</acceptance-criteria>
