# Chunk 01: Campaign Architecture
## Source: Meta Ads Manager documentation, Jon Loomer, practitioner consensus (2025-2026)

---

## Core Concept

Every Meta ad campaign begins with a structural decision that determines how the algorithm optimizes, who it targets, and how budget flows. Meta's Outcome-Driven Ad Experiences (ODAX) framework consolidates the old 11 objectives into 6, each mapping to a specific optimization event. The campaign level sets the objective and budget strategy; the ad set level controls audience, placement, and schedule; the ad level holds creative and copy. Getting the architecture right means the algorithm works *for* you. Getting it wrong means burning budget while the system optimizes toward the wrong outcome.

Campaign architecture also includes the choice between manual campaigns and Meta's Advantage+ automated campaign types, which increasingly dominate the platform. In 2025-2026, the trend is toward simplified, consolidated structures that give the algorithm maximum signal and flexibility, rather than the hyper-segmented structures of earlier years.

---

## Frameworks

### Framework: ODAX Objective Selection

**When to use:** At campaign creation — the very first decision. Your objective tells Meta what outcome to optimize for, which determines which users see your ads.

**The 6 ODAX Objectives:**

| Objective | Optimizes For | Use When You Want To... | Typical Funnel Stage |
|---|---|---|---|
| **Awareness** | Reach, brand recall lift, video views, store traffic | Maximize impressions, build brand recognition, reach as many people as possible | Top of funnel |
| **Traffic** | Link clicks, landing page views | Drive visits to a website, app, or landing page | Top / Mid funnel |
| **Engagement** | Post engagement, page likes, event responses, messages | Increase social proof, drive comments/shares, start conversations | Top / Mid funnel |
| **Leads** | Instant form submissions, Messenger conversations, calls, conversions | Collect contact info, book appointments, generate qualified leads | Mid / Bottom funnel |
| **App Promotion** | App installs, app events (registration, purchase) | Drive installs or in-app actions for mobile apps | Mid / Bottom funnel |
| **Sales** | Purchases, add-to-carts, conversions, catalog sales | Drive direct revenue — e-commerce, digital products, services | Bottom funnel |

**Objective selection rules:**
- If your goal is brand building with no immediate conversion expectation → **Awareness**
- If you need website visitors but don't have pixel events firing reliably → **Traffic** (optimize for landing page views, not link clicks)
- If you want social proof on a post you'll later use in conversion campaigns → **Engagement**
- If you need form fills or booked calls and have no e-commerce checkout → **Leads**
- If you have a mobile app → **App Promotion**
- If you have a website with purchase/conversion events firing via Pixel + CAPI → **Sales**

**Critical note:** Never use Traffic objective when you actually want conversions. The algorithm will find people who click, not people who buy. Always match the objective to the *end action* you want.

---

### Framework: CBO vs ABO Budget Strategy

**When to use:** After selecting your objective — deciding how budget flows across ad sets within a campaign.

**Terminology update (2025):** Meta renamed CBO to "Advantage+ Campaign Budget." ABO is now simply "Ad Set Budget." The underlying mechanics are unchanged.

| Factor | ABO (Ad Set Budget) | CBO (Advantage+ Campaign Budget) |
|---|---|---|
| **Budget control** | Fixed budget per ad set — you decide exact spend | Campaign-level budget — Meta allocates across ad sets |
| **Algorithm autonomy** | Low — you control distribution | High — Meta shifts spend to best performers |
| **Learning phase** | Each ad set has its own learning phase | Shared learning across ad sets |
| **Best for** | Testing new creatives/audiences with equal spend | Scaling proven winners, maximizing overall ROAS |
| **Risk** | Overspending on losers if you don't monitor | Meta may starve promising ad sets before they exit learning |
| **Budget changes** | Changing budget can reset learning phase | Budget changes at campaign level, less disruptive |
| **Minimum spend floors** | N/A — budget is fixed | Available — set minimum per ad set to prevent starvation |
| **Current best practice** | Use for controlled A/B testing | Use for scaling; remove minimums after ~7 days |

**The Hybrid Playbook (practitioner consensus):**

```
Phase 1: TEST with ABO
→ Equal budget per ad set
→ Each creative/audience gets fair evaluation
→ Run 3-7 days until statistical significance

Phase 2: SCALE with CBO
→ Graduate winners into CBO campaign
→ Use post ID duplication to preserve social proof
→ Set minimum spend floors for first week, then remove
→ Let algorithm concentrate budget on winners
```

**Budget allocation guideline:** 70% of total ad spend to Scale Campaign (CBO), 30% to Ongoing Testing Campaign (ABO).

**⚠️ 2025-2026 Reality Check — CBO vs ABO Distinction Is Diminishing:**
Even with ABO, Meta now auto-reallocates up to 20% of budget from one ad set to another that is outperforming. This happens automatically and cannot be disabled. This means:
- Traditional ABO testing phases no longer provide the strict budget control they once did
- A $100/day ABO ad set may only receive $80 if another ad set is outperforming
- The practical difference between CBO and ABO is much less material than before 2025
- For testing, monitor actual spend per ad set (not just set budget) to confirm fair evaluation
- The Hybrid Playbook above still works directionally, but expect less budget isolation in ABO than historically

---

### Framework: Advantage+ Campaign Types

**When to use:** When deciding between manual campaign setup and Meta's automated Advantage+ campaign types.

#### Advantage+ Sales Campaigns (ASC)

Formerly "Advantage+ Shopping Campaigns." The most mature and widely adopted Advantage+ type.

| Aspect | Manual Sales Campaign | Advantage+ Sales Campaign |
|---|---|---|
| **Audience targeting** | Full manual control (interests, behaviors, custom audiences, lookalikes) | Automated — Meta finds buyers; you provide optional "audience suggestions" as soft signals |
| **Placements** | Manual selection available | All placements — locked to Advantage+ Placements |
| **Creative** | You choose which ads run in which ad set | Up to 150 creative assets; Meta tests and allocates dynamically |
| **Budget** | ABO or CBO | Campaign-level only (CBO-like behavior) |
| **Existing customer controls** | Manual exclusions | Define "existing customers" via custom audience; set cap on % of budget spent on them (default 0-50%) |
| **A/B testing** | Full control | Limited — no ad set-level isolation |
| **Reported performance** | 22% average ROAS lift vs manual campaigns | Meta's reported benchmark across advertisers |

**⚠️ 2025-2026 Transition — Manual Campaign Deprecation:**
Legacy API creation of manual campaigns was blocked in October 2025. All new campaigns created through the API are now Advantage+ by default. Meta has announced that by May 2026, all remaining manual campaign creation (including Ads Manager UI) will be migrated to Advantage+ campaign types. Existing manual campaigns continue to run but cannot be duplicated via API. Plan account structures accordingly — manual campaigns are a legacy format with a defined end date.

**When to use ASC:**
- E-commerce brands with strong Pixel data (50+ purchases/week)
- When you have 10+ creative assets to test
- When you want to scale spend with less manual management
- When you trust the algorithm and prioritize efficiency over control

**When to use Manual instead:**
- New ad accounts with limited Pixel data
- Strict audience segmentation requirements (e.g., geo-specific offers)
- When you need to isolate variables for testing
- When targeting very niche B2B audiences

#### Advantage+ App Campaigns

Automated campaign type for the App Promotion objective. Meta handles targeting, placement, and creative optimization for app installs. Best for install-volume campaigns during launch phases. For retention or in-app purchase goals, configure detailed conversion events (registration, first purchase) rather than optimizing for installs alone.

#### Advantage+ Leads Campaigns

Launched early 2025. Automates lead generation across instant forms, Messenger, and call tracking. Meta's early testing shows a 10% reduction in cost per qualified lead vs manual lead campaigns. The system automatically adjusts which lead capture method works best for each audience segment. Represents the biggest expansion of the Advantage+ suite since ASC.

---

### Framework: Campaign Architecture Decision Tree

**When to use:** At the start of any new campaign build. Walk through this decision tree to determine objective, budget strategy, and campaign type.

```
START: What is the desired end action?

├── Brand awareness / reach / video views
│   → Objective: AWARENESS
│   → Structure: Manual campaign, CBO, 2-3 ad sets max
│
├── Website visits (no reliable conversion tracking)
│   → Objective: TRAFFIC
│   → Optimize for: Landing Page Views (not Link Clicks)
│   → Structure: Manual campaign, ABO for testing
│
├── Social proof / comments / shares / event RSVPs
│   → Objective: ENGAGEMENT
│   → Structure: Manual campaign, ABO or CBO
│
├── Lead capture (forms, calls, Messenger)
│   → Do you have 50+ leads/week on Pixel?
│   │   ├── YES → Try Advantage+ Leads Campaign
│   │   └── NO → Manual Leads campaign, ABO
│
├── App installs or in-app events
│   → Volume play? → Advantage+ App Campaign
│   → Retention/purchase focus? → Manual App Promotion, event-based optimization
│
└── Purchases / conversions / revenue
    → Do you have 50+ purchases/week on Pixel?
    │   ├── YES + 10+ creatives → Advantage+ Sales Campaign (ASC)
    │   ├── YES + limited creative → Manual Sales, CBO
    │   └── NO → Manual Sales, ABO, build Pixel data first
```

---

### Framework: Simplified vs Segmented Structure

**When to use:** When deciding how many campaigns, ad sets, and ads to run simultaneously.

**2025-2026 best practice:** Consolidate. Hyper-segmented structures (one ad set per interest, one campaign per product) fragment data and slow algorithmic learning. The algorithm needs ~50 conversion events per ad set per week to exit the learning phase.

| Structure | When to Use | Example |
|---|---|---|
| **Simplified (recommended default)** | Most advertisers; strong Pixel data; scaling phase | 2-4 campaigns total: 1 ASC + 1 testing + 1 retargeting |
| **Segmented** | Geo-specific offers, vastly different products, separate P&Ls | Separate campaigns per region or product line |

**Recommended campaign count by business size:**

| Business Size | Campaigns | Ad Sets per Campaign | Ads per Ad Set |
|---|---|---|---|
| **Small ($1K-5K/mo spend)** | 2-3 total | 2-3 | 3-5 |
| **Mid ($5K-25K/mo spend)** | 3-5 total | 3-5 | 5-10 |
| **Enterprise ($25K+/mo spend)** | 5-8 total | 3-6 | 5-15 |

**Structural anti-patterns to avoid:**
- More than 5 ad sets in a single CBO campaign (budget concentration risk)
- Fewer than 3 ads per ad set (insufficient creative variation for algorithm)
- Duplicating audiences across campaigns without exclusions (auction overlap)
- Running more campaigns than you can monitor and iterate on weekly

---

### Template: Campaign Naming Convention System

**When to use:** Before launching any campaign. Consistent naming enables filtering, reporting, and cross-team collaboration in Ads Manager.

**Format:** `[Funnel Stage]_[Objective]_[Budget Type]_[Audience/Note]_[Date]`

**Campaign Level:**
```
TOF_Sales_CBO_Broad_2026-03
MOF_Leads_ABO_Retarget-VV_2026-03
BOF_Sales_ASC_AllProducts_2026-03
TEST_Sales_ABO_CreativeTest-V3_2026-03
```

**Ad Set Level:**
```
LAL-1pct-Purchasers_25-65_AllPlacement
Interest-MarketingTools_25-55_US
Retarget-WV-30d_18-65_AllPlacement
Broad-NoTargeting_25-65_US
```

**Ad Level:**
```
Video-Testimonial-Jane-30s_V1
Carousel-ProductBenefits_V2
Image-BeforeAfter_Hook-A_V1
UGC-Unboxing-Creator3_V1
```

**Key conventions:**
- Use underscores `_` to separate fields, hyphens `-` within fields
- Include version numbers (`V1`, `V2`) for iteration tracking
- Prefix with funnel stage: `TOF`, `MOF`, `BOF`, `TEST`
- Include date as `YYYY-MM` for monthly campaigns
- Document your convention and share with all team members

---

## Key Principles

- **Objective = algorithm instruction.** The objective you choose is the single most important decision. It tells Meta's algorithm which users to find. Wrong objective = wrong audience = wasted budget.
- **Consolidation beats fragmentation.** The algorithm needs data density. Fewer, larger ad sets exit learning phase faster and optimize more efficiently than many small ones.
- **50 conversions per week per ad set** is the threshold to exit the learning phase. Structure your campaigns to hit this number.
- **Meta auto-reallocates up to 20% of ad set budgets** regardless of whether you use CBO or ABO. Even with ABO, Meta can shift up to 20% of one ad set's budget to another that is outperforming. This happens automatically and cannot be disabled, making the distinction between CBO and ABO less material than it was historically.
- **ABO for learning, CBO for earning.** Test with controlled budgets, then scale winners with algorithmic budget allocation.
- **ASC is not always better.** It requires strong Pixel data, diverse creative, and willingness to cede control. New accounts should start manual.
- **The 22% ROAS lift from ASC is an average.** Some advertisers see much more; others see worse results than manual. Test before committing full budget.
- **Naming conventions are infrastructure.** Without them, you cannot analyze performance at scale, communicate with team members, or automate reporting.
- **Meta's Opportunity Score (0-100)** evaluates your ad set configuration against best practices. Check it in Ads Manager — scores below 70 indicate structural issues.
- **Campaign structure is not set-and-forget.** Review weekly: pause underperformers, graduate winners, refresh creative, check for audience overlap.

---

## Decision Tools

### Objective Selection Matrix

| Your Situation | Recommended Objective | Budget Type | Campaign Type |
|---|---|---|---|
| Launching new brand, no Pixel data | Awareness or Traffic | ABO | Manual |
| Building email list, no e-commerce | Leads | ABO → CBO | Manual or Advantage+ Leads |
| E-commerce, strong Pixel, 10+ creatives | Sales | CBO (auto) | Advantage+ Sales (ASC) |
| E-commerce, new Pixel, <50 purchases/week | Sales | ABO | Manual |
| App launch, need install volume | App Promotion | CBO (auto) | Advantage+ App |
| Boosting post for social proof | Engagement | ABO | Manual |
| Retargeting website visitors to purchase | Sales | ABO or CBO | Manual |
| Testing new creative concepts | Sales or Leads | ABO | Manual |

### CBO vs ABO Decision Flowchart

```
Are you testing new creatives or audiences?
├── YES → Use ABO (equal budget distribution)
│         → Run 3-7 days
│         → Identify winners by CPA/ROAS
│         → Graduate winners to CBO
│
└── NO → Do you have proven winners?
         ├── YES → Use CBO
         │         → Set minimum spend floors (week 1)
         │         → Remove minimums after week 1
         │         → Monitor for budget concentration
         │
         └── NO → Start with ABO testing first
```

### Pre-Launch Structure Checklist

- [ ] Objective matches the actual desired end action (not a proxy)
- [ ] Budget strategy selected (ABO for testing, CBO for scaling, ASC if qualified)
- [ ] Campaign naming convention applied at all three levels
- [ ] No more than 5 ad sets per CBO campaign
- [ ] At least 3 ads per ad set
- [ ] No audience overlap between ad sets (checked via Audience Overlap tool)
- [ ] Conversion tracking verified (Pixel + CAPI firing correctly)
- [ ] Existing customer exclusions set (especially in ASC)
- [ ] Budget sufficient for 50 conversions/week/ad set at expected CPA

---

*Chunk 1 of 10 — Facebook Advertising Technical Framework*
