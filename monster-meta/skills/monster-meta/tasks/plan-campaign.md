<purpose>
Guided campaign strategy workflow that produces a complete campaign plan — objective, audience spec, budget allocation, creative approach, and naming conventions. Uses MCP targeting research tools to validate audience sizing and interest availability before committing to a plan.
</purpose>

<user-story>
As a performance marketer, I want a structured planning workflow that researches audiences, validates targeting options, and produces a deployable campaign plan, so that I can move to build with confidence.
</user-story>

<when-to-use>
- Starting a new ad campaign from scratch
- Pivoting an existing campaign to a new audience or objective
- Entry point routes here via /monster-meta plan
</when-to-use>

<context>
@context/account-config.md
</context>

<references>
@frameworks/advertising/meta/facebook/chunks/01-campaign-architecture.md (for objective selection)
@frameworks/advertising/meta/facebook/chunks/02-targeting-audiences.md (for audience strategy)
@frameworks/advertising/meta/facebook/chunks/03-bidding-budget-optimization.md (for budget/bid strategy)
@frameworks/advertising/meta/facebook/chunks/11-ai-first-paradigm.md (for 2026 Advantage+ guidance)
@frameworks/advertising/meta/facebook/chunks/19-full-funnel-strategy-copywriting.md (for funnel position)
</references>

<steps>

<step name="define_objective" priority="first">
Establish the campaign goal and funnel position.

**Ask:**
1. What is the business goal? (awareness, traffic, leads, sales)
2. Where does this campaign sit in the funnel? (TOFU/MOFU/BOFU)
3. What is the landing page or destination URL?
4. Any special ad categories? (housing, employment, credit, politics)

**When the user provides the destination URL:** Append the required UTM params per `@context/account-config.md` UTM section. This is required, not optional. The final URL in the plan MUST include `utm_source=facebook&utm_medium=paid&utm_campaign={monDD}_{type}&utm_content=[[ad.name]]`. If the user-supplied URL already has UTMs with different values, pause and confirm before overriding.

**Map business goal to ODAX objective:**
| Business Goal | ODAX Objective | Typical Optimization |
|--------------|----------------|---------------------|
| Awareness | OUTCOME_AWARENESS | REACH or IMPRESSIONS |
| Traffic | OUTCOME_TRAFFIC | LINK_CLICKS or LANDING_PAGE_VIEWS |
| Leads | OUTCOME_LEADS | LEAD_GENERATION or CONVERSIONS |
| Sales | OUTCOME_SALES | CONVERSIONS or VALUE |

**Wait for response before proceeding.**
</step>

<step name="research_audience">
Build the targeting spec using MCP research tools.

1. Ask: "Who is the ideal customer? Describe demographics, interests, behaviors, and geography."

2. **Research with MCP tools (batch in parallel):**
   - `search_interests` — validate interest keywords exist and get IDs
   - `search_behaviors` — find relevant behavioral targeting
   - `search_demographics` — check demographic options
   - `search_geo_locations` — validate geographic targets

3. Present findings in a table:
   | Category | Target | ID | Audience Size |
   |----------|--------|-----|---------------|

4. `estimate_audience_size` — validate combined targeting spec

5. Recommend: broad (Advantage+) vs defined audience based on:
   - Budget level (under $100/day → broad is safer)
   - Funnel position (TOFU → broad, BOFU → defined)
   - 2026 best practice: Andromeda performs better with 10-50+ creative variants and broad targeting

**Wait for approval of audience spec.**
</step>

<step name="set_budget_and_bid">
Define budget allocation and bid strategy.

**Ask:**
1. Daily budget or lifetime budget? How much?
2. Campaign duration (start/end dates, or ongoing)?
3. Any budget constraints or phased ramp-up?

**Recommend bid strategy based on objective:**
| Scenario | Bid Strategy | Notes |
|----------|-------------|-------|
| Starting out, testing | LOWEST_COST_WITHOUT_CAP | Let Meta optimize, no cap |
| Cost control needed | COST_CAP | Set target CPA in cents |
| ROAS target | LOWEST_COST_WITH_MIN_ROAS | Requires VALUE optimization |
| Volume at ceiling | LOWEST_COST_WITH_BID_CAP | Hard bid ceiling |

**Remind:** Budgets go to Meta in **cents** (e.g., $50/day = 5000).

**Wait for budget confirmation.**
</step>

<step name="outline_creative_approach">
Define the creative strategy at a high level.

**Ask:**
1. What creative assets do you have? (images, videos, copy)
2. How many variants do you want to test?
3. What is the primary CTA? (LEARN_MORE, SIGN_UP, SHOP_NOW, etc.)

**Recommend creative structure based on framework:**
- Charley T 3:2:2: 3 images/videos x 2 primary texts x 2 headlines
- For Advantage+/FLEX: Use `optimization_type: DEGREES_OF_FREEDOM` with multiple assets
- For manual A/B: Use `is_dynamic_creative: true` on ad set + dynamic_creative_spec

**Note:** Detailed copy and creative work happens in `/monster-meta creative`. This step captures the strategic direction.

**Wait for creative direction confirmation.**
</step>

<step name="compile_plan">
Assemble the complete campaign plan.

1. Generate the plan using @templates/campaign-plan.md format
2. Include all confirmed decisions: objective, audience, budget, creative approach
3. Include naming convention using account-config defaults
4. Include MCP tool call sequence for the build phase

Present the plan to the user.
Ask: "Campaign plan ready. Any adjustments before we move to build?"

**Wait for approval.**
</step>

</steps>

<output>
Completed campaign plan following templates/campaign-plan.md format, containing:
- Objective and funnel position
- Validated audience spec with interest/behavior IDs
- Budget and bid strategy
- Creative approach and variant count
- Naming conventions
- Ready for `/monster-meta build` to deploy
</output>

<acceptance-criteria>
- [ ] Objective mapped to valid ODAX value
- [ ] Audience researched via MCP tools with validated IDs
- [ ] Audience size estimated and within viable range
- [ ] Budget specified with correct bid strategy
- [ ] Creative approach defined (format, variant count, CTA)
- [ ] Complete plan output generated
- [ ] User approved final plan
</acceptance-criteria>
