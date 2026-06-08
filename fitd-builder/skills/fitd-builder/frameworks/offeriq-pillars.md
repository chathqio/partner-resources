# OfferIQ - the 7-pillar FITD offer standard

Self-contained distillation of Extendly's OfferIQ offer standard (faithful to
`partner/offeriq/components/pillars-data.js`). A valid foot-in-the-door offer passes
all seven pillars. This skill hydrates each pillar **for a specific niche**; the
mechanics here are niche-agnostic and non-negotiable.

The master promise is a **72-hour** turnaround (calendar time) across three
standardized calls (tech/intake call, training call, launch call). The offer rides
that machine; it does not rebuild it.

---

## Pillar 1 - One close-to-the-money verifiable problem

**Constraint.** One problem. Singular, specific, not a bundle. It sits close to the
prospect's money (solving it moves revenue, not a soft internal metric), is worth
**$100 to $300/mo recurring** (no less, no more), and is verifiable against the
market, not just asserted.

- **Formula:** `"When [trigger happens], my [type of customer] loses [money outcome]."`
- **Pass:** one sentence, no "and/plus/as well as"; you can name the revenue line it
  moves; $100-300/mo; backed by receipts (prospects asking) OR a competing product/hire
  with a known price.
- **Fail:** names a feeling or internal metric; price has no market anchor; worth >$300
  (that's a flagship) or <$100 (can't carry a plan).

## Pillar 2 - Lead magnet

**Constraint.** A free thing the agency owner puts in front of a prospect that, in
minutes and with **no per-prospect labor**, produces a **real personalized result
about that prospect's own business**. Two jobs: book the prospect on the owner's sales
calendar, and hand the owner a specific **hook** to run that call. The owner closes on
the call; the magnet never closes.

- **Formula:** `"A free, automated [thing] that gives [prospect] a real result about
  their own business in minutes, books a call on the owner's calendar, and hands the
  owner a hook to run it."`
- **Pass:** automated (no per-prospect human labor); personalized to THIS prospect;
  ends with a booked call; leaves the owner something concrete to say.
- **Fail:** tries to auto-close; books a call with nothing to talk about; a generic
  PDF/checklist; needs a human to produce per prospect.
- This pillar's hook is the **call hook**, not the attraction hook (see narrative-engine).

## Pillar 3 - Less than 5 minutes of intake questions

**Constraint.** The intake the offer adds (on top of the standard tech intake) is
completable in **under 5 minutes**. The limit is time and thought per question, not
count. The prospect answers before speaking to a human; anything that makes them stop
and think risks the form.

- **Pass:** added intake under 5 min honestly timed; no single question over ~1 min of
  thought; no duplication of the standard intake; nothing to look up or decide.
- **Fail:** "only six questions" where two need real thought; open essays where a
  pick-list fits; heavy questions parked "for later"; strategic decisions before value.

## Pillar 4 - 15-minute training call SOP

**Constraint.** The offer fits inside the standardized training call (runs ~45 min, 60
budgeted; canonical content is a HighLevel lay of the land - nav, Contacts, Pipelines,
Dashboards, Conversation Manager). The offer gets **one 15-minute custom block** on
top. Name exactly which HighLevel surface that 15 minutes trains, and keep it
trainable in 15.

- **Pass:** names the single HighLevel surface; fits in 15 min on top of canonical;
  doesn't re-teach the lay of the land; preps the customer for the launch call.
- **Fail:** needs >15 min of custom training; re-teaches navigation/Contacts/etc.;
  depends on the customer's live data; no specified focus.

## Pillar 5 - Implementation in under 3 human-hours

**Constraint.** From intake submitted to offer ready for the launch call, total
**human implementation labor is under 3 hours**, inside the ~24h window. The three
standardized calls don't count. This is what keeps the 72-hour promise economically
possible.

- **Should be automated:** customer notifications (workflow triggers), snapshot deploy
  (templated, one-click), customer-specific config from intake, knowledge-base
  population from reused intake answers.
- **Can stay human (with discipline):** a short sanity check of the deployed snapshot;
  one personalized message to the customer.
- **Pass:** every human step listed, totaling <3h; no step needs one specific person
  (written runbook anyone can run); shown end-to-end in a build walkthrough.
- **Fail:** manual steps >3h; you can't state the per-customer labor cost; snapshot
  needs a custom build per customer.

## Pillar 6 - 15-minute test and launch

**Constraint.** The launch call is Extendly-run, ~30 min. **First 15:** show the
implementation working (test data if needed) until the customer says "turn it on now."
**Remaining 15:** make it concretely live (how, where, when). Installing something
isn't the same as the customer trusting it; this call closes that gap.

- **Prove it (<15:00):** show the working *result*, not the configuration; scripted and
  timed; end on the explicit "turn it on."
- **Go live (next 15:00):** the how/where/when it starts running; capture answers as the
  agenda for the two-week CS check-in.
- **Fail:** shows the build instead of the result; needs the customer's real volume;
  ends on "great, it works" with no go-live commitment; runs past time.

## Pillar 7 - Ascension hook

**Constraint.** Delivery exposes a **second problem** the customer didn't know they had
(or now feels sharply). That second problem is what they ascend to solve. The hook is
**not pitched during onboarding**; CS records it as the next opportunity and works it in
upcoming check-in calls.

- **Formula:** `"Once problem #1 is solved, what problem becomes visible or unavoidable
  that they didn't feel before?"`
- **Pass:** the next problem written in one specific sentence; surfaces naturally during
  delivery; recorded for CS; points to a service you or Extendly can deliver.
- **Fail:** pitched during onboarding; nobody records it; takes weeks to materialize;
  leads to a service no one can deliver; generic ("they'll want more automations").

---

## Hydrating pillars for a niche

When the chosen offer comes off the menu, its `pillars` block is the **mechanics seed**
(lead_magnet, intake, training_block, implementation, test_and_launch, ascension_hook),
and `one_problem` seeds pillar 1. Your job is to **retune each to the niche**: the
problem in the niche's words and dollars, the lead-magnet's personalized result for
that vertical, the niche-specific intake fields, the ascension that vertical will feel.
Keep every constraint above intact - narrative makes it attractive, it does not bend the
mechanics.
