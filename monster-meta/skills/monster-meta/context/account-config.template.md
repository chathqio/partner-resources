# Account Config

> **Template.** `/monster-meta setup` fills this in from your own Meta account (it reads
> your accounts, pages, and pixels via the `meta-graph` MCP using your token). You can also
> edit the values by hand. Anything left as a `{{PLACEHOLDER}}` is not yet configured.

## Meta Ads Account
- **Account ID:** {{ACCOUNT_ID}}            <!-- e.g. act_1234567890 -->
- **Account Name:** {{ACCOUNT_NAME}}
- **Currency:** {{CURRENCY}}                 <!-- e.g. USD -->
- **Timezone:** {{TIMEZONE}}                 <!-- e.g. America/Los_Angeles -->

> **Agencies / multiple clients:** one token can manage every ad account in your Business
> Manager. Set the account you work with most often above; pass a different `account_id`
> per call (or re-run `/monster-meta setup`) to switch clients. Leaving the account blank
> means every build/audit step will ask which account to use.

## Facebook Page
- **Page ID:** {{PAGE_ID}}
- **Page Name:** {{PAGE_NAME}}

## Instagram
- **Instagram Actor ID:** {{INSTAGRAM_ACTOR_ID}}   <!-- optional; connected to the page above -->

## UTM Tagging — OPTIONAL, configurable per partner

UTM parameters are **off by default** in this template. If your reporting depends on
consistent UTMs, set a scheme below and the skill will apply it to every destination URL
it produces (plans, creative briefs, `create_ad_creative` calls). If you leave this
section as-is, the skill uses URLs exactly as you supply them.

- **UTM enforcement:** {{UTM_ENFORCEMENT}}    <!-- off | append | strict -->
  - `off` — use destination URLs as supplied; never modify.
  - `append` — add any missing UTM params from the scheme below; flag the addition.
  - `strict` — every destination URL MUST match the scheme; pause and confirm on any deviation.

### Scheme (used only when enforcement is `append` or `strict`)

| Parameter | Value | Notes |
|---|---|---|
| `utm_source` | {{UTM_SOURCE}} | Platform, e.g. `facebook`. |
| `utm_medium` | {{UTM_MEDIUM}} | e.g. `paid`. |
| `utm_campaign` | {{UTM_CAMPAIGN}} | Your campaign-tagging convention, e.g. `{monDD}_{type}`. |
| `utm_content` | `[[ad.name]]` | **Meta dynamic macro — literal string.** Meta substitutes each ad's name at click time. One URL covers all ads in a set. Leave as the literal `[[ad.name]]`. |

## Tracking
- **Primary Pixel ID:** {{PRIMARY_PIXEL_ID}}        <!-- used for CAPI / conversion campaigns -->
- **CAPI Configured:** {{CAPI_CONFIGURED}}          <!-- yes | no -->
- **Other pixels on account:** {{OTHER_PIXELS}}     <!-- list; mark any "do not use" -->

## Defaults
- **Default Objective:** {{DEFAULT_OBJECTIVE}}      <!-- e.g. OUTCOME_LEADS -->
- **Default Bid Strategy:** {{DEFAULT_BID_STRATEGY}} <!-- e.g. LOWEST_COST_WITHOUT_CAP -->
- **Default Billing Event:** {{DEFAULT_BILLING_EVENT}} <!-- e.g. IMPRESSIONS -->
- **Default Status on Create:** PAUSED              <!-- always PAUSED unless you change it -->
- **Naming Convention:** {{NAMING_CONVENTION}}      <!-- e.g. {date} - {objective} - {audience} - {variant} -->

## Audit Log
- **Audit-log path:** {{AUDIT_LOG_PATH}}            <!-- where the skill records every API write; e.g. ./meta-ads-audit/audit-log.md -->
