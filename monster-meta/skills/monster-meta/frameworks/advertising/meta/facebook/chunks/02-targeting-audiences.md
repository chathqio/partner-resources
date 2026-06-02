# Chunk 02: Targeting & Audiences
## Source: Meta documentation, Jon Loomer, practitioner consensus (2025-2026)

---

## Core Concept

Targeting determines *who* sees your ads. In Meta's ecosystem, targeting has shifted dramatically from advertiser-controlled to algorithm-assisted. The old model — stack interests, layer demographics, narrow to a niche — is being replaced by broad targeting with signal-based optimization. Meta's machine learning now often outperforms manual targeting when it has sufficient conversion data. The advertiser's job has shifted from "find the audience" to "provide the signals and creative, let the algorithm find the buyers."

Despite this shift, understanding the full targeting taxonomy remains essential. Manual targeting is still critical for new accounts, niche B2B audiences, geo-specific campaigns, and controlled testing. Custom audiences and lookalikes remain the highest-performing audience types for retargeting and prospecting. The key skill in 2025-2026 is knowing *when* to control targeting manually and when to let Advantage+ Audience handle it.

---

## Frameworks

### Framework: Core Targeting Taxonomy

**When to use:** When building any ad set manually (not using Advantage+ Audience). This is the complete inventory of targeting options available in Meta Ads Manager.

#### Demographics

| Category | Options | Notes |
|---|---|---|
| **Age** | 18-65+ (1-year increments) | Minimum age 18 for all ads; some categories require 21+ |
| **Gender** | All, Men, Women | "All" is recommended default unless product is gender-specific |
| **Location** | Country, state/region, city, zip/postal code, radius (1-50 mi) | Options: people living in, recently in, or traveling in this location |
| **Language** | Any language Meta supports | Only use when targeting speakers of a specific language in a multilingual country |

#### Detailed Targeting (Interests, Behaviors, Demographics Subcategories)

| Subcategory | Examples | Notes |
|---|---|---|
| **Interests** | Business, fitness, cooking, technology, specific brands | Based on pages liked, content engaged with, and inferred interests |
| **Behaviors** | Purchase behavior, device usage, travel patterns, digital activities | Based on on-platform and off-platform activity |
| **Demographics (detailed)** | Education level, job title, industry, relationship status, life events, income (US only) | Self-reported and inferred data |

**⚠️ 2025 Deprecation — Interest Targeting Consolidation:** As of June 2025, Meta removed the majority of granular interest categories entirely. Categories tied to sports teams, food preferences, music genres, car models, niche hobbies, and similar segments were consolidated or eliminated. Interest stacking (combining multiple narrow interests for precise targeting) is no longer a viable strategy. The remaining interest categories are broad groupings that offer minimal targeting precision compared to pre-2025. For cold prospecting, lookalike audiences and Advantage+ Audience are now the primary tools — interest targeting should be considered a supplementary signal at best, not a targeting strategy.

**2025 change — Targeting exclusions removed:** As of March 2025, detailed targeting exclusions (the ability to exclude specific interests or behaviors) have been removed. You can no longer say "interested in marketing but NOT interested in SEO." Custom audience exclusions still work.

---

### Framework: Custom Audience Types

**When to use:** When building retargeting audiences, seed audiences for lookalikes, or exclusion lists. Custom audiences are your highest-intent, highest-value targeting tool.

#### 1. Website Custom Audiences (WCA)

Built from Meta Pixel and Conversions API (CAPI) data.

| Retention Window | Use Case | Example |
|---|---|---|
| **1-3 days** | Ultra-hot retargeting — cart abandoners, checkout initiators | "Added to cart in last 3 days but didn't purchase" |
| **7 days** | High-intent visitors — viewed product, visited pricing page | "Visited pricing page in last 7 days" |
| **14-30 days** | Warm retargeting — general site visitors | "All website visitors, last 30 days" |
| **60-90 days** | Mid-funnel nurture — broader reach for consideration messaging | "Visited any page, last 90 days" |
| **180 days** | Maximum window — largest possible retargeting pool | "All visitors, last 180 days" (max retention) |

**Event-based WCA options:**
- All website visitors
- People who visited specific web pages (URL contains/equals)
- Visitors by time spent (top 5%, 10%, 25% by time on site)
- Custom events: Purchase, AddToCart, InitiateCheckout, Lead, ViewContent, CompleteRegistration, or any custom event
- Combination rules: Include people who did X AND/OR Y, exclude those who did Z

**Requirements:** Meta Pixel installed + Conversions API (CAPI) recommended. Event Match Quality score of 6+ for reliable audience building.

#### 2. Customer List Custom Audiences

Upload your own customer data (CRM, email list, purchase records) for Meta to match against its user base.

**Formatting requirements:**
- Accepted identifiers: email, phone, first name, last name, city, state, zip, country, date of birth, gender, mobile advertiser ID
- Format: CSV or TXT file
- Emails: lowercase, trimmed of whitespace
- Phone numbers: include country code, digits only (no dashes, spaces, parentheses)
- More identifiers per record = higher match rate

**Match rates:**
- Email only: 40-60% typical match rate
- Email + phone: 60-75% match rate
- Email + phone + name + zip: 70-85% match rate
- First-party data via CAPI: up to 80-90% match rate

**Best practices:**
- Upload at least 1,000 records (Meta's minimum for audience creation)
- Include as many identifier columns as possible
- Use hashed data uploads via the API for privacy compliance
- Refresh lists monthly — audiences do not auto-update (unless using a sync integration)
- Segment your list before upload: purchasers, leads, high-LTV, churned — each becomes a distinct audience

#### 3. App Activity Custom Audiences

Built from people who have taken specific actions in your mobile app (requires Meta SDK integration).

Options: opened app, made purchase, achieved level, added payment info, or any custom app event. Retention windows: 1-180 days.

#### 4. Engagement Custom Audiences

Built from people who have interacted with your content *on Meta's platforms* — no Pixel required.

| Engagement Source | Options | Max Retention |
|---|---|---|
| **Video** | People who watched 3s, 10s, 15s, 25%, 50%, 75%, 95% of a video | 365 days |
| **Lead Form** | People who opened or submitted an Instant Form | 90 days |
| **Instagram Account** | Visited profile, engaged with post/ad, sent message, saved post | 365 days |
| **Facebook Page** | Visited page, engaged with post/ad, clicked CTA, sent message | 365 days |
| **Shopping** | Viewed products, added to cart, purchased via Shops | 365 days |
| **Events** | People who responded to or interacted with a Facebook Event | 365 days |
| **AR Experience** | People who opened an AR experience on Facebook or Instagram | 365 days |

**Strategic note:** Video view audiences (especially 50%+ and 75%+ viewers) are among the most valuable engagement audiences. They indicate genuine interest without requiring a website visit and can be built for free through organic content or low-cost awareness campaigns.

#### 5. Offline Activity Custom Audiences

Built from offline conversion data uploaded manually or via partner integration. Matches in-store purchases, phone orders, or other offline events to Meta users. Requires offline event setup in Events Manager.

#### 6. Catalog Custom Audiences

Built from people who interacted with items in your product catalog. Options include viewed products, added to cart, purchased. Enables dynamic retargeting with personalized product ads.

---

### Framework: Lookalike Audiences

**When to use:** For prospecting — finding new customers who resemble your best existing customers. Lookalikes remain one of the most powerful targeting tools in Meta's arsenal despite the rise of broad targeting.

**How it works:** You provide a source audience (custom audience). Meta analyzes the shared characteristics of that audience and finds new people who are statistically similar.

| Percentage | Audience Size (US) | Similarity | Use Case |
|---|---|---|---|
| **1%** | ~2.4 million | Highest | Best for direct response / conversion campaigns |
| **2-3%** | ~4.8-7.2M | High | Good balance of reach and quality |
| **4-5%** | ~9.6-12M | Moderate | Broader prospecting, awareness |
| **6-10%** | ~14.4-24M | Lower | Maximum reach, brand awareness only |

**Source audience requirements:**
- Minimum: 100 people from a single country (1,000+ recommended)
- Best sources (in order of quality): Purchasers, high-LTV customers, repeat buyers, leads who converted, engaged email subscribers
- Avoid: all website visitors (too broad), all email subscribers (quality too varied)

**Value-based lookalikes:**
- Assign a monetary value to each person in your source audience (e.g., customer LTV)
- Meta weights the lookalike toward users who resemble your *highest-value* customers, not just any customer
- Delivers 20-40% better ROAS vs standard lookalikes in practitioner testing
- Requires customer list upload with a "value" column, or Pixel with purchase value data

**Multi-country lookalikes:**
- Available for campaigns targeting multiple countries simultaneously
- Meta finds similar users in each target country based on a source from any single country
- Useful for global e-commerce or SaaS with international audiences

**2025-2026 context:** Lookalikes are still effective but increasingly redundant when Advantage+ Audience is available. Many practitioners use lookalikes as "audience suggestions" within Advantage+ rather than as hard targeting constraints.

---

### Framework: Advantage+ Audience (Broad Targeting)

**When to use:** When you have strong conversion data (50+ events/week), diverse creative, and want to let Meta's algorithm find buyers without manual audience restrictions.

**What it is:** Advantage+ Audience replaces the old "broad targeting" approach and is now the default targeting setting in new campaign creation. Your targeting inputs (interests, demographics, custom audiences) become *suggestions* rather than hard constraints. Meta uses them as starting signals but will expand beyond them if it predicts better results.

**How "audience suggestions" work:**

| Input Type | What Meta Does With It |
|---|---|
| **Custom audience** | Uses as a starting signal — prioritizes similar users first, then expands |
| **Interests** | Starts delivery in this interest pool, expands to adjacent and unrelated interests if performance warrants |
| **Age/Gender** | Treats as a suggestion — may show ads outside your specified range if it predicts conversions |
| **Location** | Typically respected as a hard constraint (depends on campaign settings) |

**When algorithm outperforms manual targeting:**
- Account has 50+ weekly conversion events on the Pixel
- You have 5+ diverse creative assets (the algorithm uses creative as a targeting signal)
- Your product has broad appeal (not hyper-niche B2B)
- You are optimizing for a clear bottom-funnel event (purchase, lead)

**When manual targeting still wins:**
- New ad accounts with sparse Pixel data
- Hyper-niche B2B audiences (e.g., "CTO at SaaS companies with 50-200 employees")
- Geo-restricted offers (local businesses, regional promotions)
- When you need to exclude specific audiences precisely
- Product category restrictions or compliance requirements

**Critical setting:** If you uncheck "Use as a suggestion" for any input, Meta stops treating it as a suggestion and it becomes a hard constraint. This effectively reverts to manual targeting for that parameter.

---

### Framework: Audience Exclusions

**When to use:** To prevent wasted spend on people who should not see your ad — existing customers, recent purchasers, or audiences targeted by other campaigns.

**Available exclusion types (2026):**

With detailed targeting exclusions removed (March 2025), custom audience exclusions are now the **only viable exclusion mechanism** on Meta. All exclusion strategy must be built around custom audiences.

| Exclusion Type | How to Apply | Notes |
|---|---|---|
| **Custom audience exclusion** | Add custom audience as an exclusion at the ad set level | The only remaining exclusion tool — exclude purchasers, existing customers, email lists, engagement audiences |
| **Existing customer exclusion (ASC)** | Define "existing customers" in ASC settings; set budget cap (0-50%) | ASC-specific control; requires customer list upload |
| **Detailed targeting exclusion** | **REMOVED** as of March 2025 | No longer available — cannot exclude interests/behaviors; build custom audiences to replicate any needed exclusions |

**Best practices for exclusions:**
- Always exclude recent purchasers (7-30 day window) from prospecting campaigns
- Exclude leads who already converted from lead gen campaigns
- In ASC, upload your customer list and set existing customer budget cap to 0-10% for pure acquisition
- Create a "master exclusion" audience of all customers and update monthly

---

### Framework: Sensitive Data Restrictions (September 2025)

**When to use:** Compliance awareness — understanding what targeting capabilities have been removed.

**What changed (September 2, 2025):**
Meta began proactively scanning and disabling custom audiences and custom conversions that reference or imply sensitive information.

**Categories affected:**
- **Health conditions:** Audiences named or structured around specific conditions (diabetes, arthritis, cancer, mental health)
- **Financial status:** Audiences referencing credit scores, income levels, debt, bankruptcy
- **Political affiliation:** Audiences based on party membership or political beliefs
- **Race/ethnicity:** Any audience segmented by racial or ethnic identity
- **Sexual orientation:** Audiences based on LGBTQ+ identity
- **Religious beliefs:** Audiences segmented by religion

**Practical impact:**
- Custom audiences with flagged names/metadata stop growing and may be disabled
- Custom conversions with sensitive naming stop collecting data
- Lookalikes built from flagged source audiences are also disabled
- Even if your business is in healthcare or finance, audience names cannot imply sensitive attributes

**Mitigation:** Rename audiences and conversions to neutral terms. Instead of "diabetes_interest_list," use "health_segment_A." Review all existing audiences for compliance.

---

### Framework: Audience Overlap Tool

**When to use:** Before launching campaigns with multiple ad sets targeting different audiences — to ensure you are not bidding against yourself.

**What it shows:** The percentage of users shared between two or more audiences, displayed as a Venn diagram with overlap percentages.

**How to access:** Ads Manager → Audiences → Select up to 5 audiences → Actions → Show Audience Overlap.

**Interpretation:**

| Overlap % | Risk Level | Action |
|---|---|---|
| **0-15%** | Low | Safe to run in parallel |
| **15-30%** | Moderate | Monitor CPMs — consider consolidating |
| **30-50%** | High | Consolidate into one ad set or add exclusions |
| **50%+** | Critical | You are bidding against yourself — merge audiences immediately |

**Meta's auction overlap control:** If the same user is eligible for multiple ad sets from your account, Meta generally enters only one ad into the auction. This prevents literal self-competition but causes uneven spend distribution, sluggish learning, and distorted performance signals. Prevention is better than relying on this safeguard.

**Monitoring:** Use the Inspect tool in Ads Manager to track auction overlap percentage over time. An ad set with 20%+ auction overlap is being excluded from too many auctions.

---

### Framework: Audience Ladder

**When to use:** When designing your full-funnel audience architecture — mapping specific audience types to each stage of the customer journey.

```
HOT AUDIENCES (Bottom of Funnel — Retargeting)
├── Website Custom Audience: Add-to-cart, last 7 days (exclude purchasers)
├── Website Custom Audience: Checkout initiated, last 14 days (exclude purchasers)
├── Customer List: Leads who haven't purchased
├── Engagement: Instant form opened but not submitted, last 30 days
└── Catalog: Viewed product but didn't purchase, last 14 days

WARM AUDIENCES (Middle of Funnel — Nurture)
├── Website Custom Audience: All visitors, last 30 days (exclude hot audiences)
├── Engagement: Video viewers 50%+, last 60 days
├── Engagement: Instagram engagers, last 90 days
├── Engagement: Facebook Page engagers, last 90 days
└── Customer List: Email subscribers (non-buyers)

COLD AUDIENCES (Top of Funnel — Prospecting)
├── Lookalike 1%: Based on purchasers (or high-LTV purchasers) ← PRIMARY cold tool
├── Lookalike 1%: Based on email subscribers who converted
├── Value-based Lookalike 1%: Based on customer LTV data ← highest-quality cold audience
├── Advantage+ Audience: Broad with audience suggestions ← PRIMARY cold tool (algorithm-driven)
├── Broad targeting: No targeting inputs, all demographics ← preferred over interests
└── Interest-based targeting: Supplementary signal only (post-June 2025 consolidation removed granular categories)
```

**Budget allocation by temperature:**
- Cold (prospecting): 60-70% of total budget
- Warm (nurture): 15-25% of total budget
- Hot (retargeting): 10-20% of total budget

---

### Framework: Targeting in the Advantage+ Era

**When to use:** When deciding between manual audience selection and algorithmic targeting for any campaign.

**The signal-based approach:** In 2025-2026, Meta's targeting philosophy has shifted from "tell us who to target" to "give us signals and we'll find the buyers." The three primary signals Meta uses:

1. **Conversion data** — Your Pixel + CAPI events tell Meta who buys. More events = better targeting.
2. **Creative content** — Meta analyzes your ad creative (images, video, copy) to determine who would respond. Different creatives naturally attract different audiences.
3. **Audience suggestions** — Your targeting inputs guide initial delivery but don't constrain it.

**Decision logic:**

```
Do you have 50+ conversion events per week?
├── YES
│   ├── Is your product broadly appealing?
│   │   ├── YES → Use Advantage+ Audience (broad)
│   │   │         Provide suggestions as soft signals
│   │   │         Let creative do the targeting
│   │   │
│   │   └── NO → Use Advantage+ Audience with strong suggestions
│   │             OR manual targeting for niche segments
│   │
│   └── Are you retargeting?
│       └── ALWAYS use manual targeting (custom audiences)
│             with explicit exclusions
│
└── NO
    ├── Use manual targeting to build Pixel data
    │   Start with interests + lookalikes
    │   Graduate to Advantage+ once you hit 50 events/week
    │
    └── Consider running a Traffic or Engagement campaign
        first to build engagement audiences, then retarget
```

---

### Template: Audience Architecture Worksheet

**When to use:** When planning audiences for a new campaign or auditing existing audience strategy. Fill out one worksheet per product/offer.

```
PRODUCT/OFFER: _________________________________
WEEKLY CONVERSION VOLUME: _______ events/week
PIXEL MATURITY: [ ] New  [ ] <50 events/week  [ ] 50+ events/week

─── HOT AUDIENCES (Retargeting) ───
1. WCA: _____________ | Window: ___d | Est. Size: _______
2. WCA: _____________ | Window: ___d | Est. Size: _______
3. Customer List: _____________ | Records: _______
4. Engagement: _____________ | Window: ___d | Est. Size: _______
   Exclusions applied: _________________________________

─── WARM AUDIENCES (Nurture) ───
1. WCA: _____________ | Window: ___d | Est. Size: _______
2. Engagement: _____________ | Window: ___d | Est. Size: _______
3. Customer List: _____________ | Records: _______
   Exclusions applied: _________________________________

─── COLD AUDIENCES (Prospecting) ───
1. Lookalike: Source=_________ | %=___% | Est. Size: _______
2. Lookalike: Source=_________ | %=___% | Est. Size: _______
3. Interests: _____________ | Est. Size: _______
4. Advantage+ Audience: Suggestions=_____________
   Exclusions applied: _________________________________

─── OVERLAP CHECK ───
Hot vs Warm overlap: ___% → Action: _____________
Warm vs Cold overlap: ___% → Action: _____________
Cold audiences mutual overlap: ___% → Action: _____________

─── BUDGET SPLIT ───
Cold: ___% | Warm: ___% | Hot: ___%
```

---

## Key Principles

- **The algorithm is the new targeting.** In 2025-2026, creative strategy *is* targeting strategy. Different creatives attract different audience segments — the algorithm matches them automatically.
- **Broad does not mean untargeted.** Advantage+ Audience uses conversion data, creative analysis, and behavioral signals to find buyers. "No targeting" with strong Pixel data often outperforms detailed interest stacking.
- **Custom audiences are your moat.** Website visitors, customer lists, and engagement audiences are unique to your business. Interests and behaviors are available to every competitor. Invest in building first-party data.
- **Lookalike quality depends entirely on source quality.** A 1% lookalike from your top 100 customers will outperform a 1% from all website visitors. Always use your highest-value, most-qualified source.
- **Value-based lookalikes are underused.** Adding LTV or purchase value data to your customer list before creating lookalikes delivers 20-40% better ROAS.
- **Audience freshness matters.** Retargeting audiences decay. A 7-day website visitor is far more valuable than a 180-day visitor. Use shorter windows for higher-intent actions.
- **Exclusions prevent waste.** Always exclude purchasers from prospecting, leads from lead gen, and define existing customers in ASC campaigns.
- **Overlap is silent budget destruction.** Check audience overlap before every launch. Keep overlap below 30% between ad sets in the same campaign.
- **Sensitive data restrictions are real and enforced.** Audit your custom audience and conversion names quarterly. Rename anything that implies health, financial, political, or demographic attributes.
- **The 50-event threshold is the dividing line.** Below 50 weekly conversions: manual targeting. Above 50: Advantage+ Audience becomes increasingly viable.

---

## Decision Tools

### Manual Targeting vs Advantage+ Audience Decision Matrix

| Situation | Recommended Approach | Reasoning |
|---|---|---|
| New ad account, no Pixel history | Manual (interests + lookalikes) | Algorithm has no data to work with |
| <50 conversions/week | Manual with gradual broadening | Insufficient signal for Advantage+ |
| 50-200 conversions/week | Test Advantage+ vs manual (split test) | Enough data to test; validate before committing |
| 200+ conversions/week | Advantage+ Audience (default) | Strong signal; algorithm outperforms manual in most cases |
| Hyper-niche B2B audience | Manual (detailed targeting + custom audiences) | Algorithm may not have enough signal for niche audiences |
| Retargeting campaigns | Manual (custom audiences with exclusions) | You define who to retarget; algorithm handles delivery optimization |
| Local business (<25 mile radius) | Manual with geo-targeting | Small audience; algorithm needs constraints |
| E-commerce, broad product catalog | Advantage+ Sales Campaign | ASC excels with diverse products and broad appeal |
| Compliance-restricted industry | Manual with careful audience construction | Need explicit control over who sees ads |

### Audience Health Checklist

- [ ] All retargeting audiences have fresh data (Pixel + CAPI firing, lists updated within 30 days)
- [ ] Customer list match rate is above 50% (if below, add more identifier columns)
- [ ] Lookalike source audiences contain 1,000+ high-quality records
- [ ] No audience overlap exceeds 30% between active ad sets
- [ ] Existing customer exclusions set in all prospecting campaigns
- [ ] All custom audience and conversion names reviewed for sensitive data compliance
- [ ] Engagement audiences being built through organic content or awareness campaigns
- [ ] Value-based lookalikes created from LTV-enriched customer data
- [ ] Audience suggestions populated in all Advantage+ Audience ad sets
- [ ] Retargeting windows match intent level (shorter = higher intent)

### Audience Sizing Guide

| Audience Size | Viability | Notes |
|---|---|---|
| **<1,000** | Too small | Cannot create lookalikes; limited delivery; increase retention window or source |
| **1,000-10,000** | Small but usable | Good for retargeting; marginal for prospecting |
| **10,000-100,000** | Ideal for retargeting | Strong retargeting pool; good lookalike source |
| **100,000-1,000,000** | Ideal for warm prospecting | Good for lookalike-based and interest-based campaigns |
| **1,000,000+** | Broad prospecting | Best used with Advantage+ Audience or as lookalike source |

---

*Chunk 2 of 10 — Facebook Advertising Technical Framework*
