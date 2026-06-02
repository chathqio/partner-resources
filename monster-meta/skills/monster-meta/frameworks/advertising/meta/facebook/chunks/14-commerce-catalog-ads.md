# Chunk 14: Commerce & Catalog Ads
## Source: Meta Commerce Manager documentation, practitioner consensus (2026)

---

## Core Concept

Dynamic Product Ads (DPA) and Dynamic Ads for Broad Audiences (DABA) let advertisers automatically show relevant products from their catalog to users based on browsing behavior and purchase intent. Catalog advertising is the backbone of e-commerce scaling on Meta — instead of manually creating ads for each product, you upload a product feed and let the algorithm match the right products to the right users at the right time.

DPA retargets users who already interacted with specific products on your site. DABA prospects entirely new audiences by predicting which catalog items will resonate based on user signals. Together, they form a closed-loop system: DABA fills the top of funnel with new product-aware users, and DPA converts them downstream. With the 2025-2026 rollout of Advantage+ Catalog Campaigns, Meta has further automated this process — collapsing DPA and DABA into a single campaign type that handles both prospecting and retargeting dynamically.

Getting catalog advertising right requires three things: a clean, optimized product feed; strategic product set architecture; and proper retargeting windows with exclusion waterfalls. Neglect any one of these and the algorithm either shows the wrong products, targets the wrong people, or wastes budget re-advertising to customers who already converted.

---

## Frameworks

### Framework: DPA vs DABA

**When to use:** At campaign setup — deciding whether your catalog campaign targets existing site visitors or prospects new audiences.

| Factor | DPA (Retargeting) | DABA (Prospecting) |
|---|---|---|
| **Audience** | Users who viewed/carted/purchased products on your site | New users who have never visited your site |
| **Signal source** | Pixel events (ViewContent, AddToCart, Purchase) | Predicted interest based on user behavior across Meta |
| **Creative** | Shows exact products the user interacted with | Shows products Meta predicts will interest the user |
| **Typical ROAS** | Highest ROAS in most accounts (3-10x) | Lower ROAS than DPA but drives new customer acquisition |
| **Funnel stage** | Bottom of funnel | Top / mid funnel |
| **Minimum data** | Needs sufficient site traffic (1,000+ ViewContent events/week ideal) | Needs a catalog with 50+ products for best results |

**Budget split recommendations:**
- New accounts: 70% DPA / 30% DABA (maximize returns while building data)
- Established accounts: 40% DPA / 60% DABA (shift toward growth)
- Scaling accounts: 30% DPA / 70% DABA (prospecting fuels the retargeting pool)

**Critical note:** DPA performance is capped by your retargeting pool size. If you are not running prospecting (DABA or other TOF campaigns), your DPA audiences shrink over time as users convert or age out of windows.

---

### Framework: Product Feed Optimization

**When to use:** Before launching any catalog campaign — your feed quality directly determines ad quality.

**Required fields (ads will not run without these):**

| Field | Description | Optimization Tips |
|---|---|---|
| `id` | Unique product identifier | Must match your Pixel `content_ids` exactly |
| `title` | Product name | Front-load key attributes: Brand + Product Type + Key Feature + Variant (e.g., "Nike Air Max 90 Running Shoe - Black/White - Men's") |
| `description` | Product description | Lead with benefits, include keywords, 1,000 characters max |
| `price` | Current price | Include currency code (e.g., "29.99 USD") |
| `image_link` | Primary product image URL | Minimum 500x500px, 1:1 aspect ratio recommended, white/clean background |
| `availability` | In stock / out of stock | Update in real-time; showing out-of-stock products wastes impressions |
| `link` | Product page URL | Must include UTM parameters for tracking |

**Recommended fields (significantly improve performance):**

| Field | Impact |
|---|---|
| `google_product_category` | Helps Meta classify products for better matching |
| `brand` | Enables brand-based filtering and product sets |
| `condition` | Required for resale/refurbished goods |
| `sale_price` | Enables automatic "was/now" price overlays |
| `additional_image_link` | Up to 10 additional images; lifestyle shots recommended |
| `product_type` | Your own categorization; useful for product set creation |
| `custom_label_0` through `custom_label_4` | Power fields — use for margin tier, seasonality, best-seller flag, promo eligibility, inventory level |

**Title optimization formula:**
```
[Brand] + [Product Type] + [Key Differentiator] + [Variant/Size/Color]
```
- BAD: "Running Shoe"
- GOOD: "Nike Air Max 90 Lightweight Running Shoe - Men's Black/White"

**Image best practices:**
- Primary image: clean background, product fills 85%+ of frame
- Secondary images: lifestyle/in-use shots, multiple angles, scale reference
- Minimum resolution: 500x500px (1024x1024px+ recommended)
- No text overlays on primary image (Meta may reject or reduce delivery)
- Consistent styling across catalog for brand coherence

**Feed update frequency:**
- Inventory/availability: every 1-6 hours (prevents showing out-of-stock items)
- Prices: daily minimum, real-time for flash sales
- New products: add within 24 hours of going live on site
- Use Scheduled Feed or API for automation; avoid manual CSV uploads at scale

---

### Framework: Product Set Strategy

**When to use:** After uploading your catalog — organizing products into strategic groups for targeted campaigns.

Product sets are subsets of your catalog that you use as the product pool for specific ad sets or campaigns. The algorithm will only show products from the assigned product set.

**Product set types and use cases:**

| Product Set | Use Case | Filter Logic |
|---|---|---|
| **All Products** | Broad prospecting (DABA), general DPA retargeting | No filter — entire catalog |
| **Best Sellers** | Top performers for prospecting; highest conversion probability | Custom label = "best-seller" or sales rank top 20% |
| **High Margin** | Maximize profit per sale, not just revenue | Custom label with margin tier (e.g., "margin-high" for >50% margin) |
| **Cross-Sell Sets** | Post-purchase campaigns: bought X, show Y | Product type or category-based groupings of complementary items |
| **Upsell Sets** | Viewed entry-level, show premium | Price-tiered sets within same category |
| **Seasonal/Promo** | Holiday campaigns, flash sales, clearance | Custom label = "holiday-2026" or sale_price is set |
| **New Arrivals** | Launch campaigns, early adopter targeting | Date added within last 30 days |
| **Category-Specific** | Category-focused campaigns (e.g., "Women's Shoes") | google_product_category or product_type filter |

**Product set architecture for a typical e-commerce account:**
```
Catalog: All Products
├── Prospecting Sets
│   ├── Best Sellers (top 20% by volume)
│   ├── High Margin (>40% margin)
│   └── New Arrivals (last 30 days)
├── Retargeting Sets
│   ├── All Products (show what they viewed)
│   ├── Cross-Sell Bundles (complementary categories)
│   └── Upsell Premium (higher-priced alternatives)
└── Seasonal/Promo Sets
    ├── Current Sale Items
    └── Gift Guide Selections
```

**Custom labels are the key to advanced product sets.** Use your 5 custom label fields strategically:
- `custom_label_0`: Margin tier (high / medium / low)
- `custom_label_1`: Best-seller flag (yes / no)
- `custom_label_2`: Seasonality (spring / summer / fall / winter / evergreen)
- `custom_label_3`: Promo eligibility (promo-eligible / excluded)
- `custom_label_4`: Product lifecycle (new / core / clearance / discontinued)

---

### Framework: Advantage+ Catalog Campaigns

**When to use:** When launching catalog-based campaigns in 2025-2026. This is Meta's default and recommended format.

Advantage+ Catalog Campaigns replace the manual DPA/DABA campaign setup with a unified, algorithm-driven approach. You provide the catalog (or product set), creative templates, and budget — Meta handles audience selection, product matching, format selection, and placement optimization automatically.

**Key features:**
- **Unified prospecting + retargeting:** Single campaign handles both; Meta allocates budget dynamically between new and existing audiences
- **Existing customer budget cap:** Set the maximum percentage of budget that can be spent on existing customers (0-100%). Set low (10-20%) to force prospecting; set higher for retargeting-heavy strategies
- **Automatic product selection:** Algorithm predicts which products from your set are most likely to convert for each user
- **Multi-format delivery:** Automatically tests single image, carousel, and collection formats; allocates impressions to top performer
- **Up to 150 creative assets:** Load variations and let the algorithm test; more creative = more optimization surface

**Creative overlays:**
- Price overlay: displays product price on the image
- Discount percentage: shows "X% off" when `sale_price` is set
- Free shipping badge: highlight shipping offers
- Custom overlay templates: upload brand-consistent templates for price tags, badges, frames
- Catalog overlay editor in Commerce Manager for design customization

**Setup checklist for Advantage+ Catalog Campaigns:**
1. Ensure catalog has 50+ active products with clean feed data
2. Create relevant product sets (best sellers, high margin, etc.)
3. Set existing customer budget cap (start at 20% for growth focus)
4. Upload 5-10 creative variations minimum
5. Configure overlays (price, discount, free shipping as applicable)
6. Set conversion event (Purchase recommended for e-commerce)
7. Launch with sufficient budget for 50+ conversions/week

---

### Framework: Catalog-Based Retargeting Windows

**When to use:** When building retargeting audiences from catalog interaction events.

Retargeting windows define how recently a user must have interacted with your products to be included in the audience. Shorter windows = higher intent but smaller audience. Longer windows = larger audience but lower intent.

**Recommended retargeting windows by event:**

| Event | Window | Message Strategy | Priority |
|---|---|---|---|
| **Initiated Checkout** | 1-3 days | Urgency: "Complete your order," limited stock, discount code | Highest |
| **Add to Cart** | 1-3 days | Reminder: show carted products, social proof, "still available" | Very High |
| **Add to Cart** | 3-7 days | Incentive: discount, free shipping, bundle offer | High |
| **View Content** | 1-7 days | Product education: reviews, benefits, comparison | Medium-High |
| **View Content** | 7-14 days | Social proof: testimonials, "popular item," user photos | Medium |
| **General Site Visit** | 14-30 days | Brand story, catalog browsing, seasonal offers | Lower |
| **Purchase (cross-sell)** | 7-30 days | Complementary products, accessories, refills | Post-Purchase |
| **Purchase (upsell)** | 30-60 days | Premium upgrades, new arrivals in same category | Post-Purchase |

**Exclusion waterfall (critical for efficiency):**
```
Checkout Initiators (1-3d) → Exclude: Purchasers (7d)
Cart Abandoners (1-7d)    → Exclude: Checkout Initiators (3d) + Purchasers (7d)
Product Viewers (1-14d)   → Exclude: Cart Adders (7d) + Purchasers (7d)
Site Visitors (14-30d)    → Exclude: Product Viewers (14d) + Purchasers (14d)
Post-Purchase (7-60d)     → Include ONLY Purchasers; exclude recent purchasers (<7d)
```

The exclusion waterfall prevents users from seeing multiple retargeting messages simultaneously and ensures each user sees the most relevant message for their funnel stage.

---

### Framework: Feed Troubleshooting

**When to use:** When catalog ads underperform or products are disapproved.

**Common feed errors and fixes:**

| Error | Cause | Fix |
|---|---|---|
| Products not showing in ads | `availability` set to "out of stock" or missing required fields | Update feed; check availability status |
| Image rejected | Image too small, has text overlay, or violates ad policy | Use 1024x1024px+, remove text, review Meta ad policies |
| Price mismatch | Feed price does not match landing page price | Sync feed update frequency; ensure prices match exactly |
| Missing Pixel match | Feed `id` does not match Pixel `content_ids` | Audit Pixel implementation; IDs must be identical strings |
| Low delivery | Product set too small or all products disapproved | Expand product set; fix disapproved items |
| "Item can't be used for ads" | Policy violation (prohibited product, misleading description) | Review Meta Commerce Policies; edit title/description |

**Catalog Diagnostics tool (Commerce Manager → Diagnostics):**
- Shows item-level errors, warnings, and suggestions
- Groups issues by severity: errors (blocking), warnings (limiting), suggestions (optimization)
- Provides specific fix instructions for each issue
- Check weekly minimum; daily during launches

**Feed health checklist (run monthly):**
- [ ] All products have titles with key attributes (brand, type, variant)
- [ ] Primary images are 1024x1024px+ with clean backgrounds
- [ ] Prices match landing pages exactly
- [ ] Out-of-stock products are marked correctly (not just hidden)
- [ ] Custom labels are populated for margin, best-seller, and seasonality
- [ ] Feed update schedule is running without errors
- [ ] Pixel `content_ids` match feed `id` for all products
- [ ] No disapproved products in Catalog Diagnostics
- [ ] Product descriptions are benefit-focused and policy-compliant
- [ ] All product links resolve correctly (no 404s)

---

## Key Principles

- **Feed quality is ad quality.** Your product feed is the foundation of every catalog ad. Bad titles, poor images, or stale prices directly degrade ad performance — no amount of audience optimization compensates for a bad feed.
- **Custom labels are your secret weapon.** The five custom label fields give you strategic control over which products appear in which campaigns. Use them for margin tiers, best-seller flags, and promo eligibility.
- **DPA without prospecting is a shrinking strategy.** Retargeting pools deplete as users convert or age out. Always run DABA or other TOF campaigns to refill the funnel.
- **Exclusion waterfalls prevent wasted impressions.** Without them, the same user sees overlapping retargeting from multiple ad sets, inflating frequency and irritating potential customers.
- **Shorter retargeting windows = higher intent.** A 1-day cart abandoner is exponentially more likely to convert than a 30-day site visitor. Allocate budget accordingly.
- **Advantage+ Catalog Campaigns are the default path in 2026.** Manual DPA/DABA setup still works but receives less platform investment. Learn the Advantage+ controls (especially existing customer budget cap) to stay current.
- **Product set architecture is campaign architecture.** How you segment your catalog into product sets determines what the algorithm can show, to whom, and in what context.
- **Update your feed at least daily.** Stale pricing, out-of-stock products shown in ads, and missing new arrivals all damage both performance and customer trust.
- **Catalog size matters for DABA.** Broader catalogs (50+ products) give the algorithm more options for matching products to users. Small catalogs perform better with DPA than DABA.
- **Test creative overlays — they are free performance.** Price badges, discount percentages, and free shipping overlays consistently improve CTR and conversion rate at zero additional creative cost.

---

## Decision Tools

### Catalog Campaign Type Selector

| Your Situation | Recommended Approach |
|---|---|
| E-commerce, 50+ products, strong Pixel data | Advantage+ Catalog Campaign with best-seller product set |
| E-commerce, <50 products | Manual DPA for retargeting; standard prospecting campaigns |
| Want to retarget cart abandoners specifically | DPA with 1-3 day Add to Cart audience |
| Want to prospect new customers with catalog | DABA or Advantage+ Catalog with low existing customer cap |
| Post-purchase cross-sell | DPA with purchase audience, complementary product set |
| Seasonal promotion | Create promo product set via custom labels; run Advantage+ Catalog |

### Product Set Architecture Template

```
Step 1: Label your products
  → Assign margin tier (custom_label_0)
  → Flag best sellers (custom_label_1)
  → Tag seasonality (custom_label_2)
  → Mark promo eligibility (custom_label_3)
  → Set lifecycle stage (custom_label_4)

Step 2: Create product sets
  → Best Sellers: custom_label_1 = "yes"
  → High Margin: custom_label_0 = "high"
  → New Arrivals: date added within 30 days
  → Promo Eligible: custom_label_3 = "promo-eligible"
  → Each major category: filter by product_type

Step 3: Assign to campaigns
  → Prospecting: Best Sellers or High Margin sets
  → Retargeting: All Products (show what they viewed)
  → Post-Purchase: Cross-sell sets by category
  → Seasonal: Promo Eligible set
```

### Feed Optimization Checklist

- [ ] Titles follow [Brand] + [Type] + [Differentiator] + [Variant] formula
- [ ] All images are 1024x1024px+ with clean backgrounds
- [ ] `sale_price` is set for all items currently on promotion
- [ ] All 5 custom labels are populated with strategic values
- [ ] Feed updates are automated (API or scheduled feed) at least daily
- [ ] Pixel `content_ids` audit completed — all IDs match feed `id`
- [ ] Catalog Diagnostics shows zero errors
- [ ] Product descriptions are benefit-led and include relevant keywords
- [ ] Out-of-stock handling is configured (hide or show with "sold out" label)
- [ ] At least 2 additional images per product (lifestyle shots)

---

*Chunk 14 of 20 — Facebook Advertising Technical Framework*
