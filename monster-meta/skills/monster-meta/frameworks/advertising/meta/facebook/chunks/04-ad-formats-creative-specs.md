# Chunk 4: Ad Formats & Creative Specs
## Source: Meta Ads Guide, Meta Business Help Center, creative best practices (2026)

---

## Core Concept

Meta offers six primary ad formats — Single Image, Video, Carousel, Collection, Instant Experience, and Flexible Ads — each suited to different objectives, funnel stages, and creative strategies. Every format must conform to placement-specific technical specifications (dimensions, aspect ratios, file types, character limits) that directly affect delivery, cost, and performance. Getting specs wrong does not just look bad — it reduces auction competitiveness because Meta penalizes poor ad quality.

Beyond format selection, Meta's Advantage+ Creative system uses AI to automatically enhance and adapt your creative assets across placements. Understanding when to enable or disable these enhancements — and which formats support which features — is critical for maintaining brand control while leveraging algorithmic optimization.

---

## Frameworks

### Framework: Creative Spec Quick-Reference Table

**When to use:** During ad creation to confirm your assets meet technical requirements for all target placements.

#### Single Image Specs

| Spec | Feed | Stories / Reels | Right Column | Search | Audience Network |
|---|---|---|---|---|---|
| **Recommended size** | 1080 x 1350 px | 1080 x 1920 px | 1080 x 1080 px | 1080 x 1080 px | 1080 x 1080 px |
| **Aspect ratio** | 4:5 (portrait) | 9:16 (full screen) | 1:1 (square) | 1:1 | Varies |
| **File types** | JPG, PNG | JPG, PNG | JPG, PNG | JPG, PNG | JPG, PNG |
| **Max file size** | 30 MB | 30 MB | 30 MB | 30 MB | 30 MB |
| **Primary text** | 125 chars visible (up to 2,200 allowed) | Not displayed | 125 chars | 125 chars | 125 chars |
| **Headline** | 40 chars recommended (up to 255) | N/A (overlay only) | 40 chars | 40 chars | 40 chars |
| **Description** | 25-30 chars recommended | N/A | 20 chars | 25 chars | 25 chars |

**Notes:** Feed images at 4:5 occupy more vertical screen space on mobile than 1:1, increasing visibility — **4:5 and 9:16 are now the algorithm-preferred aspect ratios** (deprioritize 1:1 square for Feed; reserve square for Right Column, Search, and Audience Network placements). Meta recommends uploading at the highest resolution available (1440 x 1800 ideal for Feed). The 20% text overlay rule was removed, but images with less text overlay still see better delivery and lower costs.

#### Video Specs

| Spec | Feed | Stories / Reels | In-Stream | Right Column |
|---|---|---|---|---|
| **Recommended size** | 1080 x 1350 px | 1080 x 1920 px | 1920 x 1080 px | 1080 x 1080 px |
| **Aspect ratio** | 4:5 (portrait) | 9:16 (full screen) | 16:9 (landscape) | 1:1 (square) |
| **Duration** | 1 sec – 241 min | 1–60 sec (Reels: up to 90 sec) | 5–15 sec recommended | 1 sec – 241 min |
| **File types** | MP4, MOV (H.264) | MP4, MOV | MP4, MOV | MP4, MOV |
| **Max file size** | 4 GB | 4 GB | 4 GB | 4 GB |
| **Audio** | AAC, 128+ kbps | AAC | AAC | AAC |
| **Captions** | Recommended (auto-generated available) | Burned-in recommended | Required | Optional |
| **Thumbnail** | Separate upload or auto-frame; same aspect ratio as video | 1080 x 1920 | Match video ratio | Match video ratio |

**Notes:** 9:16 vertical video on Stories/Reels drives 41% higher engagement than cropped formats. As of March 2026, Stories and Reels share a unified safe zone — keep critical content in the center 1080 x 1420 area (top ~250 px and bottom ~340 px are covered by UI elements across both placements). First 3 seconds determine whether users watch; lead with motion and a hook. **2026 change:** The engaged-view threshold dropped from 10 seconds to 5 seconds — a "video view" now counts after 5 seconds of engaged watching, making early-engagement metrics more generous but also meaning the hook window is even more critical.

#### Carousel Specs

| Spec | Requirement |
|---|---|
| **Number of cards** | 2–10 cards per carousel |
| **Image size per card** | 1080 x 1080 px (1:1 recommended) |
| **Video per card** | 1080 x 1080 px, up to 240 min, 4 GB max |
| **Aspect ratio** | 1:1 (all cards must match) |
| **File types** | JPG, PNG (images); MP4, MOV (video) |
| **Max image file size** | 30 MB per card |
| **Primary text** | 125 chars visible |
| **Headline per card** | 40 chars recommended |
| **Description per card** | 25 chars recommended |
| **Link** | Each card can link to a unique URL |
| **CTA** | One CTA button per card (can differ across cards) |

**Notes:** Carousel cards can mix images and video. Use sequential storytelling (problem → solution → proof → CTA) or showcase multiple products. Enable "Automatic card ordering" to let Meta show the best-performing card first, or disable it when story sequence matters.

#### Collection Ad Specs

| Spec | Requirement |
|---|---|
| **Cover media** | Image (1080 x 1080 or 1080 x 1350) or Video (up to 120 min) |
| **Product images below cover** | Auto-pulled from catalog (4 products displayed) |
| **Aspect ratio (cover)** | 1:1 or 4:5 |
| **Primary text** | 125 chars visible |
| **Headline** | 40 chars |
| **Instant Experience** | Required — opens full-screen when tapped |
| **Mobile only** | Collection ads display on mobile placements only |

**Notes:** Collection ads pair a cover image/video with a product grid pulled from your catalog. Tapping opens a full-screen Instant Experience. Best for e-commerce product discovery. Requires a connected product catalog.

#### Instant Experience Specs

| Spec | Requirement |
|---|---|
| **Templates** | Instant Storefront, Instant Customer Acquisition, Instant Lookbook, Instant Storytelling, Custom |
| **Components** | Images, videos, carousels, text blocks, buttons, product sets, forms |
| **Minimum components** | 5 media elements for custom templates |
| **Image specs** | 1080 px wide, full-width; up to 20 images |
| **Video specs** | Up to 2 min per video; auto-play on view |
| **Load speed** | 15x faster than mobile web (pre-cached) |
| **CTA buttons** | Customizable text and URL per button |
| **Required elements** | Back button (top-left), scroll/swipe indicator |

**Template selection guide:**

| Template | Best For | Key Feature |
|---|---|---|
| Instant Storefront | E-commerce product browsing | Grid layout, catalog integration, "Shop Now" flow |
| Instant Customer Acquisition | Lead gen / conversions | Mini landing page with single CTA, persuasion-focused |
| Instant Lookbook | Fashion, lifestyle, visual brands | Lifestyle imagery linked to product tags |
| Instant Storytelling | Brand awareness, launches | Immersive narrative with mixed media |
| Custom | Advanced / unique needs | Full control over layout and components |

#### Flexible Ads Specs (Replaced Dynamic Creative)

| Spec | Requirement |
|---|---|
| **Images** | Up to 10 images per ad |
| **Videos** | Up to 10 videos per ad |
| **Primary text** | Up to 5 text variations |
| **Headlines** | Up to 5 headline variations |
| **Descriptions** | Up to 5 description variations |
| **CTAs** | Multiple CTA options selectable |
| **How it works** | Meta mixes and matches creative elements, testing combinations automatically to find top performers |
| **Reporting** | Performance breakdown by individual asset available |

**Notes:** Flexible Ads replaced Dynamic Creative in 2024. The system tests combinations of your uploaded assets to find winning permutations. Best for rapid creative testing without manually building dozens of ad variations. Performance improvement of 25-40% is commonly reported vs. standard single-variant ads.

---

### Framework: Advantage+ Creative Enhancements

**When to use:** When deciding which AI-powered creative optimizations to enable or disable on your ads.

| Enhancement | What It Does | Applies To | Enable When | Disable When |
|---|---|---|---|---|
| **AI Background Generation** | Generates alternative backgrounds for product images | Single Image | Product-on-white images, catalog ads | Lifestyle photography, branded backgrounds |
| **Text Optimization** | Rearranges primary text, headline, and description for best performance | All text-based formats | Running multiple text variations, testing messaging | Precise message control is required |
| **Format Adaptation** | Automatically adjusts aspect ratio and layout per placement | Image, Video | Running across Feed + Stories + Reels simultaneously | Custom creative per placement already provided |
| **Music for Reels** | Adds background music from Meta's library to Reels placements | Video (Reels) | Short-form video without audio, product demos | Video has custom audio/voiceover |
| **Image Brightness/Contrast** | Adjusts image brightness and contrast for better visibility | Single Image | Standard product photography | Already color-graded, brand-specific aesthetics |
| **3D Motion** | Adds subtle parallax/motion effect to static images | Single Image | Static images in Stories/Reels placements | Already using video or motion graphics |
| **Text Overlay** | Adds headline/description as text overlay on creative | Image | Driving direct response, promotional offers | Clean brand aesthetic, awareness campaigns |

**Default behavior:** Advantage+ Creative is enabled by default on new campaigns. All enhancements are opt-out (you must manually disable ones you do not want).

**Recommendation:** Enable all enhancements during testing phases. Once you identify winning creative, disable enhancements on that specific creative to lock in the version that works, while keeping enhancements on for new test variants.

---

### Framework: Creative Format Decision Tree

**When to use:** When choosing which ad format to use based on your objective, placement, and funnel stage.

```
START → What is your primary objective?

AWARENESS / REACH
  → Do you have video assets?
    YES → Video ad (15-30 sec, 9:16 for Stories/Reels, 4:5 for Feed)
    NO  → Single Image (bold visual, minimal text, brand-forward)

TRAFFIC / ENGAGEMENT
  → Showcasing multiple products or features?
    YES → Carousel (each card = one product/benefit + unique link)
    NO  → Do you have video under 60 seconds?
      YES → Video ad (hook in first 3 sec, CTA at end)
      NO  → Single Image with strong CTA

LEAD GENERATION
  → Want leads to stay on-platform?
    YES → Lead Ad with Instant Form
    NO  → Single Image or Video → landing page with form
  → Need qualifying questions?
    YES → Instant Form with conditional logic fields

SALES / CONVERSIONS
  → E-commerce with product catalog?
    YES → Collection Ad (cover + product grid) or Carousel
    NO  → Do you want immersive storytelling?
      YES → Instant Experience (Storytelling or Custom template)
      NO  → Video ad (testimonial, demo, or offer-focused)

TESTING / ITERATION
  → Want to test multiple creative variants fast?
    YES → Flexible Ad (up to 10 images/videos, 5 text variants)
    NO  → A/B test with individual ad variants
```

---

### Framework: Ad Creative Checklist

**When to use:** Before launching any new campaign — the minimum viable creative set.

```
MINIMUM LAUNCH KIT (per ad set):
[ ] 3-5 creative variants (mix of formats if possible)
[ ] At least 1 video (15-30 sec, vertical 9:16 or portrait 4:5)
[ ] At least 1 static image (4:5 for Feed, 9:16 for Stories)
[ ] 3 primary text variations (different hooks/angles)
[ ] 2 headline variations
[ ] All assets meet platform specs (see spec tables above)

CREATIVE QUALITY CHECKS:
[ ] Hook in first 3 seconds (video) or first visual scan (image)
[ ] Clear value proposition visible without clicking "See More"
[ ] CTA is specific and action-oriented (not generic "Learn More" unless top-of-funnel)
[ ] Mobile-first design — previewed on phone screen
[ ] No excessive text overlay on images (under 20% for best delivery)
[ ] Captions/subtitles on all video (85% of Facebook video is watched without sound)
[ ] Safe zones respected for Stories/Reels (no critical content in top 250px or bottom 340px)

BRANDING:
[ ] Logo visible within first 3 seconds (video) or prominently placed (image)
[ ] Consistent color palette across all variants
[ ] Brand voice consistent across all text variants

COMPLIANCE:
[ ] No prohibited content (before/after images for health, misleading claims)
[ ] No excessive use of "you" in personal attribute references
[ ] Landing page matches ad promise (congruence check)
[ ] All claims substantiated and compliant with Meta Advertising Policies
```

---

### Lead Ad Form Reference

**When to use:** When building Instant Form lead ads.

**Field types available:**
- **Prefill fields:** Full name, email, phone number, city, state, zip code, country, company name, job title (auto-populated from user profile)
- **Custom questions:** Short answer, multiple choice, conditional (branching based on previous answer), appointment scheduling
- **Conditional logic:** Set follow-up questions based on answers (e.g., "What is your budget?" → if >$10K, show "Schedule a call" → if <$10K, show "Download our guide")

**Form types:**
| Type | Best For | Conversion Rate | Lead Quality |
|---|---|---|---|
| **More Volume (Instant Form)** | Maximizing lead count, low-friction offers | Higher | Lower (less intent filtering) |
| **Higher Intent** | Qualified leads, sales team follow-up | Lower | Higher (adds review step before submit) |

**CRM integrations:** Native integrations with Salesforce, HubSpot, Mailchimp, Zapier, and 30+ CRM/marketing automation platforms. Webhook option for custom integrations. Speed-to-lead is critical — leads contacted within 5 minutes convert 9x better than those contacted after 30 minutes.

---

### Call-to-Action Button Reference

**When to use:** When selecting the CTA button for your ad.

| CTA Button | Best For | Typical Objective |
|---|---|---|
| **Shop Now** | E-commerce, product pages | Sales |
| **Learn More** | Content, education, awareness (most versatile, highest overall usage) | Traffic, Awareness |
| **Sign Up** | Newsletters, free trials, webinars | Leads |
| **Book Now** | Appointments, consultations, reservations | Leads, Sales |
| **Contact Us** | Service businesses, high-touch sales | Leads |
| **Download** | Apps, PDFs, lead magnets | App Installs, Leads |
| **Get Offer** | Promotions, discounts, limited-time deals | Sales |
| **Get Quote** | Insurance, services, B2B | Leads |
| **Subscribe** | Memberships, SaaS, recurring products | Sales |
| **Watch More** | Video content, video series | Engagement |
| **Apply Now** | Jobs, programs, applications | Leads |
| **Order Now** | Food delivery, direct purchase | Sales |
| **Send Message** | Messenger/WhatsApp conversations | Messages |
| **Call Now** | Phone-based businesses | Leads |
| **See Menu** | Restaurants | Traffic |
| **Listen Now** | Podcasts, music | Engagement |
| **Play Game** | Gaming | App Installs |

**Selection logic:** Match CTA to the immediate next action the user takes after clicking. "Learn More" is the safest default for top-of-funnel. "Shop Now" and "Sign Up" consistently outperform other CTAs for direct response campaigns. Availability varies by objective — not all CTAs appear for all campaign types.

---

## Key Principles

- **Mobile-first is non-negotiable.** Over 98% of Meta users access via mobile. Design all creative for phone screens first, then adapt for desktop.
- **4:5 for Feed, 9:16 for Stories/Reels.** These aspect ratios maximize screen real estate on mobile. Landscape (16:9) wastes 40%+ of available viewport in Feed.
- **The 3-second rule.** For video: if your hook does not land in the first 3 seconds, you lose the viewer. For images: the value proposition must be visible in a single visual scan.
- **Sound-off by default.** 85% of Facebook video is watched without sound. Always include captions or burned-in text. Design video to work silently.
- **Text truncation is real.** Primary text cuts off at ~125 characters in Feed. Front-load your most important message and CTA within those 125 characters.
- **Flexible Ads outperform single variants.** Letting Meta test combinations of your creative elements typically yields 25-40% better performance than manually picking a single creative.
- **Advantage+ Creative is opt-out, not opt-in.** Enhancements are on by default. Audit your ad preview across placements to ensure enhancements are not degrading your brand aesthetic.
- **Creative diversity beats creative perfection.** Three good variants that test different hooks outperform one "perfect" ad. The algorithm needs options to find what resonates with different audience segments.
- **Refresh creative every 2-3 weeks.** Ad fatigue is signaled by rising frequency (>3.0), declining CTR, and increasing CPA. Fresh creative is the primary lever for sustained performance.
- **Placement-specific creative wins.** Ads customized per placement (separate assets for Feed, Stories, Reels) outperform single assets stretched across all placements via format adaptation.

---

## Decision Tools

### Format Selection by Objective

```
Awareness     → Video (preferred) or Single Image
Traffic       → Single Image, Video, or Carousel
Engagement    → Video, Carousel
Leads         → Lead Ad (Instant Form), Single Image, Video
Sales         → Collection, Carousel, Video, Single Image
App Installs  → Video, Single Image with "Download" CTA
Messages      → Single Image or Video with "Send Message" CTA
```

### Advantage+ Creative On/Off Decision Guide

```
ENABLE Advantage+ Creative when:
[ ] Launching a new campaign with limited creative assets
[ ] Running across multiple placements simultaneously
[ ] Testing phase — want Meta to find best-performing combinations
[ ] Using product catalog images (AI backgrounds add variety)
[ ] Short-form video without voiceover (music enhancement helps)

DISABLE Advantage+ Creative when:
[ ] Creative has already been validated (protect the winning version)
[ ] Brand guidelines require exact visual consistency
[ ] Custom voiceover/audio that should not be altered
[ ] Lifestyle photography with intentional backgrounds
[ ] Running a specific A/B creative test (enhancements add variables)
[ ] Legal/compliance constraints on ad content modification
```

### Creative Fatigue Diagnostic

```
SYMPTOM: Performance declining on a previously strong campaign

CHECK:
[ ] Is frequency > 3.0? → Creative fatigue. Add 3-5 new variants.
[ ] Is CTR declining week over week? → Hook fatigue. Test new opening angles.
[ ] Is CPA rising while CTR holds? → Audience fatigue. Expand targeting.
[ ] Have you refreshed creative in the last 21 days? → If NO, refresh now.
[ ] Are you running fewer than 3 active ad variants? → Too few. Add variety.

ACTION PLAN:
1. Add 3-5 new creative variants (different hooks, formats, angles)
2. Pause ads with frequency > 5.0
3. Keep top performer running alongside new variants
4. Test a completely new format (if all images, try video)
5. Re-evaluate in 5-7 days
```

---

*Chunk 4 of 10 — Facebook Advertising Technical Framework*
