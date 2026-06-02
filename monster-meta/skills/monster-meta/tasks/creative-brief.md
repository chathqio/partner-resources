<purpose>
Build ad copy variants, creative direction, and competitive intelligence for Meta ad campaigns. Produces structured creative briefs with multiple headline/text/description variants ready for deployment.
</purpose>

<user-story>
As a performance marketer, I want AI-assisted creative development that follows proven frameworks and competitive research, so that I can produce high-performing ad variants quickly.
</user-story>

<when-to-use>
- Developing ad copy for a new campaign
- Refreshing creative for an existing campaign
- Researching competitor ads for inspiration
- Entry point routes here via /monster-meta creative
</when-to-use>

<context>
@context/account-config.md
</context>

<references>
@frameworks/advertising/meta/facebook/chunks/04-ad-formats-creative-specs.md (format specs and limits)
@frameworks/advertising/meta/facebook/chunks/08-charley-t-322-psm.md (3:2:2 creative testing)
@frameworks/advertising/meta/facebook/chunks/10-dara-denney-performance-creative.md (performance creative principles)
@frameworks/advertising/meta/facebook/chunks/12-creative-as-targeting-2026.md (creative diversity strategy)
@frameworks/advertising/meta/facebook/chunks/19-full-funnel-strategy-copywriting.md (copy frameworks by funnel stage)
</references>

<steps>

<step name="gather_creative_brief" priority="first">
Capture the creative context.

**Ask:**
1. What product/offer are you advertising? (1-2 sentence description)
2. Who is the target audience? (pain points, desires, language they use)
3. What funnel stage? (TOFU awareness, MOFU consideration, BOFU conversion)
4. What ad format? (single image, video, carousel, collection)
5. Any existing creative or brand guidelines to follow?
6. Want competitive research first? (I'll search the Ads Library)

**Wait for response.**
</step>

<step name="competitive_research">
Research competitor and industry ads if requested.

<if condition="user wants competitive research">
1. `search_ads_archive` with relevant search terms and country codes
2. Analyze top results for:
   - Hook patterns (what stops the scroll)
   - Copy structure (short vs long, story vs direct)
   - CTA patterns
   - Visual style (UGC, lifestyle, product, graphic)
3. Present findings:
   | Competitor | Hook | Copy Angle | CTA | Visual Style |
   |-----------|------|-----------|-----|-------------|
4. Note: "These are patterns to learn from, not copy. Our creative should be distinctly positioned."
</if>

<if condition="user skips research">
Continue to copy development.
</if>
</step>

<step name="develop_copy">
Write ad copy variants using framework principles.

**Apply the 3:2:2 method (Chunk 08):**
- 3 visual variants (different images/video hooks)
- 2 primary text variants (different copy angles)
- 2 headline variants (different value props)

**Copy structure by funnel stage (Chunk 19):**

| Stage | Primary Text Approach | Headline Approach |
|-------|---------------------|------------------|
| TOFU | Problem-aware hook → curiosity → CTA | Broad benefit statement |
| MOFU | Solution-aware → social proof → CTA | Specific value prop |
| BOFU | Offer-specific → urgency → CTA | Direct offer + scarcity |

**For each variant, produce:**
- **Primary Text** (message field) — up to 125 chars visible, 2200 max
- **Headline** — up to 40 chars (truncates on mobile)
- **Description** — up to 30 chars (shown in some placements)
- **CTA Button** — from Meta's approved list

Present all variants in a comparison table:

| Variant | Primary Text | Headline | Description | CTA |
|---------|-------------|----------|-------------|-----|
| A1 | | | | |
| A2 | | | | |
| B1 | | | | |
| B2 | | | | |

**Character count warnings if any field exceeds recommended limits.**

Ask: "Which variants do you want to use? Or want me to adjust any?"

**Wait for approval.**
</step>

<step name="spec_visual_direction">
Define visual direction for each variant.

For each approved copy variant, specify:
- **Format:** Single image / video / carousel
- **Visual concept:** What the image/video should show
- **Image specs:** Recommended 1080x1080 (1:1) for feed, 1080x1920 (9:16) for Stories/Reels
- **Video specs:** 15s recommended, hook in first 3s, captions required
- **Text overlay guidance:** Minimal (Meta penalizes >20% text on images)

Present as a creative brief table.
</step>

<step name="output_brief">
Compile the final creative brief.

1. Combine approved copy variants + visual direction
2. Format as a deployable brief:
   - Ready for `/monster-meta build` (copy fields map directly to MCP create_ad_creative params)
   - Ready for design team (visual specs included)
3. Note which variants are paired (e.g., "Variant A1 = Image 1 + Primary Text A + Headline 1")
4. **Every destination URL in the brief MUST follow the UTM schema in `@context/account-config.md`** — all four UTM params present, `utm_content=[[ad.name]]` as a literal string. One URL covers all ads in the set.

Ask: "Creative brief complete. Want to deploy these directly with `/monster-meta build`?"
</step>

</steps>

<output>
Creative brief containing:
- Copy variants (primary text, headlines, descriptions, CTAs)
- Visual direction for each variant
- Format specs and character counts
- Competitive research findings (if requested)
- Ready for deployment via /monster-meta build
</output>

<acceptance-criteria>
- [ ] Product/offer and audience context captured
- [ ] Funnel stage identified and copy approach matched
- [ ] At minimum 2 primary text + 2 headline variants produced
- [ ] Character counts within Meta's recommended limits
- [ ] Visual direction specified with correct format specs
- [ ] Competitive research included (if requested)
- [ ] Variants formatted ready for MCP create_ad_creative params
- [ ] User approved final creative brief
</acceptance-criteria>
