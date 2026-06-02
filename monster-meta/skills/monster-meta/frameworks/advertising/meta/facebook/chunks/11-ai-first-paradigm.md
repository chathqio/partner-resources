# Chunk 11: The AI-First Paradigm — Andromeda, GEM & Lattice
## Source: Meta engineering blog, Meta Conversions Conference 2025, Jon Loomer, Andrew Foxwell, practitioner consensus (2025-2026)

---

## Core Concept

The foundational mental model for Meta advertising in 2026 and beyond. Three AI systems — Andromeda, GEM, and Lattice — now control ad delivery end-to-end, from retrieval to ranking to prediction. Understanding how these systems work together is the difference between scaling profitably and stagnating while blaming "the algorithm."

The old paradigm was audience-first: you defined who should see your ads, then the algorithm found those people and served your creative. The new paradigm is creative-first: you supply diverse creative assets and conversion goals, and the AI systems determine who sees what, when, where, and in what format. This is not a minor optimization update — it is a fundamental architectural shift in how Meta's ad platform operates.

Meta's stated trajectory is toward a "goal-only" model where advertisers set business outcomes and budgets, and AI handles everything else. Manual controls are being systematically removed. Advertisers who adapt their account structures, creative processes, and measurement frameworks to work with these systems will outperform. Those who fight them — clinging to manual targeting, micro-segmented campaigns, and bid overrides — will see progressively worse results as the platform evolves away from them.

---

## Frameworks

### Framework: Andromeda Retrieval System

**When to use:** When making any decision about campaign structure, audience targeting, or creative strategy. Andromeda is the first-stage system that determines which ads are even *candidates* for a given auction — if your ad never makes it past Andromeda, nothing else matters.

**How Andromeda works:**

Andromeda is Meta's retrieval engine. Before any ad is ranked or scored, Andromeda decides which ads from the entire pool of active campaigns are relevant enough to enter the auction for a given user. It replaced Meta's previous retrieval system starting in late 2024 with global rollout completed October 2025.

**Key capabilities:**

| Dimension | Previous System | Andromeda |
|---|---|---|
| **Matching approach** | Audience-first: find users matching targeting criteria, then serve ads | Creative-first: analyze ad content, then match to users whose behavior patterns align |
| **Speed** | Baseline | 100x faster matching per auction |
| **Ad variants evaluated** | Hundreds per auction | 10,000x more variants evaluated — tens of thousands of ads considered per impression |
| **Targeting signal** | Audience parameters (interests, demographics, lookalikes) | Creative content is the primary signal — visual elements, copy themes, audio patterns, and format type determine audience match |
| **Diversity handling** | Limited — similar ads competed against each other | Rewards creative diversity — genuinely different ads reach genuinely different micro-audiences |

**What this means for advertisers:**

- **Creative diversity is now the primary targeting mechanism.** One broad campaign with 20 genuinely different creatives effectively targets 20 different micro-audiences — without you defining any of them.
- **Hyper-segmented audience targeting is counterproductive.** Narrowing your audience with layered interests restricts Andromeda's ability to find optimal matches. Broad targeting with diverse creative consistently outperforms narrow targeting with homogeneous creative.
- **Minor creative variations waste slots.** Same video with different thumbnails, or same copy with one word changed — Andromeda treats these as near-duplicates and they compete with each other instead of reaching new audiences.
- **More campaigns = worse performance.** Campaign fragmentation splits your creative pool, reducing the number of variants Andromeda can evaluate per auction. Consolidation gives Andromeda maximum creative surface area.

---

### Framework: GEM (Generalized Engagement Model)

**When to use:** When designing creative strategy, evaluating ad performance metrics, and understanding why certain content formats outperform others. GEM determines how ads are *ranked* after Andromeda retrieves them.

**What GEM is:**

GEM is Meta's multimodal foundation model that replaced placement-specific ranking models. Previously, Meta ran separate ranking models for Facebook Feed, Instagram Feed, Reels, Stories, and each other placement. GEM is a single unified model that ranks ads across all surfaces.

**Key capabilities:**

- **4x more efficient** at driving performance per unit of compute compared to previous ranking models
- **Sequence-learning:** GEM doesn't predict single actions (will this user click?). It predicts behavior chains — will this user watch 5 seconds, then visit the profile, then click the link, then purchase tomorrow? This chain prediction is fundamentally more accurate for conversion optimization.
- **Multimodal understanding:** GEM processes visual, textual, and audio signals together. It understands what an ad is about — not just metadata tags, but the actual content of images, the tone of copy, the energy of video audio.
- **Engagement-weighted ranking:** GEM weights meaningful engagement signals over surface-level metrics.

**GEM's engagement hierarchy (highest to lowest signal value):**

| Signal | Weight | Why It Matters |
|---|---|---|
| Saves | Highest | Indicates genuine intent — user wants to return to this content |
| Shares | Very High | Social endorsement — user vouches for this to their network |
| Comments (substantive) | High | Active engagement — user took time to respond |
| Extended watch time | High | Attention investment — especially on Reels/video |
| Profile visits from ad | Medium-High | Curiosity signal — user wants to know more about the brand |
| Link clicks | Medium | Intent signal — but clicks alone are cheap; GEM wants downstream behavior |
| Likes/reactions | Low | Passive engagement — low cognitive investment |

**Performance benchmarks:**
- 5% more conversions on Instagram (compared to previous ranking)
- 3% more conversions on Facebook Feed
- These gains compound with better creative — high-engagement creative benefits disproportionately from GEM's ranking

**Implications for creative strategy:**
- Design for saves and shares, not just clicks. Content that people bookmark or forward to friends will be ranked higher.
- Longer-form content that holds attention is rewarded. GEM tracks watch time curves, not just completion rates.
- Authentic, substantive creative outperforms polished-but-generic creative. GEM's engagement signals favor content that provokes real responses.

---

### Framework: Lattice Prediction System

**When to use:** When interpreting campaign performance, understanding cross-placement results, and making decisions about creative format and length. Lattice is the final prediction layer that determines expected outcomes.

**What Lattice is:**

Lattice is Meta's prediction system with trillions of parameters. It replaced siloed per-objective models (one model for purchase prediction, another for lead prediction, another for app install prediction) with a unified cross-surface prediction engine.

**Key capabilities:**

| Capability | What It Does | Advertiser Impact |
|---|---|---|
| **Unified cross-objective prediction** | Single model predicts all conversion types | Learnings from purchase campaigns improve lead campaign delivery and vice versa |
| **Cross-surface learning** | Instagram behavior informs Facebook delivery | A user's Reels engagement predicts their Facebook Feed purchase likelihood |
| **Per-viewer personalization** | Adjusts ad experience for each individual viewer | Same campaign may show a 15-second cut to one user and a 60-second version to another |
| **Content-length optimization** | Predicts optimal content duration per user | Short-form viewers get short cuts; long-form viewers get extended versions |
| **Format selection** | Predicts best format per user per moment | Same product may appear as carousel to one user and single image to another |

**What Lattice means for campaign management:**

- **Stop optimizing for placements.** Lattice already knows which placement works best for each user. Manual placement selection overrides a system that has trillions of data points.
- **Supply multiple creative lengths.** If you only provide one video length, Lattice cannot personalize. Provide 15s, 30s, and 60s cuts of the same concept.
- **Trust cross-surface attribution.** A user who watches your Reel on Instagram and buys through Facebook Feed two days later — Lattice predicted and enabled that journey. Placement-level ROAS reporting misses these cross-surface paths.

---

### Framework: The "Goal-Only" Trajectory

**When to use:** For strategic planning and account migration decisions. Understanding Meta's product roadmap prevents building structures that will be deprecated.

**Meta's stated vision (late 2026):** Advertisers set business goals, provide creative assets and first-party data, and AI handles everything else — targeting, placement, bidding, budget allocation, format selection, and delivery optimization.

**Deprecation timeline:**

| Date | Change | Impact |
|---|---|---|
| **October 2025** | Legacy API creation of manual campaigns blocked | All new API-created campaigns are Advantage+ by default |
| **December 2025** | Detailed targeting exclusions removed | Cannot exclude interest-based audiences |
| **Q1 2026** | Interest targeting relegated to "audience suggestions" (soft signal only) | Interest inputs become hints, not constraints |
| **May 2026** | Manual campaign creation fully migrated to Advantage+ in Ads Manager UI | No new manual campaigns possible anywhere |
| **Late 2026 (projected)** | Goal-only interface: objective + budget + creative + data | Manual bid overrides, audience restrictions, placement controls removed |

**What you still control (and will continue to):**

- Creative inputs (images, video, copy, landing pages)
- Conversion goals (which outcome to optimize for)
- Budget (how much to spend, campaign-level)
- First-party data (customer lists, CAPI signals, CRM integration)
- Brand safety settings (block lists, content exclusions)
- Geographic constraints (country/region-level)

**What is being removed:**

- Manual audience targeting (interests, behaviors, demographics beyond age/gender/geo)
- Placement selection
- Bid micro-management (cost caps, bid caps becoming "suggestions")
- Campaign-level frequency controls
- Ad set-level budget isolation

---

### Framework: AI-Era Account Structure (The 2-Campaign Model)

**When to use:** When restructuring an existing account or building a new one from scratch. This is the recommended default structure for accounts spending $1K-$100K+/month in the AI-first era.

**The structure:**

```
CAMPAIGN 1: CREATIVE TESTING
├── Type: Manual or Advantage+ (depending on data maturity)
├── Budget: ABO — equal spend per ad set
├── Targeting: Broad (age + geo only)
├── Ad sets: 2-4, each containing 2-4 new creative variants
├── Purpose: Identify winning creative concepts with fair budget distribution
├── Duration: 3-7 days per test cycle
├── Success criteria: CPA at or below 1.5x target, or ROAS at or above 0.7x target
└── Action: Winners graduate to Campaign 2

CAMPAIGN 2: ADVANTAGE+ SCALE
├── Type: Advantage+ Sales Campaign (or Advantage+ Leads)
├── Budget: Campaign-level (CBO equivalent) — 70-80% of total ad spend
├── Targeting: Fully algorithmic (Andromeda + Lattice handle everything)
├── Creatives: 20-50+ proven winners loaded simultaneously
├── Existing customer cap: Set to 10-20% depending on business model
├── Purpose: Scale proven creative with maximum algorithmic flexibility
└── Action: Continuously feed new winners from Campaign 1
```

**Why only 2 campaigns:**

- **Andromeda evaluates more variants from consolidated pools.** Splitting creative across 8 campaigns means each campaign has fewer variants for Andromeda to work with.
- **Lattice learns faster with larger data pools.** One campaign with 50 conversions/week learns faster than 5 campaigns with 10 each.
- **No separate retargeting campaign needed.** Advantage+ automatically allocates budget to retarget engaged users. The existing customer cap controls how much budget goes to retention vs acquisition.
- **Fewer campaigns = less management overhead.** Two campaigns to monitor instead of eight means more time for creative strategy and less time for campaign administration.

**When to add a third campaign:**
- Separate product lines with completely different audiences and landing pages
- Separate geographic markets with different languages or offers
- Brand awareness objective (separate from performance campaigns)
- App install campaigns (different objective and optimization)

---

### Framework: What You Control vs What AI Controls — Decision Matrix

**When to use:** Quick reference when building campaigns or evaluating whether a manual override is worth the trade-off.

| Lever | Who Controls | Notes |
|---|---|---|
| **Business objective** | Advertiser | You choose: awareness, traffic, leads, sales, app, engagement |
| **Total budget** | Advertiser | Campaign-level spend limit |
| **Budget allocation across ad sets** | Shared | You set initial distribution; AI reallocates up to 20% (ABO) or fully (CBO) |
| **Creative assets** | Advertiser | Images, video, copy, landing pages — your primary input |
| **Creative selection per user** | AI | Which ad from your pool gets shown to which user |
| **Audience targeting** | AI (with optional hints) | Broad is default; interest inputs are "suggestions" only |
| **Placement selection** | AI | Advantage+ Placements is default and increasingly mandatory |
| **Bid amount** | Shared | You set cost cap/bid cap as guardrail; AI optimizes within it |
| **Delivery timing** | AI | When during the day your ads are shown |
| **Frequency** | AI | How often the same user sees your ad |
| **Ad format per user** | AI (Lattice) | Carousel vs single image vs video — per-viewer decision |
| **Content length per user** | AI (Lattice) | Which cut of your video each viewer sees |
| **Retargeting** | AI | Advantage+ auto-retargets; no separate campaign needed |
| **First-party data signals** | Advertiser | Customer lists, CAPI events, CRM data — you supply it |
| **Conversion event** | Advertiser | Which event to optimize for (purchase, lead, add-to-cart) |
| **Geographic constraints** | Advertiser | Country/region targeting remains manual |
| **Age/gender constraints** | Advertiser | Basic demographic limits remain available |
| **Brand safety** | Advertiser | Block lists, content type exclusions, inventory filters |

---

## Key Principles

- **The algorithm is not your enemy — it is your multiplier.** Andromeda, GEM, and Lattice have more data about user behavior than any media buyer. Working with them means supplying great creative and clean data, then letting them optimize delivery.
- **Creative is the new targeting.** With Andromeda's creative-first matching, the diversity and quality of your creative assets is the single largest lever for performance. Audience settings are secondary.
- **Consolidation is not laziness — it is strategy.** Fewer campaigns with more creative variants outperform many campaigns with few variants. This is an architectural fact of how Andromeda retrieves ads.
- **Manual controls are being removed for a reason.** Meta's internal testing consistently shows that removing manual overrides improves aggregate performance. Fighting this trend costs you money.
- **First-party data is your remaining competitive moat.** As manual targeting disappears, the quality of your CAPI integration, customer lists, and CRM data becomes the primary differentiator between you and competitors.
- **The 2-campaign model is a starting point, not a religion.** Some businesses legitimately need 3-4 campaigns. But if you have more than 5 active campaigns and you are not an enterprise spender, you are almost certainly fragmenting your data.
- **Retargeting as a separate campaign is obsolete.** Advantage+ automatically retargets engaged users. A dedicated retargeting campaign competes with your own scale campaign in the auction, driving up your costs.
- **Expect attribution gaps and plan for them.** As AI controls more delivery decisions across surfaces and formats, single-touch attribution becomes less meaningful. Adopt incrementality testing and blended ROAS as primary measurement frameworks.
- **The transition is happening whether you participate or not.** Manual campaigns are being deprecated on a published timeline. Migrate proactively and benefit from early learning, or be forced to migrate reactively when the tools disappear.
- **Supply the raw materials, let the AI build.** Your job is creative production, data quality, and strategic goal-setting. The AI's job is delivery optimization. Stay in your lane and let the AI stay in its lane.

---

## Decision Tools

### "Is My Account AI-Optimized?" Diagnostic Checklist

- [ ] Running 4 or fewer active campaigns (excluding brand awareness)
- [ ] At least one Advantage+ Sales or Advantage+ Leads campaign active
- [ ] Primary scale campaign has 20+ creative assets loaded
- [ ] No manual placement selection — using Advantage+ Placements everywhere
- [ ] No narrow interest stacking — targeting is broad or using audience suggestions only
- [ ] Conversions API (CAPI) implemented and deduplicating with Pixel
- [ ] Customer list uploaded and refreshed within the last 30 days
- [ ] Existing customer cap set in Advantage+ campaigns
- [ ] No separate retargeting campaign (Advantage+ handles it)
- [ ] Creative testing campaign running with 2-4 new concepts per week

### Migration Checklist: Manual to AI-First Account Structure

1. **Audit current structure:** Count campaigns, ad sets, total creative assets, and overlap
2. **Identify top-performing creative:** Last 30 days, by CPA and ROAS — these are your Campaign 2 seed
3. **Set up Campaign 2 (Advantage+ Scale):** Load top 20+ creatives, set existing customer cap, set campaign budget to 70% of total spend
4. **Set up Campaign 1 (Creative Testing):** ABO, broad targeting, 2-4 ad sets with 2-4 new concepts each, 30% of total spend
5. **Pause old campaigns gradually:** Reduce budget on old campaigns by 25% per day over 4 days while monitoring Campaign 2 ramp
6. **Implement CAPI** if not already in place — this is non-negotiable for AI-era performance
7. **Upload customer lists:** Purchasers, leads, email subscribers — refresh monthly
8. **Remove manual placement selections** from any remaining manual campaigns
9. **Monitor for 14 days** before evaluating — allow learning phase to complete
10. **Document baseline metrics** (CPA, ROAS, CPM) from the old structure for comparison

### Warning Signs Your Account Is Fighting the Algorithm

| Warning Sign | What It Means | Fix |
|---|---|---|
| 6+ active campaigns for a single product/offer | Data fragmentation — each campaign has insufficient conversion volume | Consolidate to 2-campaign model |
| Manual placements selected | Restricting Lattice's cross-surface optimization | Switch to Advantage+ Placements |
| Narrow interest stacking (3+ layers) | Constraining Andromeda's creative-first matching | Remove interest constraints; go broad |
| Separate retargeting campaign alongside Advantage+ | Self-competition in the auction | Remove retargeting campaign; use existing customer cap in Advantage+ |
| Fewer than 10 creative assets in scale campaign | Insufficient creative diversity for Andromeda | Increase to 20+ genuinely different assets |
| Bid caps set below estimated CPA | Throttling delivery — learning phase cannot complete | Remove bid caps or set them 20%+ above target CPA |
| Daily budget changes greater than 20% | Resetting the learning phase repeatedly | Make budget changes in increments of 10-15% maximum |
| No CAPI implementation | Missing 30-50% of conversion signals on iOS users | Implement CAPI immediately — highest priority technical task |

---

*Chunk 11 of 20 — Facebook Advertising Technical Framework*
