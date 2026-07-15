<purpose>
Contextualize an **existing Extendly menu offer** to a specific niche: take a chosen
active offer off the menu and run the full pipeline that adapts it into one hydrated,
deployable niche package: research → one specific problem → Expert Secrets narrative →
all 7 OfferIQ pillars retuned for the niche → ad/VSL/landing assets. Gated stage by
stage so the user stays in control and each stage builds on an approved prior stage.
(This is for offers that ALREADY exist on the menu. To construct a brand-new offer from
scratch, use `tasks/build-offer.md` instead.)
</purpose>

<user-story>
As an agency partner, I want to hand the skill a niche and an existing menu offer and
get back a complete, niche-specific foot-in-the-door package - hook, story, mechanics,
and ready copy - so that I can attract a specific person with a specific problem and
close them.
</user-story>

<when-to-use>
- The user runs /fitd-builder contextualize, or asks to adapt an existing menu offer to
  a niche / produce a full niche package
</when-to-use>

<references>
@context/offer-menu.md (resolve the menu + output path)
@tasks/research-niche.md (stage 1)
@frameworks/narrative-engine.md (stage 3)
@frameworks/offeriq-pillars.md (stage 4)
@frameworks/ai-studio-brief.md (stage 5: the AI Studio landing-page brief, §5d)
@templates/niche-offer-package.md (assembly)
@checklists/offer-quality.md (gate before delivery)
@frameworks/artifact-rendering.md (stage 6: render the visual artifact)
@templates/offer-package-artifact.html (stage 6: the self-contained HTML template)
</references>

<steps>

<step name="stage_0_resolve_menu" priority="first">
Resolve the offer menu per `context/offer-menu.md` (live URL → local → bundled
snapshot) and report which source you used. List the `active` offers. Confirm the two
inputs with the user:
- **Niche** - tighten to a specific vertical + size/revenue band (challenge anything
  too broad).
- **Offer** - must be an active menu offer; load its full record as the seed.

Also confirm the **output path** (default `./niche-offers/{niche-slug}.md`;
Extendly-internal: `partner/offeriq/niche_contex/{niche-slug}.md`).

**Wait for confirmation before proceeding.**
</step>

<step name="stage_1_research">
Run `tasks/research-niche.md` for the confirmed niche + offer. Produce the five-part
brief (pains, vocabulary, current vehicle, dollars at stake, objections sorted
vehicle/internal/external). Present it and **gate**: "Approve this research, or correct
it, before I contextualize the offer."

**Wait for approval.**
</step>

<step name="stage_2_one_problem">
Using the research and the offer's seed `one_problem`, write the ONE close-to-the-money
problem for this niche in the owner's words, in the Pillar 1 shape:
`"When [trigger], my [type of customer] loses [money outcome]."` Add the
close-to-money rationale, the verifiability anchor, and the $100-300/mo justification
(per `frameworks/offeriq-pillars.md` Pillar 1).

**Gate:** confirm the problem statement before building narrative on top of it.
</step>

<step name="stage_3_narrative">
Load `frameworks/narrative-engine.md`. Build, in order, in the niche's vocabulary:
1. **New opportunity** - Who/What + Opportunity Switch Headline (the new vehicle, not
   an improvement).
2. **Big Domino** - the one belief statement for this niche + offer.
3. **Epiphany Bridge story** - the full 8-beat story for a relatable owner in the
   niche (both journeys; feelings staged; third-grade clarity).
4. **3 Secrets** - reframe the research's vehicle/internal/external false beliefs as
   curiosity secrets, each with its shatter.

Keep the **attraction hook** distinct from the offer's **call hook**. No em dashes.

**Gate:** present the narrative; confirm the hook + story land before generating
mechanics and assets.
</step>

<step name="stage_4_hydrate_pillars">
Load `frameworks/offeriq-pillars.md` and the chosen offer's `pillars` seed. Hydrate all
seven pillars for the niche (problem from stage 2; lead magnet + call hook; <5 min
intake fields; 15-min training surface; <3h implementation; 15-min test & launch;
ascension hook). Retune each to the niche without bending any constraint. Mark each
pillar pass/fail; resolve or flag any fail.
</step>

<step name="stage_5_assets">
Compress the narrative into the four deployable assets (consistency with stages 2-4 is
required - they are the same hook + story in deployable form):
1. **Ad hook lines** - 5-10 attraction-hook variants across the 5 curiosity angles.
2. **VSL / story script** - the spoken-form Epiphany Bridge, read-aloud ready, landing
   the Big Domino, knocking down the 3 secrets, transitioning to the offer.
3. **Landing page copy** - headline · subhead · problem/agitate · new opportunity ·
   secrets/proof · offer · CTA.
4. **AI Studio landing-page brief** (§5d) - per `frameworks/ai-studio-brief.md`, a
   paste-ready HighLevel AI Studio Build-mode prompt, plus an Assist-mode field map
   and a pre-generation checklist. Derive each field per that framework's source
   table (audience/pain from §1 + §2, objection from §3d, benefits from the §3
   reframes + offer result-value, proof from §2, offer/price from §4). Match §5c only
   on headline, offer, and CTA (§5c has no benefits list, so do not source them there).
</step>

<step name="assemble_gate_and_write">
1. Assemble everything into `templates/niche-offer-package.md`, filling §0-§5 and the
   build notes (menu source, any TBDs, compliance flags carried from the offer).
2. Run `checklists/offer-quality.md` against the package. Fix anything that fails;
   anything that can't be fixed goes in Build notes.
3. Present the finished package to the user and confirm the output path.
4. On approval, write the file to the resolved path (create the folder if missing).

Ask: "Package written to {path}. Want any section revised before I render the
visual version?"

**Wait for approval before writing; revise on request.** Once the markdown is
approved, proceed to stage 6.
</step>

<step name="stage_6_artifact">
Render the approved package as a **visual, self-contained HTML artifact** per
`frameworks/artifact-rendering.md`, using `templates/offer-package-artifact.html`.

1. Fill the template from the approved package (§0-§5 + build notes), overwriting
   the sample content region by region. Add/remove repeatable units to match the
   real package. Leave the `<style>`, the `<svg><defs>` icon library, and the
   `<script>` untouched. Set the `<title>`, cover tag, rail title, and footer to
   this offer + niche. Render failing pillars with the flag variant. For §5d, put
   the **truncated** Build-mode prompt in the `.br-body` block (the full brief stays
   in the markdown); keep its lines flush-left and use ASCII `->`.
2. **Keep it CSP-clean: no external hosts** (no CDN, webfont, remote image, or
   fetch). Icons come from the inline `<symbol>` set; add a symbol rather than
   linking one. No em dashes; attraction hook distinct from the call hook.
3. Deliver:
   - **If the `Artifact` tool is available** (preferred): publish the filled
     document with `Artifact` (favicon `🎯`, a one-line description naming the
     offer + niche). Give the user the returned URL and note it is private until
     they share it.
   - **If `Artifact` is not available**: wrap the document in the standard shell
     (see the framework) and write it to `{same-folder}/{niche-slug}.html`; tell
     the user the path.

Ask: "Visual package ready at {url or path}. Want any changes?" Revise on request
(edit the same file and republish to the same URL, or rewrite the file).
</step>

</steps>

<output>
Two artifacts of the same package:
1. One hydrated markdown file at the resolved output path (the source of truth):
   snapshot, niche definition, the one specific problem, the full narrative (new
   opportunity · big domino · epiphany bridge · 3 secrets), the 7 hydrated OfferIQ
   pillars with pass/fail, and the four deployable assets (ad hooks, VSL/story
   script, landing copy, and the full AI Studio landing-page brief).
2. A visual, self-contained HTML artifact of that package - published as a native
   Artifact (preferred) or written as a `{niche-slug}.html` file (fallback).
</output>

<acceptance-criteria>
- [ ] Menu resolved (source reported); niche tightened; offer is an active menu offer
- [ ] Each stage gated and approved before the next
- [ ] Pillar 1 problem is one sentence, close-to-money, verifiable, $100-300/mo
- [ ] Narrative built in order, in the niche's vocabulary, attraction-hook ≠ call-hook
- [ ] All 7 pillars hydrated and marked pass/fail (fails resolved or flagged)
- [ ] Four assets produced and consistent with the narrative (ad hooks, VSL, landing copy, AI Studio brief)
- [ ] §5d AI Studio brief is paste-ready and consistent with §5c (headline, offer, CTA); full in the markdown, truncated in the artifact
- [ ] Package passes offer-quality checklist; no em dashes
- [ ] Markdown file written to the confirmed output path
- [ ] Visual artifact rendered from the template, CSP-clean (no external hosts), its
      scorecard matching the real pass/fail; delivered as a native Artifact or `.html`
</acceptance-criteria>
