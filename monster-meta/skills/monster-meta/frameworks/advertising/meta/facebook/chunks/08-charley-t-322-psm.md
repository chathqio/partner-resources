# Chunk 8: The 3:2:2 Method & PSM — Charley Tichenor IV
## Source: Disrupter School, Disrupter Dispatch, Medium (ctthedisrupter), Social Media Examiner, podcast appearances, LinkedIn posts

---

## Core Concept

Charley Tichenor IV (known as "Charley T" or "Professor Charley T") is a Meta Top 100 Advertiser who has personally managed hundreds of millions in ad spend, with clients and brands generating over $1B in revenue. His client roster includes CBS Television, MGM Hotels, and Disney Movie Club. He founded Disrupter School and Disrupter Agency, and created the 3:2:2 Method, PSM (Profitable Scaling Margin), and 4Pi Analysis frameworks that form a complete system for launching, measuring, and scaling Meta ad campaigns.

Charley T's core philosophy is that Meta is a machine learning platform, not a targeting platform. The advertiser's job is to feed the algorithm high-quality creative inputs and get out of its way. Narrow targeting, fragmented campaign structures, and vanity metrics like ROAS actively work against the algorithm's ability to optimize. His system replaces complexity with simplicity: one campaign, broad targeting, dynamic creative testing via the 3:2:2 Method, profitability decisions driven by PSM instead of ROAS, and campaign health diagnostics through 4Pi Analysis. The result is accounts that scale predictably while requiring 30 minutes per week of management instead of 2 hours per day.

---

## Frameworks

### Framework: The 3:2:2 Method (Dynamic Creative Testing)

**When to use:** Every time you launch a new ad, test new creative, or refresh fatigued campaigns. This is the default ad creation protocol.

**What it is:** A Dynamic Creative template using 3 creative assets + 2 primary text variations + 2 headline variations per ad set. Meta's dynamic creative engine combines these into up to 12 unique ad permutations, then uses machine learning to serve the highest-performing combination to each user.

**Why this ratio:** 3 creatives provide enough variation for the algorithm to learn without diluting signal. 2 primary texts and 2 headlines create meaningful contrast without overwhelming the test matrix. Each impression of each element informs how well every other element performs — Meta prioritizes the best combinations automatically. Loading 10 images and 5 headlines (as Meta allows) creates too many permutations for meaningful signal.

**Step-by-step setup:**

| Step | Action | Details |
|------|--------|---------|
| 1 | Create campaign | Select Sales or Leads objective. Enable Campaign Budget Optimization (CBO). Set daily budget. |
| 2 | Create ad set | Turn ON Dynamic Creative toggle. Set targeting to BROAD: age, gender, and location only. No interest targeting, no lookalikes, no custom audiences. |
| 3 | Add 3 creative assets | Ideally 3 videos (preferred) or a mix of video and static images. Each should represent a different angle, hook, or value proposition. |
| 4 | Write 2 primary texts | Two distinct copy approaches — e.g., one story-driven, one benefit-driven. Different lengths are fine (short vs. long). |
| 5 | Write 2 headlines | Two distinct headlines that frame the offer differently. |
| 6 | Set remaining fields | Add CTA button, destination URL, tracking parameters. |
| 7 | Launch and wait | Allow 3-7 days for the algorithm to exit learning phase. Do NOT touch the ad set during this period. |
| 8 | Read results | Use breakdown reports to identify which creative, text, and headline combinations the algorithm favors. |

**Key rules:**
- Videos outperform static images in most cases — lead with video when possible
- Each creative should address a different objection, angle, or emotional trigger
- "Broad" is a noun, not an adjective — it means age + gender + location only, zero behavioral or interest targeting. **Why this matters more than ever (2026):** Meta's June 2025 interest consolidation removed the majority of granular interest categories, making interest stacking non-viable. Even if you wanted to target interests, the remaining categories are too broad to provide meaningful segmentation. The algorithm, powered by Andromeda's creative-first matching, now outperforms any manual targeting approach when given sufficient creative volume and conversion data.
- CBO is mandatory — let Meta allocate budget across ad sets based on performance
- Never duplicate the same creative across multiple ad sets; this creates internal competition

---

### Framework: 1 Campaign Ad Account Structure

**When to use:** When setting up or restructuring a Meta ad account for any business. This is the foundational account architecture that all other Charley T frameworks operate within.

**Why it works:** The more campaigns you run, the more complex and unstable Meta becomes. Performance suffers and you cannot invest meaningfully into the optimization flywheel around your best ads.

**Structure:**

| Component | Purpose | Details |
|-----------|---------|---------|
| 1 Campaign (CBO) | Contains everything | Sales or Leads objective. All budget allocated here. |
| Control Ad Set | Houses proven winners | Contains post IDs of top-performing 20-50+ ads. Broad targeting. This is where the majority of budget flows. Andromeda's retrieval engine efficiently handles 50+ post IDs per ad set — the old 4-6 ad convention is obsolete. Note: Meta's 20% auto-reallocation between ad sets means budget distribution is less predictable than pre-2025; monitor actual spend vs. set budget. |
| Testing Ad Set(s) | Tests new 3:2:2 creative | Each new 3:2:2 batch launches here. Broad targeting. Lower budget allocation via CBO. |

**Workflow:**
1. Launch new creative using 3:2:2 Method in a testing ad set
2. After learning phase, identify winners via 4Pi Analysis and performance metrics
3. Graduate winning ad post IDs into the control ad set
4. Retire underperformers — do not modify, just turn off
5. Repeat: the control ad set accumulates your best-ever ads, compounding performance over time

**Critical principle:** The 1-campaign structure is built on the scientific method. The control ad set is your control group — a consistent, projectable baseline to test against. Every new 3:2:2 batch is a hypothesis being tested against that control.

---

### Framework: PSM (Profitable Scaling Margin)

**When to use:** For all scaling decisions, budget allocation, and profitability analysis. Replaces ROAS and MER as the primary performance metric.

**Why ROAS fails:** ROAS is a vanity metric that ignores COGS, shipping, taxes, overhead, and — most critically — customer lifetime value. Two businesses with identical ROAS can have wildly different profitability. ROAS is a "hunter" metric focused on the immediate kill; PSM is a "farmer" metric focused on compounding value.

**The PSM Formula:**

```
PSM = LTV / (COGS + CPA)
```

Where:
- **LTV** = Customer Lifetime Value (total revenue a customer generates over their entire relationship, not just first purchase)
- **COGS** = Cost of Goods Sold (product cost, shipping, fulfillment, taxes — everything to deliver the product)
- **CPA** = Cost Per Acquisition (what you pay Meta to acquire that customer)

**How to interpret PSM:**

| PSM Value | Meaning | Action |
|-----------|---------|--------|
| PSM > 3.0x | Highly profitable — significant margin headroom | Aggressive scaling. Increase budget. You could spend 3x more before breakeven. |
| PSM 2.0-3.0x | Healthy profit — solid scaling territory | Scale confidently. Increase budget 20% when CPA is at or below target. |
| PSM 1.5-2.0x | Moderate profit — scaling with caution | Maintain current spend. Optimize creative and funnel before scaling further. |
| PSM 1.0-1.5x | Thin margin — barely profitable | Hold or reduce. Focus on improving LTV (upsells, retention) or reducing COGS. |
| PSM < 1.0x | Unprofitable — spending more than you earn | Cut immediately. Pause campaigns. Fix unit economics before resuming ads. |

**Worked example:**
- AOV (first purchase): $40 | LTV: $200 | COGS: $30 | CPA: $35
- **PSM = $200 / ($30 + $35) = 3.08x**
- ROAS view: $40 / $35 = 1.14x — looks terrible, most advertisers would cut
- PSM view: 3.08x — highly profitable, should scale aggressively
- The difference: PSM accounts for $160 in future revenue that ROAS ignores

**PSM improvement levers:**
- Increase LTV: upsells, cross-sells, subscriptions, retention programs, email/SMS sequences
- Decrease COGS: better supplier terms, fulfillment optimization, product bundling
- Decrease CPA: better creative (3:2:2 testing), broader targeting, improved landing pages

---

### Framework: 4Pi Analysis (Campaign Health Diagnostics)

**When to use:** Weekly or when diagnosing performance changes. Provides a snapshot of campaign health using only 4 metrics — everything else is noise.

**The 4 metrics:**

| Metric | What It Measures | What It Tells You |
|--------|------------------|-------------------|
| **Spend** | How much Meta is spending on an ad/ad set | How much the algorithm "wants" to deliver your ad. High spend = algorithm confidence. |
| **CPM** (Cost Per 1,000 Impressions) | Cost efficiency of reaching people | Content quality signal. Low CPM = Meta thinks people want to see your ad. High CPM = your content isn't connecting and will be shown less at higher cost. |
| **Frequency** | How often the same person sees your ad | Ad fatigue indicator. Rising frequency with rising CPM = creative fatigue. |
| **CPA** (Cost Per Acquisition) | Efficiency of converting impressions to customers | Bottom-line performance. The ultimate measure of ad effectiveness. |

**Two-step reading process:**

**Step 1 — CPM & Frequency (Content Health)**
- Low CPM + Low Frequency = Fresh, high-quality content reaching new people. Ideal state.
- Low CPM + High Frequency = Content is good but audience is saturated. Expand targeting or add new creative.
- High CPM + Low Frequency = Content quality issue. The algorithm doesn't want to serve it. Replace creative.
- High CPM + High Frequency = Ad fatigue. Immediate creative refresh needed. Launch new 3:2:2 batch.

**Step 2 — Spend & CPA (Performance Health)**
- High Spend + Low CPA = The algorithm is confidently scaling a winner. Do not touch. Consider increasing budget.
- High Spend + High CPA = Inefficient scale. Check Step 1 — likely a creative or fatigue issue driving up costs.
- Low Spend + Low CPA = Algorithm wants to spend more but is budget-constrained. Increase budget.
- Low Spend + High CPA = Poor performer. The algorithm is throttling delivery. Consider pausing.

**Key insight:** 4Pi identifies operational trends, not point-in-time issues. Always analyze over 7-day windows, never single days. Single-day fluctuations are noise.

---

### Framework: Performance Gate Scaling (Budget Scaling Protocol)

**When to use:** After a campaign has exited learning phase and you want to increase spend on winners.

**Scaling rules:**

| Rule | Condition | Action |
|------|-----------|--------|
| Scale Up | Last 7-day CPA is at or below target CPA | Increase daily budget by 20% at start of day |
| Protect | At 75% of daily budget spent, CPA is 20%+ over target | Pause delivery for the day (automated rule) |
| Cap | Set maximum daily budget incrementally | Increase cap from $120 to $140 to $160 as conversion thresholds are met |
| Pause | CPA has been over target for 7+ consecutive days | Pause the ad set. Launch new 3:2:2 test. |

**Why 20%:** Budget increases over 20% can reset Meta's learning phase, causing performance volatility. The 20% threshold keeps changes within the algorithm's comfort zone. Compounding 20% increases daily (when CPA allows) produces aggressive scaling without destabilization.

**Vertical vs. horizontal scaling in Charley T's system:**
- **Vertical scaling** = increasing budget on proven winners (the 20% rule). Primary scaling mechanism.
- **Horizontal scaling** = launching new 3:2:2 creative batches in testing ad sets, then graduating winners to the control ad set. This is about creative variation, not audience fragmentation — the audience is always broad.

---

## Key Principles

- **Meta is a machine learning platform, not a targeting platform.** Feed it creative inputs and let the algorithm find the right people.
- **Broad targeting outperforms interest and lookalike targeting at scale.** "Broad" means age, gender, and location only — zero behavioral inputs.
- **Creative volume beats audience segmentation.** Test more creative, not more audiences. The 3:2:2 Method is the vehicle.
- **ROAS is for ego; PSM is for scale.** PSM gives you the real picture of how much you can afford to spend to acquire a customer.
- **One campaign, one structure.** Account complexity is the enemy of algorithmic performance.
- **The scientific method applies to advertising.** The control ad set is your control group. Every 3:2:2 batch is a hypothesis.
- **CPM is a content quality score.** Low CPM = people want your content. High CPM = they don't.
- **Never optimize during learning phase.** Allow 3-7 days. Premature changes reset learning and waste budget.
- **Compound winners; don't chase losers.** Graduate winners to control. Turn off losers. Never "fix" underperformers — replace with new 3:2:2.
- **30 minutes per week, not 2 hours per day.** The 1-campaign structure + 3:2:2 + automated scaling rules reduce management time by 85%+.

---

## Decision Tools

### Scale / Maintain / Cut Decision Matrix

Use this matrix weekly to make budget decisions on each ad set:

| PSM | CPA vs. Target | CPM Trend | Frequency | Decision |
|-----|----------------|-----------|-----------|----------|
| > 2.0x | At or below target | Stable or falling | < 2.0 | **SCALE:** Increase budget 20% daily |
| > 2.0x | At or below target | Rising | > 2.5 | **MAINTAIN + REFRESH:** Hold budget, launch new 3:2:2 batch — early fatigue signal |
| > 2.0x | 10-20% over target | Stable | < 2.0 | **MAINTAIN:** Hold budget, monitor for 3 more days |
| 1.5-2.0x | At or below target | Stable | < 2.0 | **MAINTAIN:** Profitable but thin — optimize funnel/LTV before scaling |
| 1.5-2.0x | Over target | Rising | > 2.5 | **CUT SPEND:** Reduce budget 25%, launch new 3:2:2 to replace fatigued creative |
| 1.0-1.5x | Any | Any | Any | **HOLD:** Do not scale. Focus entirely on improving LTV or reducing COGS |
| < 1.0x | Any | Any | Any | **CUT:** Pause campaign. Fix unit economics before running ads |

### Creative Refresh Trigger Checklist

Launch a new 3:2:2 batch when ANY of these are true:

- [ ] Frequency exceeds 2.5 on any ad set over 7-day window
- [ ] CPM has risen 20%+ from baseline over 7-day window
- [ ] CPA has risen 15%+ from target over 7-day window with no funnel changes
- [ ] An ad set has been running 21+ days without new creative
- [ ] CTR (click-through rate) has dropped 20%+ from first-week baseline

### PSM Calculator Template

Use this template to calculate PSM for any product or offer:

```
INPUTS:
  Average Order Value (first purchase):  $________
  Customer Lifetime Value (LTV):         $________
  Total COGS (product + shipping + processing): $________
  Current CPA (from Meta Ads Manager):   $________

CALCULATE PSM:
  PSM = LTV / (Total COGS + CPA)
      = $________ / ($________ + $________) = ________x

CALCULATE MAX CPA (breakeven):
  Max CPA = LTV - Total COGS = $________ - $________ = $________

SCALING HEADROOM:
  Gap = Max CPA - Current CPA = $________
  Headroom = ________% more you could spend before breakeven

INTERPRET: >3.0x = scale aggressively | 2.0-3.0x = scale confidently |
  1.5-2.0x = maintain | 1.0-1.5x = hold | <1.0x = cut
```

### 3:2:2 Launch Checklist

Before launching any new 3:2:2 ad set:

- [ ] Campaign is set to CBO (Campaign Budget Optimization)
- [ ] Ad set targeting is BROAD (age + gender + location only)
- [ ] Dynamic Creative toggle is ON
- [ ] Exactly 3 creative assets loaded (video preferred)
- [ ] Each creative represents a different angle/hook/objection
- [ ] Exactly 2 primary text variations written (distinct approaches, not minor edits)
- [ ] Exactly 2 headline variations written (distinct framings)
- [ ] CTA button selected
- [ ] Pixel/conversion event properly configured
- [ ] UTM parameters added to destination URL
- [ ] No scheduling restrictions set (let the algorithm choose delivery times)
- [ ] Committed to no changes for 3-7 days (learning phase protection)

---

*Chunk 8 of 10 — Facebook Advertising Technical Framework*
