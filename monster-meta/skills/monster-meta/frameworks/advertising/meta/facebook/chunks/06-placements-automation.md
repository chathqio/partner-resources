# Chunk 6: Placements & Automation
## Source: Meta Business Help Center, Meta Engineering Blog, Jon Loomer Digital, practitioner consensus

---

## Core Concept

Where your ad appears and how the system decides to show it are two sides of the same coin. Meta offers 19+ placement options across five platforms --- Facebook, Instagram, Messenger, Audience Network, and Threads. Each placement has different creative requirements, user intent signals, and cost profiles. The fundamental strategic question is whether to select placements manually or let Meta's AI distribute delivery automatically via Advantage+ Placements.

In 2025, Meta's ad delivery infrastructure underwent a generational shift. The Andromeda retrieval engine (global October 2025) moved the system from audience-first to creative-first matching, delivering 20-35% ROAS lifts for compliant advertisers. The GEM foundation model (live since Q2 2025) made ad ranking 4x more efficient and drove 5% more conversions on Instagram and 3% more on Facebook Feed. These changes reward advertisers who provide creative variety, broad targeting, and clean signal --- and penalize those clinging to narrow audiences and single-creative ad sets. Automation tools like Campaign Budget Optimization and Automated Rules give you systematic control over scaling winners and killing losers without manual babysitting.

---

## Frameworks

### Framework: Complete Placement Map

**When to use:** When planning placement strategy or building placement-specific creative assets.

#### Facebook Placements

| Placement | Format | Aspect Ratio | Notes |
|---|---|---|---|
| **Feed** | Image, Video, Carousel, Collection | 1:1 or 4:5 | Highest volume placement; primary real estate |
| **Right Column** | Image | 1:1 | Desktop only; low cost, low engagement; best for retargeting |
| **Marketplace** | Image, Video, Carousel | 1:1 or 4:5 | High purchase intent; commerce-focused audience |
| **Stories** | Image, Video | 9:16 (full screen) | 5-15 second attention window; swipe-up CTA |
| **Reels** | Video | 9:16 (full screen) | Sound-on, fast-paced; 15-90 seconds; highest growth placement |
| **In-Stream Video** | Video | 16:9 or 1:1 | Mid-roll in long-form video content; non-skippable (5-15s) |
| **Search Results** | Image, Video | 1:1 or 4:5 | Appears alongside organic search results; high intent |

#### Instagram Placements

| Placement | Format | Aspect Ratio | Notes |
|---|---|---|---|
| **Feed** | Image, Video, Carousel, Collection | 1:1 or 4:5 | Core placement; supports shopping tags |
| **Explore** | Image, Video | 1:1 or 4:5 | Discovery-focused; reaches users browsing new content |
| **Stories** | Image, Video | 9:16 (full screen) | Ephemeral feel; swipe-up/link sticker CTA |
| **Reels** | Video | 9:16 (full screen) | Highest organic reach potential; sound-on default |
| **Shop** | Image, Carousel | 1:1 | E-commerce product discovery; catalog-connected |

#### Messenger Placements

| Placement | Format | Aspect Ratio | Notes |
|---|---|---|---|
| **Sponsored Messages** | Text + Image | N/A | Sent directly to users who have existing conversations; re-engagement |
| **Stories** | Image, Video | 9:16 | Similar to Facebook/IG Stories; lower volume |

*Note: Messenger Inbox placement was removed by Meta in late 2025.*

#### Audience Network Placements

| Placement | Format | Notes |
|---|---|---|
| **Native** | Image, Video | Blends into third-party app content |
| **Banner** | Image | Standard display banner in apps |
| **Interstitial** | Image, Video | Full-screen between app content |
| **Rewarded Video** | Video | User watches ad to unlock in-app reward; high completion rates |

*Audience Network extends reach to third-party apps/sites. Volume is large but quality and brand safety are lower. Best for top-of-funnel reach at low CPM.*

#### Threads Placement (New 2025-2026)

| Placement | Format | Aspect Ratio | Notes |
|---|---|---|---|
| **Feed** | Image, Video, Carousel | 1:1 or 4:5 | Global rollout January 2026; 400M+ MAU; image + video + carousel (image-only carousel) |

Threads ads support: image ads, video ads, carousel ads (image-only), Advantage+ catalog ads (image/carousel only), and app install ads.

**⚠️ Threads is a priority test placement for 2026:** With 400M+ MAUs (globally available January 2026), Threads is Meta's fastest-growing placement. Early data shows strong performance for prospecting and awareness campaigns with lower CPMs than established placements. Test Threads in your Advantage+ Placements mix — the algorithm will allocate spend there when it finds converters.

---

### Framework: Placement-Specific Creative Requirements

**When to use:** When building creative assets to ensure they render correctly across all placements.

| Dimension | Feed (FB/IG) | Stories/Reels | Right Column | In-Stream |
|---|---|---|---|---|
| **Primary aspect ratio** | 1:1 or 4:5 | 9:16 | 1:1 | 16:9 or 1:1 |
| **Resolution (min)** | 1080x1080 | 1080x1920 | 254x254 | 1080x1080 |
| **Video length** | Up to 240 min | 5-15s (Stories), 15-90s (Reels) | N/A | 5-15s |
| **Text overlay** | Minimal (no hard limit, but <20% performs better) | Minimal; keep in safe zone (top/bottom 14% may be obscured by UI) | Minimal | None recommended |
| **Primary text** | 125 chars visible before "See More" | Not shown (creative only) | Short (limited space) | Not shown |
| **Headline** | 27 chars visible | Not shown | 27 chars | Not shown |
| **Sound** | Off by default (Feed) | On by default (Reels) | N/A | On by default |

**Best practice:** Create 3 asset versions minimum:
1. **1:1 square** --- covers Feed, Marketplace, Search, Explore
2. **4:5 vertical** --- optimized for Feed with maximum screen real estate
3. **9:16 full vertical** --- covers Stories and Reels across all platforms

---

### Framework: Advantage+ Placements vs Manual Placements

**When to use:** When deciding how to configure placement delivery at the ad set level.

| Factor | Advantage+ Placements | Manual Placements |
|---|---|---|
| **How it works** | Meta distributes budget across all eligible placements automatically | You select exactly which placements receive delivery |
| **Best for** | Prospecting, broad audiences, conversion campaigns, new campaigns | Retargeting, placement-specific creative tests, brand safety concerns |
| **Performance** | Generally lower overall CPA (Meta optimizes for cheapest conversions) | Higher control but potentially higher CPA |
| **Creative requirement** | Must provide assets in all aspect ratios (1:1, 4:5, 9:16) | Can tailor creative to specific placements |
| **Andromeda compatibility** | Fully compatible; rewards creative variety | Works but limits algorithm's optimization surface |
| **Learning phase** | Exits faster (more placement options = more data signals) | Slower exit (fewer signals from restricted placements) |

**Default:** Start with Advantage+ Placements. Review placement breakdown after 2 weeks. Exclude any placement with CPA > 3x average. Switch to Manual only for retargeting with placement-specific creative or brand safety concerns (exclude Audience Network).

**⚠️ October 2025 change — Placement exclusions are no longer absolute:** Meta now spends up to 5% of budget on "excluded" placements if the algorithm predicts conversions there. Exclusions are treated as strong preferences, not hard blocks. Monitor placement breakdowns even on campaigns with exclusions set.

---

### Framework: Andromeda Algorithm & Ad Delivery (Global October 2025)

**When to use:** When structuring campaigns, creative, and targeting for Meta's current delivery system.

Andromeda is Meta's AI-powered ads retrieval engine that shifted delivery from **audience-first** to **creative-first** --- matching the most relevant creative to each user based on thousands of behavioral signals.

**Performance:** 20-35% ROAS lift for compliant advertisers; +7% conversions with image generation. Narrow audiences and single-creative ad sets are actively penalized.

**Andromeda-optimized structure:**
- 1 campaign with Advantage Campaign Budget
- 1-2 ad sets with broad targeting (minimal exclusions)
- 10-50+ unique creative concepts per ad set (the old 6-ad or 10-20 ad convention is outdated; Andromeda's retrieval capacity handles 50+ post IDs efficiently)
- Multiple formats: static, video, carousel, Reels-native
- Let the algorithm allocate spend to winning creative/placement combos

---

### Framework: GEM (Generalized Engagement Model)

**When to use:** When understanding why Meta's ad ranking has changed and how to align with it.

GEM is Meta's largest ads foundation model, replacing placement-specific ranking models with a unified cross-platform model.

- **4x more efficient** at driving performance gains per unit of data and compute vs. previous models
- **5% more conversions** on Instagram, **3% more** on Facebook Feed (live since Q2 2025)
- Shares learnings across all Meta properties; analyzes both organic and paid signals
- **Key implication:** GEM rewards genuine engagement (saves, shares, comments, watch time), not just clicks. Creative that people interact with organically gets ranked higher in paid auctions.

---

### Framework: Opportunity Score (0-100)

**When to use:** When auditing campaign setup quality and identifying optimization gaps.

Introduced June 2025, Opportunity Score is Meta's assessment of how well your campaigns are configured relative to best practices. It measures **configuration quality**, not performance.

**Score components:**

| Dimension | What It Evaluates |
|---|---|
| **Creative variety** | Number of unique creative concepts, format diversity (static, video, carousel), aspect ratio coverage |
| **Signal quality** | Pixel + CAPI implementation, EMQ scores, event coverage, conversion data freshness |
| **Audience breadth** | Targeting scope (broad vs. narrow), use of Advantage+ audience expansion |
| **Bid strategy** | Alignment between bid strategy and campaign objective |
| **Automation adoption** | Use of Advantage+ placements, Advantage Campaign Budget, automated creative tools |

**How to improve your score:**
1. Add 10-20 unique creative concepts (biggest single lever)
2. Implement CAPI and raise EMQ above 8.0
3. Broaden targeting (remove unnecessary restrictions)
4. Enable Advantage+ placements and Advantage Campaign Budget
5. Use multiple ad formats per ad set

**Important:** A high Opportunity Score does not guarantee good performance. It indicates your account is configured to give Meta's AI the best chance to optimize. Think of it as a pre-flight checklist, not a results predictor.

---

### Framework: Campaign Budget Optimization (Advantage Campaign Budget)

**When to use:** When managing budget allocation across multiple ad sets within a single campaign.

CBO (rebranded as Advantage Campaign Budget) sets budget at the campaign level and lets Meta dynamically distribute spend across ad sets based on real-time performance signals (CTR, CPA, ROAS). Budget flows to the ad set predicted to deliver the best results at the lowest cost. Performance: Andromeda-optimized accounts using CBO with broad targeting and 10-50+ creatives now see 20-35% ROAS lifts (up from the earlier 12% CPA improvement benchmark). The combination of Andromeda + CBO + creative volume is the strongest structural advantage on the platform.

**CBO vs ABO decision:**

```
IF (testing new audiences/creative with equal priority) -> ABO
IF (scaling proven campaigns) -> CBO
IF (Andromeda-optimized: 1-2 ad sets, broad targeting) -> CBO (default)
IF (mixed ad sets, very different audience sizes) -> CBO + minimum spend floors
```

**Minimum spend floors:** Set per ad set to guarantee delivery. Use sparingly --- overriding allocation reduces optimization.

---

### Framework: Placement Strategy by Funnel Stage

**When to use:** When selecting placements aligned to campaign objectives at each funnel stage.

| Funnel Stage | Objective | Recommended Placements | Rationale |
|---|---|---|---|
| **Top of Funnel (Awareness)** | Reach, Video Views | FB/IG Reels, IG Explore, FB In-Stream Video, Audience Network, Threads Feed | Maximum reach at lowest CPM; video completion builds remarketing pools |
| **Mid Funnel (Consideration)** | Traffic, Engagement, Video Views | FB/IG Feed, IG Stories, FB Search Results, IG Explore | Intent signals are stronger in Feed; Stories drive engagement |
| **Bottom Funnel (Conversion)** | Purchases, Leads, App Installs | FB/IG Feed, FB Marketplace, IG Shop, FB Search Results | Purchase-intent placements; product catalog integration |
| **Retargeting** | Conversions, Catalog Sales | FB/IG Feed, FB Right Column, IG Stories, Messenger Sponsored Messages | High frequency tolerance; Right Column is cheap for reminders; Messenger is personal |

**Default recommendation:** Use Advantage+ Placements with all-format creative at every funnel stage. Only switch to manual placements when you have a specific strategic reason (placement-specific creative, brand safety, or A/B testing placements).

---

### Framework: Automation Rules Playbook

**When to use:** When setting up automated rules to manage campaigns without constant manual monitoring.

#### Rule 1: Kill Underperformers
- **Condition:** Cost per purchase > $X (your CPA threshold) AND Amount spent > $Y (minimum for statistical significance, typically 2-3x target CPA)
- **Action:** Pause ad
- **Schedule:** Every 30 minutes
- **Why:** Prevents runaway spend on ads that have had enough data to prove they will not work

#### Rule 2: Scale Winners (Vertical)
- **Condition:** ROAS > target (e.g., 3.0) for last 3 days AND Amount spent > $100
- **Action:** Increase daily budget by 20%
- **Schedule:** Once daily
- **Why:** Gradually scales winning ad sets without resetting the learning phase (keep increases under 30%)

#### Rule 3: Creative Fatigue Alert
- **Condition:** CTR < 1.5% for last 2 consecutive days AND Impressions > 5,000
- **Action:** Send notification
- **Schedule:** Daily
- **Why:** Declining CTR signals creative fatigue or audience saturation; time to refresh creative

#### Rule 4: Frequency Cap
- **Condition:** Frequency > 3.0 (prospecting) or > 8.0 (retargeting)
- **Action:** Pause ad set or reduce budget by 25%
- **Schedule:** Daily
- **Why:** High frequency drives ad fatigue, negative feedback, and rising CPAs

#### Rule 5: Budget Protection
- **Condition:** Amount spent > daily budget x 1.5
- **Action:** Send notification
- **Schedule:** Every 2 hours
- **Why:** Catches abnormal spend spikes from algorithm fluctuations

#### Rule 6: Learning Phase Monitor
- **Condition:** Ad set active > 7 days AND status = "Learning" AND conversions < 50
- **Action:** Send notification
- **Schedule:** Daily
- **Why:** Stuck ad sets need creative refresh, broader audience, or higher budget

#### Rule 7: Dayparting Budget Adjustment
- **Condition:** Day of week = Saturday/Sunday (or your low-conversion days)
- **Action:** Decrease budget by 15% (reverse for high-conversion days)
- **Schedule:** Daily at midnight
- **Why:** Aligns spend with conversion patterns; confirm pattern with 30 days of data first

---

## Key Principles

- Meta offers 19+ placements across Facebook, Instagram, Messenger, Audience Network, and Threads; provide creative in all formats to maximize delivery options
- Advantage+ Placements outperform manual placements for most conversion campaigns --- default to Advantage+ unless you have a specific reason for manual control
- Andromeda (global October 2025) shifted ad delivery from audience-first to creative-first; 10-50+ unique creative concepts per campaign is the new baseline (Andromeda handles far more ad variants than previous systems)
- GEM makes ad ranking 4x more efficient and rewards genuine engagement (saves, shares, comments), not just clicks
- Opportunity Score measures configuration quality, not results --- use it as a setup checklist, not a performance metric
- Campaign Budget Optimization (Advantage Campaign Budget) delivers up to 12% lower CPA by letting Meta allocate spend dynamically
- Never increase budgets by more than 30% at a time --- larger jumps reset the learning phase
- Create 3 asset versions minimum: 1:1 (Feed), 4:5 (Feed optimized), 9:16 (Stories/Reels)
- Automated rules are essential for scaling --- at minimum, set up kill rules for underperformers and scale rules for winners
- Threads ads (global January 2026, 400M+ MAU) are a new placement worth testing, especially for awareness and engagement objectives

---

## Decision Tools

### Placement Decision Quick Reference

```
Awareness/Reach  -> Advantage+ (always)
Traffic          -> Advantage+ (default); Manual only for placement A/B tests
Conversions      -> Advantage+ (default)
Retargeting      -> Manual if placement-specific creative; otherwise Advantage+
Catalog Sales    -> Advantage+ (always --- catalog ads auto-adapt)

No 9:16 creative? -> Manual (exclude Stories/Reels) OR create 9:16 assets
Brand safety?    -> Advantage+ minus Audience Network
After 2 weeks    -> Exclude any placement with CPA > 3x average
```

### Automation Rule Templates (Copy-Paste Ready)

| Rule | Condition | Action | Schedule |
|---|---|---|---|
| **Budget protection** | Cost per result > CPA target x 1.5 AND spent > CPA target x 3 | Pause | Every 30 min |
| **Scale winner** | Cost per result < CPA target x 0.8 AND results > 10 (last 3d) | +20% budget (cap at 3-5x start) | Daily |
| **Creative fatigue** | CTR (link) < 1.0% AND impressions > 8,000 (last 3d) | Pause | Daily |
| **Frequency guard** | Frequency > 3.5 (last 7d) | -25% budget | Daily |

---

*Chunk 6 of 10 --- Facebook Advertising Technical Framework*
