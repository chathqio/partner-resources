<purpose>
Pull performance data from existing campaigns and diagnose issues using framework knowledge. Produces a structured performance report with specific recommendations.
</purpose>

<user-story>
As a performance marketer, I want to pull live campaign data and get framework-backed diagnosis of what's working and what's not, so that I can make informed optimization decisions.
</user-story>

<when-to-use>
- Reviewing active campaign performance
- Diagnosing delivery, cost, or conversion issues
- Preparing optimization recommendations
- Entry point routes here via /monster-meta audit
</when-to-use>

<context>
@context/account-config.md
</context>

<references>
@frameworks/advertising/meta/facebook/chunks/05-tracking-attribution-measurement.md (for attribution analysis)
@frameworks/advertising/meta/facebook/chunks/07-account-reporting-policy.md (for reporting structure)
@frameworks/advertising/meta/facebook/chunks/09-depesh-mandalia-bpm-method.md (for BPM performance matrix)
@frameworks/advertising/meta/facebook/chunks/20-account-audit-troubleshooting-operations.md (for diagnostic workflows)
</references>

<steps>

<step name="identify_scope" priority="first">
Determine what to audit.

**Ask:**
1. What do you want to audit? (entire account, specific campaign, ad set, or ad)
2. What time range? (last 7 days, last 30 days, custom range)
3. Any specific concern? (high CPL, low CTR, delivery issues, scaling plateau)

If account ID not in account-config, ask for it.

**Wait for response.**
</step>

<step name="pull_data">
Retrieve performance data via MCP tools.

1. **Account-level overview** (if auditing account):
   - `get_campaigns` with account_id to list all campaigns
   - `get_insights` at account level with requested time_range

2. **Campaign-level detail** (batch in parallel):
   - `get_insights` with campaign_id + breakdowns (age, gender, platform_position, device_platform)
   - `get_adsets` for the campaign
   - `get_ads` for the campaign

3. **Ad-level creative review** (for top and bottom performers):
   - `get_ad_creatives` for each ad
   - `get_ad_image` for visual review (if image ads)

4. Present raw metrics summary:
   | Metric | Value |
   |--------|-------|
   | Spend | |
   | Impressions | |
   | Reach | |
   | CPM | |
   | CTR (link) | |
   | CPC | |
   | Conversions | |
   | CPA / CPL | |
   | ROAS | |
   | Frequency | |
</step>

<step name="diagnose">
Apply framework knowledge to diagnose issues.

**Use the BPM method (Chunk 09) to classify:**
- Is the issue in **Business** (offer/market fit)?
- Is the issue in **Platform** (targeting/delivery/bidding)?
- Is the issue in **Media** (creative/copy/CTA)?

**Common diagnostic patterns:**

| Symptom | Likely Cause | Framework Reference |
|---------|-------------|-------------------|
| High CPM, low delivery | Audience too narrow or creative fatigue | Chunk 02, 12 |
| High CTR, low conversions | Landing page or tracking issue | Chunk 05, 16 |
| Low CTR | Creative not resonating | Chunk 08, 10, 12 |
| High frequency (>3) | Audience saturation | Chunk 16, 17 |
| Learning phase stuck | Too many ad sets or low budget | Chunk 03, 11 |
| iOS attribution gaps | CAPI not configured or delayed reporting | Chunk 05, 13 |

**Analyze breakdowns:**
- Age/gender: Are certain demographics outperforming?
- Platform: Is Instagram outperforming Facebook or vice versa?
- Placement: Are certain placements wasting spend?
- Device: Mobile vs desktop performance gap?
</step>

<step name="recommend">
Generate specific, actionable recommendations.

For each issue found:
1. **What's happening** — data-backed observation
2. **Why** — root cause from framework knowledge
3. **Fix** — specific action with MCP tool to execute it
4. **Priority** — High/Medium/Low based on spend impact

Present as a structured report using @templates/performance-report.md format.

Ask: "Want me to execute any of these recommendations now?"

**Wait for response.**
</step>

</steps>

<output>
Performance report following templates/performance-report.md format, containing:
- Metrics summary table
- BPM diagnosis (Business/Platform/Media)
- Breakdown analysis (age, gender, platform, placement, device)
- Prioritized recommendations with specific actions
- MCP tool calls ready to execute fixes
</output>

<acceptance-criteria>
- [ ] Audit scope confirmed (account/campaign/adset/ad + time range)
- [ ] Performance data pulled via MCP tools
- [ ] Metrics summary presented in table format
- [ ] Issues diagnosed using framework knowledge (BPM or diagnostic patterns)
- [ ] Breakdowns analyzed for targeting insights
- [ ] Recommendations are specific, actionable, and prioritized
- [ ] Report output generated
</acceptance-criteria>
