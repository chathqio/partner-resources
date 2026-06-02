# Chunk 20: Account Audit, Troubleshooting & Operations
## Source: Andrew Foxwell (Foxwell Digital, Foxwell Founders), agency SOPs, Meta Business Help Center (2026)

---

## Core Concept

Even the best-structured campaigns degrade over time. Creative fatigues, audiences saturate, tracking breaks, and platform changes shift the playing field. Account audits identify waste, diagnose performance issues, and surface optimization opportunities before small problems compound into major budget drains.

This chunk provides the complete operational toolkit for maintaining and scaling Meta ad accounts: a structured audit methodology, troubleshooting protocols for the most common performance issues, reporting infrastructure, and agency-level workflow SOPs. Andrew Foxwell's AAA Audit framework — refined through thousands of account reviews across the Foxwell Founders community — provides the diagnostic backbone. The troubleshooting section covers the 15 most common failure modes with specific fixes. The operations section covers everything from weekly checklists to client onboarding.

Operations is the unsexy discipline that separates profitable advertisers from those who "tried Facebook ads and they didn't work." The difference is rarely strategy — it's execution consistency.

---

## Frameworks

### Framework: Foxwell AAA Audit Methodology

**When to use:** Monthly (at minimum), or whenever performance degrades significantly. Andrew Foxwell's Account-Campaign-AdSet-Ad audit framework provides a systematic, top-down diagnostic.

**Account-Level Audit:**
- **Business Portfolio setup:** Is the Business Portfolio (formerly Business Manager) properly structured? Correct ownership of Pages, Pixels, ad accounts? Proper partner access levels?
- **Pixel / CAPI health:** Is the Meta Pixel firing on all key pages? Is Conversions API (CAPI) sending server-side events? Check Event Manager for deduplication status and Event Match Quality (EMQ) scores — target 6.0+ on all key events.
- **Audience library:** Are custom audiences up to date? Any audiences based on expired data (180+ day windows)? Are lookalike audiences refreshed from current seed data?
- **Catalog feed status:** For e-commerce — are product feeds syncing? Check for rejected products, missing fields (price, availability, image), and feed freshness.
- **Policy compliance:** Any active policy violations, restricted ad account warnings, or disabled ad flags? Check Account Quality dashboard.

**Campaign-Level Audit:**
- **Objective alignment:** Does each campaign's objective match its actual goal? (Common mistake: using Traffic objective for conversion goals)
- **Budget strategy:** Is budget allocated proportionally across funnel stages? Any campaigns spending disproportionately with poor results?
- **Structure:** Is the account over-fragmented? Count total active campaigns, ad sets, and ads. More than 5-8 active campaigns is a red flag for most accounts.
- **Naming conventions:** Are all campaigns, ad sets, and ads following a consistent naming convention? Can you filter and report by funnel stage, audience type, or creative concept?

**Ad Set-Level Audit:**
- **Targeting overlap:** Run the Audience Overlap tool on all active ad sets. Overlap above 30% between ad sets in different campaigns means you're bidding against yourself.
- **Learning phase status:** How many ad sets are stuck in "Learning Limited"? This means they're not getting 50 optimization events per week — either increase budget, broaden audience, or consolidate.
- **Frequency:** Check frequency on prospecting ad sets. Above 3.0 on cold audiences indicates saturation. Above 8-10 on retargeting is acceptable but monitor for fatigue.
- **Budget sufficiency:** Calculate: target CPA x 50 = minimum weekly budget per ad set to exit learning. If ad set budget is below this, consolidate or increase.

**Ad-Level Audit:**
- **Creative diversity:** Are you running at least 3-5 distinct creative concepts per ad set? (Not just variations — truly different angles, formats, or hooks)
- **Fatigue indicators:** CTR declining week-over-week while frequency rises = creative fatigue. Flag ads with >20% CTR decline over 14 days.
- **Format mix:** Are you testing across formats (video, image, carousel, collection)? Single-format ad sets leave performance on the table.
- **Advantage+ Creative settings:** Review whether Advantage+ enhancements (text variations, visual optimizations) are enabled. Test on vs off — automated enhancements don't always improve performance.

**Scoring system:**

| Dimension | Green | Yellow | Red |
|---|---|---|---|
| Pixel/CAPI | EMQ 6.0+, CAPI active, dedup working | EMQ 4.0-5.9 or CAPI not set up | EMQ <4.0 or Pixel errors |
| Structure | 2-5 campaigns, clear funnel mapping | 6-8 campaigns, some overlap | 9+ campaigns, fragmented, no clear structure |
| Learning Phase | 80%+ ad sets active (not Learning Limited) | 50-79% active | <50% active (most in Learning Limited) |
| Creative | 3+ concepts per ad set, <14d avg age | 2 concepts, some fatigue signals | 1 concept or severe fatigue across ad sets |
| Targeting | No overlap >30%, exclusions in place | Some overlap, missing exclusions | Heavy overlap, no exclusions, bidding against yourself |

---

### Framework: Weekly Audit Checklist

**When to use:** Every Monday morning (or your designated review day). 30-minute review to catch issues before they compound.

- [ ] Check all campaigns for learning phase status — flag any ad sets in "Learning Limited" for 7+ days
- [ ] Review frequency on all prospecting ad sets — flag any above 3.0 for creative refresh
- [ ] Check CPA/ROAS trends vs targets (7-day rolling average vs 30-day average) — flag any campaign >20% off target
- [ ] Review Creative Fatigue Indicators — CTR declining + frequency rising = fatigue. Queue replacement creative
- [ ] Check budget pacing — are campaigns on track to spend full monthly budget? Over-spending or under-spending?
- [ ] Review any policy violations or ad rejections in Account Quality dashboard
- [ ] Confirm automated rules are executing correctly (check rule activity log)
- [ ] Quick scan of auction insights — any new competitors entering your auction?
- [ ] Check for any Meta platform updates or outages that may have affected delivery

**Time budget:** 30 minutes maximum. If you find issues, log them for deeper investigation — do not try to fix everything in the weekly review.

---

### Framework: Monthly Audit Checklist

**When to use:** First week of each month. Deep 2-hour review that covers strategic and structural health.

- [ ] Full Foxwell AAA audit (account, campaign, ad set, ad levels)
- [ ] Creative performance analysis — identify top 5 winners and bottom 5 losers. Document why each won or lost (hook, angle, format, audience match)
- [ ] Audience overlap analysis across all active campaigns — consolidate or exclude as needed
- [ ] Pixel/CAPI health check — verify EMQ scores, event firing accuracy, deduplication status
- [ ] Catalog feed diagnostics (e-commerce) — check rejected products, missing fields, feed freshness
- [ ] Historical data export — Meta retains granular data for 37 months but detailed breakdowns for shorter periods. Export key metrics monthly
- [ ] Competitor creative analysis — review top competitors in Meta Ad Library. Note new angles, formats, or offers
- [ ] Budget reallocation — shift budget based on performance trends (increase spend on winning campaigns, reduce or pause underperformers)
- [ ] Audience refresh — update custom audiences, create new lookalikes from recent high-value customers
- [ ] Test roadmap — plan next month's creative tests, audience tests, and structural experiments

---

### Framework: Common Performance Issues & Fixes

**When to use:** When something goes wrong. Diagnose the symptom, identify the likely cause, apply the fix.

| Symptom | Likely Cause | Fix |
|---|---|---|
| **CPA suddenly spiked (2x+ overnight)** | Creative fatigue, audience saturation, competitor surge, seasonal CPM increase, or tracking disruption | Check frequency first (fatigue?). Check CPM trends (market-level?). Verify Pixel/CAPI still firing. Introduce new creative. If market-level CPM spike, reduce spend temporarily. |
| **Campaign stuck in Learning Limited** | Insufficient budget, too many ad sets fragmenting data, narrow audience, low conversion volume event selected | Consolidate ad sets (fewer, larger). Increase budget to 50x target CPA per week. Broaden audience. Consider optimizing for a higher-volume event (e.g., Add to Cart instead of Purchase). |
| **High CTR but low conversions** | Landing page problem, message mismatch between ad and page, slow load speed, tracking error, or wrong audience (clickers, not buyers) | Audit landing page for message match. Check mobile load speed (target <3s). Verify conversion events are firing. Switch from Link Click to Landing Page View optimization. |
| **Low delivery / impressions** | Bid or cost cap too restrictive, audience too small (<100K), policy issue suppressing delivery, low ad quality ranking | Remove or raise bid caps. Broaden audience. Check ad quality diagnostics. Review for policy violations. Ensure budget meets minimum thresholds. |
| **Frequency too high (>3.0 prospecting)** | Audience saturation — same people seeing ads repeatedly | Expand audience size. Introduce new creative (the audience isn't fatigued, they're fatigued with your creative). Increase TOFU spend to build larger retargeting pools. |
| **ROAS declining gradually over weeks** | Creative fatigue, audience exhaustion, competitive pressure, or seasonality | Refresh creative (new hooks, angles, formats). Test new audiences. Audit post-click experience. Compare against seasonal benchmarks. |
| **Ads keep getting rejected** | Policy violation pattern — common triggers: before/after imagery, personal attributes, health claims, misleading buttons | Review Meta Advertising Standards. Remove personal attribute targeting language ("Are you overweight?"). Use compliant before/after formats. Appeal if false positive. |
| **Pixel events not firing** | Code deployment broke Pixel, site redesign removed Pixel code, tag manager misconfiguration, consent management blocking | Check Events Manager for real-time event activity. Use Meta Pixel Helper browser extension. Verify tag manager triggers. Check consent banner isn't blocking Pixel load. |
| **High CPM (>$30 for cold traffic)** | Competitive auction period (Q4, holidays), low ad quality, narrow audience, or placement restrictions | Broaden placements (enable Advantage+ Placements). Improve ad quality scores. Test different audiences. If seasonal, accept higher CPMs and focus on efficiency. |
| **Ad set spending unevenly in CBO** | Algorithm concentrating budget on perceived winner — may be correct or premature | If early (<72hrs), set minimum spend floors per ad set. If >7 days and concentration is on best performer, this is working as intended. If concentrating on a loser, pause it. |
| **Advantage+ Sales not performing** | Insufficient creative diversity, weak Pixel data (<50 purchases/week), or existing customer cap set incorrectly | Add more creative (target 10+ assets). Build Pixel data with manual campaigns first. Adjust existing customer cap (try 0% to force prospecting). |
| **Retargeting audience too small** | Insufficient TOFU investment, short audience windows, or tracking gaps | Increase TOFU spend to build larger engagement and visitor pools. Extend audience windows (7d → 30d → 90d). Verify Pixel capturing all site visitors. |
| **Conversion attribution seems off** | iOS privacy changes (ATT), ad blockers, cross-device attribution gaps, view-through vs click-through confusion | Enable CAPI for server-side tracking. Review attribution settings (7-day click, 1-day view is default). Cross-reference with GA4 or backend data. Accept some gap as the new normal. |

---

### Framework: Delivery Insights Tool

**When to use:** When diagnosing why a campaign isn't delivering as expected or why CPMs have changed significantly.

**How to access:** Ads Manager → select campaign or ad set → "Inspect" button → Delivery Insights tab

**Key metrics and interpretation:**

| Metric | What It Shows | Action Threshold |
|---|---|---|
| **Auction Overlap Rate** | % of auctions where your ad sets compete against each other | >30% — consolidate ad sets or add exclusions |
| **Audience Reached %** | % of total audience that has seen your ad | >70% on prospecting — audience nearing saturation |
| **First Time Impression Ratio** | % of impressions going to people seeing your ad for the first time | <50% on prospecting — need fresh audience or creative |
| **Auction Competition** | Trend of competitor activity in your auction | Rising competition → expect higher CPMs. Consider differentiation or off-peak scheduling |

**When to use Delivery Insights vs other diagnostics:**
- Performance drop + stable creative = check Delivery Insights (audience/competition issue)
- Performance drop + aging creative = check ad-level metrics (creative fatigue issue)
- No delivery at all = check policy compliance + bid/budget settings first

---

### Framework: Reporting Dashboard Setup

**When to use:** At account setup — build reporting infrastructure before launching campaigns, not after.

**Recommended stack:**
- **Looker Studio (Google Data Studio)** — free, flexible, shareable dashboards
- **Supermetrics** or **Funnel.io** — automated data connectors from Meta Ads to Looker Studio
- **Meta Ads Manager exports** — backup for manual analysis and data archival

**Key dashboard views:**

| Dashboard View | Audience | Refresh Cadence | Key Metrics |
|---|---|---|---|
| **Executive summary** | C-suite, client stakeholders | Weekly | Total spend, ROAS, CPA, revenue, trend arrows |
| **Campaign performance** | Media buyers, account managers | Daily | Campaign-level CPA, ROAS, spend, conversions by funnel stage |
| **Creative analysis** | Creative team, media buyers | Weekly | Ad-level CTR, hook rate, CPA, ROAS, creative fatigue indicators |
| **Audience insights** | Strategists, media buyers | Monthly | Audience overlap, reach vs frequency, audience saturation metrics |
| **Funnel analysis** | Full team | Monthly | Stage-by-stage conversion rates, cost per stage, drop-off points |

**Automated reporting cadence:**
- **Daily:** Automated Slack/email alert if any campaign exceeds CPA target by >30% or spend pacing is >120% of daily target
- **Weekly:** Performance summary email to stakeholders — spend, results, ROAS, top/bottom performers
- **Monthly:** Deep-dive report with strategic recommendations — sent 3-5 business days into new month

---

### Framework: Agency Workflows & SOPs

**When to use:** For agencies managing multiple client accounts or in-house teams needing operational structure.

**Client onboarding SOP:**
1. Access setup — request Business Portfolio partner access (never admin ownership)
2. Pixel/CAPI audit — verify tracking health before launching any campaigns
3. Goal alignment workshop — define KPIs, CPA/ROAS targets, budget, and timeline
4. Competitor and audience research — Meta Ad Library scan, audience sizing
5. Creative brief — align on brand guidelines, approved messaging, compliance requirements
6. Reporting setup — build dashboard, set automated alerts, confirm reporting cadence
7. Campaign architecture plan — document funnel structure, campaign naming, budget allocation
8. Launch checklist — final review before going live

**Campaign management SOP (ongoing):**
- **Daily (10 min):** Check for policy violations, delivery anomalies, budget pacing alerts
- **Weekly (30 min):** Full weekly audit checklist (see above). Document findings.
- **Bi-weekly (1 hr):** Creative refresh assessment. Brief new creative if needed.
- **Monthly (2 hrs):** Full monthly audit. Strategy adjustment. Client performance review.
- **Quarterly (half day):** Strategic review — funnel performance, audience strategy, creative direction, budget reallocation, competitive landscape

**Creative request workflow:**
```
Media buyer identifies need → Creative brief (format, audience, angle, reference)
→ Creative team produces assets (3-5 business days)
→ Internal review + compliance check
→ Client approval (if required)
→ Upload to Ads Manager with proper naming
→ Launch in testing campaign (ABO)
```

**Escalation protocol:**
- CPA >50% above target for 3+ consecutive days → alert account manager
- CPA >100% above target for 24+ hours → pause campaign, investigate immediately
- Ad account restricted or disabled → escalate to agency owner + Meta rep within 1 hour
- Policy violation on client-approved creative → notify client immediately, pause ad, request compliant revision

---

### Framework: Creative Hub & Ad Library Tools

**When to use:** For creative research, competitive analysis, and ad mockup creation.

**Meta Ad Library (ads.facebook.com/ads/library):**
- **Competitor research:** Search by advertiser name to see all active ads. Note creative formats, copy angles, offers, and landing page destinations.
- **Industry research:** Search by keyword to see how the market is advertising for specific products or services.
- **Creative swipe file:** Screenshot top-performing competitor ads (identified by longest run time — ads running 60+ days are likely profitable). Organize by format, hook type, and offer.
- **Transparency data:** View spend ranges (for political/social issue ads), audience demographics reached, and active vs inactive status.

**How to build a competitive swipe file:**
1. Identify 10-15 direct competitors and aspirational brands in your space
2. Search each in Ad Library — filter by country, platform, and active status
3. Screenshot ads running longest (longevity = profitability signal)
4. Categorize by: format (video/image/carousel), hook type (question/stat/story), offer type (discount/lead magnet/direct sale)
5. Identify patterns — what formats dominate? What hooks recur? What offers appear most?
6. Use patterns to inform your creative testing roadmap — don't copy, but learn from what the market rewards

**Creative Hub (business.facebook.com/creativeHub):**
- Mock up ads in all formats without spending budget
- Preview how ads render across placements (Feed, Stories, Reels, Right Column)
- Share mockups with team or clients for approval before building in Ads Manager
- Test creative concepts internally before committing production resources

---

## Key Principles

- **Audit consistently, not reactively.** Weekly and monthly audits catch problems early when they're cheap to fix. Waiting until performance craters means the damage is already done.
- **The Foxwell AAA methodology works top-down for a reason.** Account-level issues (broken Pixel, policy violations) invalidate everything below them. Always start at the account level.
- **Learning Limited is a structural problem, not a performance problem.** It means the algorithm doesn't have enough data to optimize. The fix is always consolidation or budget increase — never more fragmentation.
- **Creative fatigue is the #1 performance killer.** Most "my ads stopped working" diagnoses end at creative fatigue. Build a creative pipeline that produces new assets every 2-3 weeks.
- **Frequency tells different stories at different funnel stages.** Frequency of 3.0 on prospecting is a problem. Frequency of 8.0 on retargeting is normal. Context determines whether frequency is a signal or noise.
- **Reporting infrastructure should exist before you launch.** If you can't measure it, you can't optimize it. Build dashboards and alerts during account setup, not after the first month of spend.
- **The best troubleshooting tool is a comparison.** Compare this week to last week. This month to last month. This campaign to that campaign. Absolute numbers are meaningless without context.
- **Document everything.** What you tested, what you changed, why you changed it, what happened. Without documentation, you repeat mistakes and can't replicate wins.
- **Data retention is your responsibility.** Export key metrics monthly. Meta's reporting interface is not an archive — granular breakdowns have limited retention windows.
- **Operations is a competitive advantage.** Two advertisers with identical strategy, creative, and budget will produce vastly different results based on operational discipline. The one who audits weekly, refreshes creative proactively, and fixes issues fast will outperform the one who sets and forgets.

---

## Decision Tools

### "What's Wrong With My Campaign?" Diagnostic Flowchart

```
Campaign underperforming. Start here:

1. Is the campaign delivering impressions?
   ├── NO → Check: policy violations? Budget too low? Audience too small? Bid cap too restrictive?
   └── YES ↓

2. Is the CPM reasonable (within historical range)?
   ├── NO (CPM spiked) → Check: auction competition, seasonal trends, audience saturation
   └── YES ↓

3. Is the CTR reasonable (>1% for Feed, >0.5% for broad)?
   ├── NO → Creative problem. Check: hook, visual, relevance to audience. Test new creative.
   └── YES ↓

4. Are people landing on the page (Landing Page View rate >70% of clicks)?
   ├── NO → Page speed problem. Check mobile load time. Target <3 seconds.
   └── YES ↓

5. Are people converting on the page?
   ├── NO → Landing page problem. Check: message match, CTA clarity, trust signals, form length.
   └── YES but CPA too high ↓

6. Is the conversion rate reasonable but volume too low?
   └── Audience or budget problem. Broaden targeting. Increase budget. Consolidate ad sets.
```

### Account Health Scorecard Template

| Dimension | Status | Score | Notes |
|---|---|---|---|
| **Pixel / CAPI Health** | [ ] Green [ ] Yellow [ ] Red | /10 | EMQ: ___ CAPI: Y/N Dedup: Y/N |
| **Account Structure** | [ ] Green [ ] Yellow [ ] Red | /10 | Active campaigns: ___ Ad sets: ___ |
| **Learning Phase** | [ ] Green [ ] Yellow [ ] Red | /10 | ___% of ad sets active (not Limited) |
| **Creative Health** | [ ] Green [ ] Yellow [ ] Red | /10 | Avg creative age: ___d Concepts: ___ |
| **Audience Health** | [ ] Green [ ] Yellow [ ] Red | /10 | Overlap: ___% Saturation: ___% |
| **Budget Efficiency** | [ ] Green [ ] Yellow [ ] Red | /10 | CPA vs target: ___% ROAS: ___ |
| **Policy Compliance** | [ ] Green [ ] Yellow [ ] Red | /10 | Active violations: ___ |
| **TOTAL** | | /70 | >55 = healthy, 40-55 = needs attention, <40 = urgent |

### Weekly Operations Checklist (Quick Reference)

```
Every Monday:
□ Learning phase status check (all ad sets)
□ Frequency review (flag >3.0 prospecting)
□ CPA/ROAS vs targets (7d rolling)
□ Creative fatigue scan (CTR trend + frequency)
□ Budget pacing check
□ Policy violation review
□ Automated rule execution log
□ Document findings + action items
Time: 30 minutes
```

### Monthly Audit Template (Quick Reference)

```
First week of month:
□ Full Foxwell AAA audit (account → campaign → ad set → ad)
□ Top 5 / bottom 5 creative analysis with rationale
□ Audience overlap analysis
□ Pixel/CAPI health verification
□ Catalog feed diagnostics (if e-commerce)
□ Data export for archival
□ Competitor creative scan (Ad Library)
□ Budget reallocation based on trends
□ Audience refresh (new lookalikes, updated custom audiences)
□ Next month's test roadmap
Time: 2 hours
```

### Agency Onboarding Checklist

```
New client setup:
□ Business Portfolio partner access granted (not admin)
□ Pixel/CAPI audit completed — health documented
□ KPIs, CPA/ROAS targets, and budget confirmed in writing
□ Competitor analysis completed (Ad Library + market research)
□ Creative brief aligned with brand guidelines
□ Reporting dashboard built and shared with client
□ Campaign architecture plan documented and approved
□ Naming conventions documented and shared with team
□ Automated alerts configured (CPA, spend pacing)
□ Launch checklist reviewed — ready for first campaign
```

---

*Chunk 20 of 20 — Facebook Advertising Technical Framework*