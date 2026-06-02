<purpose>
Scaling workflow for campaigns that are performing well. Covers budget increases, audience expansion, creative refresh, and budget scheduling — using the scaling playbook framework to avoid disrupting learning phase or tanking performance.
</purpose>

<user-story>
As a performance marketer, I want a structured scaling process that increases spend without killing performance, so that I can grow campaigns profitably from test budgets to significant spend.
</user-story>

<when-to-use>
- Campaign is past learning phase and performing at target CPA/ROAS
- Ready to increase budget beyond current daily spend
- Need to expand to new audiences while maintaining performance
- Entry point routes here via /monster-meta scale
</when-to-use>

<context>
@context/account-config.md
</context>

<references>
@frameworks/advertising/meta/facebook/chunks/17-scaling-playbook.md (primary — scaling methodology)
@frameworks/advertising/meta/facebook/chunks/03-bidding-budget-optimization.md (budget/bid mechanics)
@frameworks/advertising/meta/facebook/chunks/11-ai-first-paradigm.md (Advantage+ scaling)
@frameworks/advertising/meta/facebook/chunks/12-creative-as-targeting-2026.md (creative volume for scale)
</references>

<steps>

<step name="assess_readiness" priority="first">
Determine if the campaign is ready to scale.

1. Ask: "Which campaign do you want to scale? Provide the campaign ID or name."

2. Pull current performance:
   - `get_campaign_details` for campaign settings
   - `get_insights` for last 7 days
   - `get_adsets` to check learning phase status

3. **Scaling readiness check:**
   - [ ] Past learning phase (50+ conversions in 7 days per ad set)
   - [ ] CPA/ROAS at or below target for 3+ consecutive days
   - [ ] Frequency below 3.0
   - [ ] No delivery issues or policy flags
   - [ ] Creative not fatigued (CTR stable or improving)

4. Present readiness assessment.
   - If ready: "Campaign is ready to scale. Current spend: ${X}/day, CPA: ${Y}."
   - If not ready: "Not ready to scale — {specific issues}. Fix these first."

**Wait for confirmation to proceed.**
</step>

<step name="choose_scaling_method">
Select the appropriate scaling approach.

**Present scaling options from Chunk 17:**

| Method | When to Use | Risk Level |
|--------|------------|------------|
| **Vertical — Budget increase** | 20-30% increments every 3-5 days | Low |
| **Horizontal — New ad sets** | Duplicate winning ad set to new audiences | Medium |
| **Creative refresh** | Add new variants to winning structure | Low |
| **CBO migration** | Move from ABO to CBO for Meta optimization | Medium |
| **Advantage+ Shopping/App** | Full automation for e-comm/app campaigns | Variable |
| **Budget scheduling** | Spike budget for known high-demand periods | Low |

Ask: "Which scaling approach? You can combine multiple."

**Wait for selection.**
</step>

<step name="execute_scaling">
Execute the chosen scaling method(s).

<if condition="vertical budget increase">
1. Calculate new budget: current + 20-30% (never more than 50% jump)
2. Show: "Current: ${X}/day → New: ${Y}/day (+{Z}%)"
3. On approval: `update_campaign` or `update_adset` with new daily_budget
4. Schedule next increase: "Check again in 3-5 days. If CPA holds, increase another 20-30%."
</if>

<if condition="horizontal new audiences">
1. Research new audiences via `search_interests`, `search_behaviors`, `get_interest_suggestions`
2. Estimate new audience size via `estimate_audience_size`
3. Create new ad set: `create_adset` with new targeting, same budget as original
4. Copy winning creative to new ad set: `create_ad` with existing creative_id
</if>

<if condition="creative refresh">
1. Review current creatives: `get_ad_creatives` for winning ad
2. Recommend new variants based on Chunk 12 (creative diversity):
   - New hooks (first 3 seconds of video, first line of copy)
   - New visual angles (UGC, testimonial, product demo, lifestyle)
   - New CTAs
3. Create new creatives: `create_ad_creative` + `create_ad`
</if>

<if condition="budget scheduling">
1. Ask: "What dates need higher budget? What multiplier?"
2. Create schedule: `create_budget_schedule` with time_start, time_end, budget_value
</if>

All new entities created in **PAUSED** status. Ask before activating.
</step>

<step name="monitoring_plan">
Set up the post-scaling monitoring plan.

Present monitoring framework:
| Timeframe | Check | Action if CPA rises >20% |
|-----------|-------|--------------------------|
| Day 1-2 | Watch for learning phase reset | Don't panic — allow re-learning |
| Day 3-5 | Compare CPA to pre-scale baseline | If still elevated, reduce budget 10% |
| Day 7 | Full performance review | Run /monster-meta audit |

Report: "Scaling complete. Monitor over the next 7 days. Run `/monster-meta audit` for the performance check."
</step>

</steps>

<output>
Scaling actions executed:
- Changes made (budget updates, new ad sets, new creatives)
- Entity IDs for all new objects
- Monitoring plan with check-in schedule
- Rollback instructions if performance degrades
</output>

<acceptance-criteria>
- [ ] Scaling readiness assessed with data from MCP
- [ ] Scaling method selected based on campaign state
- [ ] Changes executed via MCP tools
- [ ] All new entities created PAUSED (user confirms activation)
- [ ] Monitoring plan provided with specific check-in dates
- [ ] Rollback instructions included
</acceptance-criteria>
