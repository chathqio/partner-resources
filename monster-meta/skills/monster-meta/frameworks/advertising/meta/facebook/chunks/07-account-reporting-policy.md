# Chunk 7: Account Structure, Reporting & Policy
## Source: Meta Business Help Center, Meta for Developers documentation, Meta Advertising Standards (current as of March 2026)

---

## Core Concept

Every Meta advertising operation rests on three pillars: account structure (how assets are organized and permissioned), reporting (how performance is measured and analyzed), and policy compliance (what you are allowed to advertise and how). Weaknesses in any pillar cascade into the others -- a poorly structured account produces unreliable reports, and policy violations can shut down even the highest-performing campaigns overnight.

This chunk provides the complete operational reference for managing the infrastructure layer of Meta advertising. It covers the Business Portfolio hierarchy, ad account organization, data source configuration, reporting dimensions and metrics (including 2025-2026 additions), A/B testing methodology, data retention constraints, and the full compliance landscape including Special Ad Categories and restricted content rules.

---

## Frameworks

---

### Framework: Business Portfolio Architecture

**When to use:** Setting up or auditing the organizational container for all Meta advertising assets.

**Structure:**

| Layer | Description | Key Limits |
|-------|-------------|------------|
| **Business Portfolio** (formerly Business Manager) | Central hub that owns/manages all Meta assets | Max 2 per personal Facebook profile |
| **People** | Team members with assigned roles | Admin, Employee (portfolio-level) |
| **Ad Accounts** | Individual advertising accounts within the portfolio | New portfolios start with 1; request more as spend history grows |
| **Pages** | Facebook Pages connected to the portfolio | No hard limit; assign per-page roles |
| **Instagram Accounts** | Connected IG business/creator accounts | Linked via Accounts Center |
| **Datasets** (formerly Pixels) | Data sources for tracking and attribution | One primary dataset per ad account recommended |
| **Catalogs** | Product feeds for dynamic ads | Organized within Commerce Manager |

**Permission Tiers:**

| Role | Portfolio Settings | Manage People | Manage Assets | View Reports | Manage Billing |
|------|-------------------|---------------|---------------|--------------|----------------|
| Admin | Full | Yes | Yes | Yes | Yes |
| Employee | None | No | Assigned only | Assigned only | No |
| Finance Analyst | None | No | No | Yes | View only |
| Finance Editor | None | No | No | Yes | Full |

**Best Practices:**
- Use one Business Portfolio per business entity. Do not mix client assets in your agency's portfolio -- request access instead.
- Enable two-factor authentication for all admins (mandatory for verified portfolios).
- Use temporary access (time-limited permissions) for contractors and short-term collaborators.
- Review and remove departed team members monthly.

---

### Framework: Ad Account Organization System

**When to use:** Setting up ad accounts for a new business, agency, or multi-brand operation.

**Naming Convention Template:**

```
[Brand/Client]-[Region]-[Purpose]-[Qualifier]
```

**Examples:**
- `AcmeCorp-US-Prospecting`
- `AcmeCorp-UK-Retargeting`
- `AcmeCorp-US-SpecialAdCategory`
- `Agency-ClientName-Main`

**When to Use Multiple Ad Accounts:**
- Different geographic regions with separate billing currencies
- Special Ad Category campaigns (must be in a separate account from non-SAC campaigns)
- Separate brands or business units requiring independent billing
- Agency structure where each client needs isolated reporting
- Testing a fresh account after severe policy strikes on an existing one

**When NOT to Split:**
- Do not create multiple accounts just to "reset" algorithm learning -- Meta tracks at the portfolio level
- Do not split prospecting vs. retargeting into separate accounts (use campaign-level separation instead)
- Do not create new accounts to circumvent policy enforcement -- this results in permanent bans

**Ad Account Limits:** New portfolios begin with 1 ad account. Limits increase based on spend history and account standing. Request increases through Business Settings > Ad Accounts.

---

### Framework: Dataset & Catalog Configuration

**When to use:** Connecting first-party data sources and product catalogs to ad accounts.

**Dataset Configuration (formerly Pixel + CAPI):**

| Data Source | Setup Method | Use Case |
|-------------|-------------|----------|
| Website | Meta Pixel + Conversions API (CAPI) | Standard web conversion tracking |
| App | Meta SDK | Mobile app install/event tracking |
| Offline | Offline Conversions API | In-store, phone, or CRM conversions |
| Chat | Messaging integrations | Lead capture via Messenger/WhatsApp |
| CRM | Customer list uploads | Custom Audiences from first-party data |

**Setup Priority:** Always implement both Pixel (browser-side) and Conversions API (server-side) for redundant, privacy-resilient tracking. Browser-only tracking loses 20-40% of conversions due to ad blockers and iOS privacy controls.

**Catalog & Commerce Manager:**

| Element | Description |
|---------|-------------|
| Product Feed | CSV, TSV, XML, or Google Sheets file containing product data (ID, title, description, price, image URL, availability) |
| Feed Schedule | Auto-update hourly, daily, or weekly |
| Product Sets | Subsets of catalog for targeting specific product groups in dynamic ads |
| Dynamic Product Ads | Automatically show users the products they viewed, added to cart, or similar items |
| Catalog Diagnostics | Built-in tool to identify feed errors, missing fields, and rejected products |

**Feed Best Practices:** Include `google_product_category`, `brand`, `condition`, `availability`, and at least 3 high-quality images per product. Products with missing required fields are rejected from dynamic delivery.

---

### Framework: Reporting Dashboard Template

**When to use:** Building standardized reporting views for different campaign types.

**Essential Metrics by Campaign Type:**

| Metric | Awareness | Traffic | Lead Gen | Sales/ROAS |
|--------|-----------|---------|----------|------------|
| Reach | Primary | Monitor | Monitor | Monitor |
| Impressions | Primary | Monitor | -- | -- |
| Frequency | Primary | Monitor | Monitor | Monitor |
| CPM | Primary | Monitor | Monitor | Monitor |
| CPC (Link Click) | -- | Primary | Primary | Monitor |
| CTR (Link Click) | -- | Primary | Primary | Monitor |
| CPA (Cost per Action) | -- | -- | Primary | Primary |
| Conversion Rate | -- | -- | Primary | Primary |
| ROAS | -- | -- | -- | Primary |
| Purchase Value | -- | -- | -- | Primary |

**Core Metric Definitions:**

| Metric | Formula | What It Tells You |
|--------|---------|-------------------|
| **CPM** | (Spend / Impressions) x 1,000 | Cost to reach 1,000 people; measures demand/competition for your audience |
| **CPC** | Spend / Link Clicks | Cost per click to your destination |
| **CTR** | (Link Clicks / Impressions) x 100 | Ad relevance and creative effectiveness |
| **CPA** | Spend / Conversions | Acquisition cost per desired action |
| **ROAS** | Purchase Value / Spend | Revenue generated per dollar spent |
| **Frequency** | Impressions / Reach | Average times each person saw your ad |
| **Reach** | Unique users who saw ad | Audience penetration |
| **Impressions** | Total ad displays | Volume of delivery (includes repeats) |

**New Metrics (2025-2026):**

| Metric | Description | Action Threshold |
|--------|-------------|-----------------|
| **Creative Fatigue Indicator** | Flags ads experiencing performance decline due to audience overexposure | Replace creative when flagged; declining conversion efficiency is the primary signal (not just CTR drops) |
| **Creative Similarity Score** | Measures visual/thematic overlap between ads in the same account | High similarity raises CPMs via Andromeda algorithm penalty; diversify hooks, formats, and visual styles |
| **Audience Segments Breakdown** | Breaks Sales campaign results by New Customers, Existing Customers, Engaged Audience | Available only on Sales objective campaigns |
| **Value Rules Breakdown** | Shows results with and without value rules applied | Compare attributed value across customer segments |

**Available Reporting Breakdowns:**

| Category | Breakdowns |
|----------|-----------|
| **Time** | Day, Week, 2 Weeks, Month |
| **Demographics** | Age, Gender, Age and Gender, Country, Region, DMA Region |
| **Delivery** | Placement, Platform, Device, Platform and Device, Placement and Device |
| **Time of Day** | By Ad Account Time Zone, By Viewer's Time Zone |
| **Action** | Conversion Device, Product ID, Carousel Card, Video View Type, Video Sound, Reactions |

**Note:** When optimizing for offsite conversions, available breakdowns are limited to Impression Device, Platform and Device, and Placement.

---

### Framework: Custom Metrics & A/B Testing

**When to use:** When standard metrics are insufficient and you need business-specific KPIs, or when you need statistically valid tests to guide optimization decisions.

**Custom Metric Formulas (create in Ads Manager > Columns > Custom Metrics):**

| Custom Metric | Formula | Use Case |
|---------------|---------|----------|
| Profit per Purchase | `Purchase Value - Spend` (at ad level) | True profitability after ad cost |
| Break-Even ROAS | `1 / Profit Margin` (reference calc) | Minimum ROAS target (e.g., 25% margin = 4.0x) |
| True CPA | `Spend / Offline Conversions` | When final conversion happens off-platform |
| Lead-to-Sale Rate | `Purchases / Leads` | Funnel quality indicator |
| Cost per MQL | `Spend / Qualified Leads` (custom event) | When using lead scoring |
| Efficiency Ratio | `Spend / Revenue` | Lower is better; inverse of ROAS |
| Revenue per Impression | `Purchase Value / Impressions` | Creative revenue efficiency |

**A/B Testing Tool (Experiments):**

| Parameter | Requirement |
|-----------|-------------|
| Variables you can test | Creative, Audience, Placement, Delivery Optimization (one at a time) |
| Minimum duration | 7 days recommended (5-day minimum enforced) |
| Maximum duration | 30 days |
| Audience isolation | Automatic non-overlapping split |
| Minimum conversions | 50-100 per variation for statistical confidence |
| Minimum budget | $300-500 per variation recommended |
| Winner declaration | Meta auto-declares with confidence percentage |
| Significance threshold | Meta uses standard statistical significance; results indicate probability of repeatability |

**A/B Test Decision Rules:**
- If confidence > 90%: implement the winner
- If confidence 70-90%: directional signal; retest with higher budget
- If confidence < 70%: inconclusive; increase sample size or test duration
- Always test one variable at a time; multi-variable tests produce ambiguous results

---

### Framework: 13-Month Data Retention Response Plan

**When to use:** Planning data export and archival strategy in response to Meta's January 2026 API data retention limits.

**What Changed (Effective January 12, 2026):**

| Data Type | Retention Limit |
|-----------|----------------|
| Unique-count fields (unique actions, cost per unique action) with any breakdown | 13 months |
| Hourly breakdowns across all fields | 13 months |
| Frequency breakdowns | 6 months |
| 7-day and 28-day view-through attribution windows | Deprecated entirely |
| MMM breakdowns | Async API jobs only (no real-time sync access) |

**Required Actions:**
1. **⚠️ Export historical data NOW — this data is permanently gone.** Any unique-count or hourly data older than 13 months is permanently inaccessible via API. Data using the deprecated 7-day and 28-day view-through attribution windows is also permanently unrecoverable — it cannot be re-queried under the new attribution model. If you have not exported, that data is already lost and there is no recovery path.
2. **Set up automated monthly exports** of all reporting data to your data warehouse (BigQuery, Snowflake, or even Google Sheets for small accounts).
3. **Shift attribution analysis** to 7-day click and 1-day view windows (the surviving defaults).
4. **Update dashboards** that reference deprecated attribution windows; replace with Conversions API-sourced data where possible.
5. **Document baseline metrics** from pre-change periods so year-over-year comparisons remain valid even when the underlying data is no longer query-able.

---

### Framework: Account Health Audit Checklist

**When to use:** Monthly review of account structure, compliance, and reporting integrity.

**Account Structure (Monthly):**
- [ ] All team members still active and roles appropriate
- [ ] No unauthorized users with admin access
- [ ] Two-factor authentication enabled for all admins
- [ ] Ad account naming conventions followed consistently
- [ ] Inactive ad accounts flagged or archived
- [ ] Business verification status current

**Data & Tracking (Monthly):**
- [ ] Pixel firing correctly on all key pages (use Meta Pixel Helper)
- [ ] Conversions API sending redundant server-side events
- [ ] Event match quality score above 6.0 (ideally 8.0+)
- [ ] Dataset diagnostics show no unresolved errors
- [ ] Catalog feed updating on schedule with zero rejected products
- [ ] Custom conversions still mapped correctly after any site changes

**Policy & Compliance (Monthly):**
- [ ] Account Quality dashboard reviewed -- no pending policy issues
- [ ] Special Ad Category correctly declared on all applicable campaigns
- [ ] No ads running with restricted content without required disclaimers
- [ ] Ad rejection rate trending -- investigate if above 10%
- [ ] Business verification and any required advertiser identity confirmations up to date

**Reporting & Data (Monthly):**
- [ ] Historical data export ran successfully for the prior month
- [ ] Custom metrics still calculating correctly (spot-check 3 campaigns)
- [ ] Creative fatigue indicators reviewed -- flagged creatives swapped
- [ ] Creative similarity score checked -- diversify if score is high
- [ ] Frequency caps reviewed -- no campaigns above 3.0 frequency on prospecting audiences

---

## Key Principles

- **One Business Portfolio per business entity.** Agencies should request access to client assets, not house them in the agency's portfolio. Each personal profile can own a maximum of 2 Business Portfolios.
- **Pixel + CAPI together is mandatory.** Browser-only tracking is unreliable in a post-iOS-14.5 world. Server-side events via Conversions API are the baseline, not an upgrade.
- **Special Ad Categories are not optional.** Failure to declare the correct category results in ad rejection, account restriction, or permanent ban. When in doubt, declare.
- **Creative diversity protects CPMs.** Meta's Andromeda algorithm penalizes accounts with high creative similarity by raising CPMs. Vary hooks, formats, visual styles, and messaging angles across ad sets.
- **Data older than 13 months is gone.** After January 2026, unique-count metrics and hourly breakdowns beyond 13 months are permanently inaccessible via API. Export proactively.
- **Frequency is the silent killer.** Monitor frequency weekly on prospecting campaigns. Above 3.0 frequency, creative fatigue accelerates and CPA rises sharply.
- **A/B tests need volume, not time.** Statistical significance comes from conversions, not calendar days. Budget appropriately for 50-100 conversions per variation minimum.
- **Appeal rejections promptly but strategically.** Use Account Quality to request reviews within 30 days. After a rejected appeal, you cannot resubmit for 30 days -- make your first appeal thorough.
- **Naming conventions are infrastructure.** Consistent naming across campaigns, ad sets, and ads enables automated reporting, cross-account analysis, and faster troubleshooting.
- **Custom metrics reveal true performance.** Standard ROAS ignores COGS. Build break-even ROAS and profit-per-purchase custom metrics to make spend decisions based on actual profitability.

---

## Decision Tools

### Special Ad Category Determination Flowchart

```
START: What does your ad promote?
|
+--> Housing (rentals, sales, mortgage, insurance, home improvement financing)?
|    --> YES --> Declare: Housing
|
+--> Employment (job listings, recruitment, career opportunities)?
|    --> YES --> Declare: Employment
|
+--> Financial Products or Services (credit, loans, banking, savings,
|    insurance, investments, crypto, financial advisory)?
|    --> YES --> Declare: Financial Products and Services
|    NOTE: This replaced the old "Credit" category in late 2024.
|    Mandatory for ALL financial product advertisers as of early 2025.
|
+--> Social Issues, Elections, or Politics?
|    --> YES --> Declare: Social Issues, Elections or Politics
|    (Requires additional identity verification and "Paid for by" disclaimers)
|
+--> None of the above?
     --> No Special Ad Category required
     --> BUT check Restricted Content list below before proceeding
```

**Special Ad Category Targeting Restrictions (all categories):**
- Age: locked to 18-65+
- Gender: must include all genders
- Location: city/county/region only (no ZIP/postal code targeting)
- Lookalike Audiences: not available (use Special Ad Audiences instead)
- Customer List Custom Audiences: must certify lists do not use prohibited data (enforced March 2025 for US advertisers)

**⚠️ Compounding restriction impact (2026):** With the June 2025 interest targeting consolidation also removing granular interest categories, SAC campaigns are now effectively limited to broad demographics + custom audiences only. The combination of SAC restrictions + interest deprecation means these campaigns have the narrowest targeting toolkit on the platform. Strategy must rely heavily on creative diversity, first-party data (customer lists), and Advantage+ Audience expansion to find qualified prospects.

### Restricted & Prohibited Content Quick Reference

| Category | Status | Requirements |
|----------|--------|-------------|
| Alcohol | Restricted | Must comply with local laws; age-gated targeting required |
| Gambling & Lotteries | Restricted | Prior written permission + geo-restrictions |
| Health & Wellness | Restricted | No before/after images; no unrealistic claims; Purchase/Add-to-Cart events restricted (Jan 2025) |
| Political/Social Issues | Special Category | Identity verification + "Paid for by" disclosure |
| Supplements | Restricted | No health cure claims; must comply with local regulations |
| Dating | Restricted | Prior written approval required |
| Cryptocurrency | Restricted | Prior written approval; no misleading yield claims |
| Illegal products/services | Prohibited | No exceptions |
| Weapons/ammunition | Prohibited | Includes accessories and modifications |
| Tobacco/nicotine | Prohibited | Includes e-cigarettes and vaping |
| Misleading health claims | Prohibited | Includes miracle cures and anti-vaccine content |
| Discriminatory practices | Prohibited | Any ad that discriminates based on protected characteristics |
| Deceptive financial products | Prohibited | Payday loans, penny auctions, ICOs without approval |

### Ad Review & Appeal Process

```
Ad Submitted --> Automated Review (minutes to hours)
|
+--> Approved --> Ad runs
|
+--> Rejected --> Notification with policy cited
     |
     +--> Fix and Resubmit (fastest path)
     |
     +--> Request Review in Account Quality (3-7 business days)
          |
          +--> Approved --> Ad runs
          |
          +--> Rejected --> 30-day cooldown before next appeal
               |
               +--> Submit detailed appeal via Business Support Home
               +--> Include: compliance explanation, creative context,
                    business legitimacy documentation
```

### When to Escalate Account Issues

| Situation | Action |
|-----------|--------|
| Single ad rejected | Fix creative/copy and resubmit; or appeal if compliant |
| Multiple ads rejected same day | Pause and audit all active ads before resubmitting; may indicate policy shift |
| Ad account restricted | Review Account Quality; submit appeal with documentation |
| Business Portfolio restricted | Contact Meta Business Support directly; prepare business verification documents |
| Permanent ban threat | Engage Meta marketing partner or agency rep if available; document full compliance history |

---

*Chunk 7 of 10 -- Facebook Advertising Technical Framework*
