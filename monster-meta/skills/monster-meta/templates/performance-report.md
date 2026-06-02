# Performance Report Template

Structured output for `/monster-meta audit`. Save as: `output/ads/{campaign-name}-audit-{date}.md`

```template
# Performance Report: {campaign_name}

**Period:** {start_date} to {end_date}
**Generated:** {report_date}
**Account:** {account_id}

## Summary Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Spend | {spend} | | |
| Impressions | {impressions} | | |
| Reach | {reach} | | |
| Frequency | {frequency} | <3.0 | {status} |
| CPM | {cpm} | | |
| CTR (link) | {ctr} | >1.0% | {status} |
| CPC | {cpc} | | |
| Conversions | {conversions} | | |
| CPA / CPL | {cpa} | {target_cpa} | {status} |
| ROAS | {roas} | {target_roas} | {status} |

## BPM Diagnosis

### Business (Offer/Market Fit)
[Assessment of whether the offer resonates with the market. Is CPA high because the offer is weak, or because the platform delivery is off?]

### Platform (Targeting/Delivery/Bidding)
[Assessment of audience targeting, delivery efficiency, bid strategy performance. Learning phase status, audience saturation, placement performance.]

### Media (Creative/Copy/CTA)
[Assessment of creative performance. CTR trends, creative fatigue indicators, copy resonance, CTA effectiveness.]

## Breakdown Analysis

### By Age/Gender
| Segment | Spend | CPA | CTR | ROAS |
|---------|-------|-----|-----|------|
| {segment} | {spend} | {cpa} | {ctr} | {roas} |

### By Platform
| Platform | Spend | CPA | CTR | ROAS |
|----------|-------|-----|-----|------|
| {platform} | {spend} | {cpa} | {ctr} | {roas} |

### By Placement
| Placement | Spend | CPA | CTR | ROAS |
|-----------|-------|-----|-----|------|
| {placement} | {spend} | {cpa} | {ctr} | {roas} |

## Recommendations

| Priority | Issue | Root Cause | Action | MCP Tool |
|----------|-------|-----------|--------|----------|
| {priority} | [What's happening] | [Why — framework reference] | [Specific fix] | {tool_name} |

## Next Steps
1. [Immediate action items]
2. [Scheduled follow-up actions]
3. [Longer-term strategic adjustments]
```

## Field Documentation

| Field | Type | Description |
|-------|------|-------------|
| {campaign_name} | Variable | Campaign being audited |
| {start_date}, {end_date} | Variable | Audit period |
| {spend}, {impressions}, etc. | Variable | Raw metrics from get_insights |
| {status} | Variable | Pass/Warning/Fail against benchmark |
| {target_cpa}, {target_roas} | Variable | User's target KPIs |
| {segment}, {platform}, {placement} | Variable | Breakdown dimension values |
| {priority} | Variable | High, Medium, or Low |
| {tool_name} | Variable | MCP tool to execute the fix |
| [Assessment...] | Prose | Framework-backed analysis |
| [What's happening] | Prose | Data-backed observation |
| [Why — framework reference] | Prose | Root cause citing specific chunk |
| [Specific fix] | Prose | Actionable recommendation |

## Section Specifications

### Summary Metrics
Pull all values from `get_insights`. Status column compares against benchmarks or user targets. Use traffic-light: Pass (at/below target), Warning (within 20%), Fail (above target).

### BPM Diagnosis
Apply Depesh Mandalia's BPM framework (Chunk 09). Separate issues into Business, Platform, and Media categories. This prevents misdiagnosis (e.g., blaming creative when the offer is the problem).

### Breakdown Analysis
Pull from `get_insights` with breakdown parameter. Only include breakdowns relevant to the diagnosis. Highlight segments that are significantly over/under performing.

### Recommendations
Each recommendation must have: a data observation, a root cause from framework knowledge, a specific action, and the MCP tool to execute it. Prioritize by spend impact.
