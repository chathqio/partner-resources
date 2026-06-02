# Campaign Plan Template

Structured output for `/monster-meta plan`. Save as: `output/ads/{campaign-name}-plan.md`

```template
# Campaign Plan: {campaign_name}

**Created:** {date}
**Status:** Draft — pending build

## Objective
- **Business Goal:** [What outcome this campaign drives]
- **ODAX Objective:** {objective}
- **Funnel Position:** {funnel_stage}
- **Destination URL:** {landing_page_url}
- **Special Ad Categories:** {special_ad_categories}

## Audience
- **Strategy:** {audience_strategy}
- **Age Range:** {age_min} - {age_max}
- **Gender:** {gender}
- **Geography:** {geo_locations}
- **Interests:**
  | Interest | ID | Audience Size |
  |----------|-----|---------------|
  | {interest_name} | {interest_id} | {audience_size} |
- **Behaviors:** {behaviors}
- **Custom Audiences:** {custom_audiences}
- **Estimated Total Audience:** {estimated_audience_size}
- **Advantage+ Audience:** {advantage_audience_enabled}

## Budget & Bidding
- **Budget Type:** {budget_type}
- **Amount:** {budget_amount} ({budget_in_cents} cents)
- **Duration:** {start_date} to {end_date}
- **Bid Strategy:** {bid_strategy}
- **Bid Amount/Cap:** {bid_amount}
- **Optimization Goal:** {optimization_goal}
- **Billing Event:** {billing_event}

## Creative Approach
- **Format:** {ad_format}
- **Variant Count:** {variant_count}
- **Testing Method:** {testing_method}
- **CTA:** {call_to_action_type}
- **Copy Angles:** [Brief description of each copy angle]
- **Visual Direction:** [Brief description of visual approach]

## Naming Convention
- **Campaign:** {campaign_naming}
- **Ad Set:** {adset_naming}
- **Ad:** {ad_naming}

## Build Sequence
1. `create_campaign` — {objective}, {bid_strategy}, {budget}
2. `upload_ad_image` — upload creative assets
3. `create_adset` — targeting, budget, optimization
4. `create_ad_creative` — copy, image, CTA
5. `create_ad` — link creative to ad set
6. Pre-launch checklist
7. Activate on confirmation
```

## Field Documentation

| Field | Type | Description |
|-------|------|-------------|
| {campaign_name} | Variable | Campaign name following naming convention |
| {date} | Variable | Plan creation date (YYYY-MM-DD) |
| {objective} | Variable | ODAX objective (e.g., OUTCOME_LEADS) |
| {funnel_stage} | Variable | TOFU, MOFU, or BOFU |
| {landing_page_url} | Variable | Destination URL for ad clicks |
| {audience_strategy} | Variable | Broad, Defined, or Advantage+ |
| {budget_type} | Variable | Daily or Lifetime |
| {budget_amount} | Variable | Human-readable dollar amount |
| {budget_in_cents} | Variable | Budget in cents for MCP API calls |
| {bid_strategy} | Variable | Meta bid strategy enum value |
| {ad_format} | Variable | Single Image, Video, Carousel, etc. |
| {testing_method} | Variable | 3:2:2, Dynamic Creative, FLEX/DOF, or manual A/B |
| [What outcome...] | Prose | Human-written business goal description |
| [Brief description...] | Prose | Human-written creative direction notes |

## Section Specifications

### Objective
Map the business goal to ODAX. Include funnel position to inform creative and targeting decisions downstream.

### Audience
Include validated interest IDs from MCP research. Note estimated audience size. Recommend Advantage+ for budgets under $100/day or TOFU campaigns.

### Budget & Bidding
Always express budget in both dollars and cents (MCP requires cents). Match bid strategy to objective and risk tolerance.

### Creative Approach
Reference the testing method from framework chunks. Link to creative brief if `/monster-meta creative` was run separately.

### Build Sequence
Pre-populate with the exact MCP tool calls needed. This becomes the execution checklist for `/monster-meta build`.
