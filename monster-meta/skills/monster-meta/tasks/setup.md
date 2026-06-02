<purpose>
First-run configuration wizard. Validates the user's Meta access token, auto-discovers their
ad accounts, pages, and pixels via the meta-graph MCP, and writes a personalized
context/account-config.md from the template. Idempotent — safe to re-run any time (e.g. after a
plugin update, when switching the default client account, or to change UTM/audit settings).
</purpose>

<user-story>
As a new partner installing Monster Meta, I want a guided one-time setup that confirms my token
works and fills in my own account/page/pixel details, so that the plan/build/audit/scale commands
operate on my account without me hand-editing config files.
</user-story>

<when-to-use>
- First time using the skill after installing the plugin (account-config.md is the stub or has {{PLACEHOLDER}} values)
- After a `/plugin update` that may have reset account-config.md
- To switch the default client account, change the UTM scheme, or change the audit-log path
- Entry point routes here via /monster-meta setup
</when-to-use>

<context>
@context/account-config.template.md
</context>

<steps>

<step name="validate_token" priority="first">
Confirm the MCP is connected with a working token.

1. Call `whoami`. This returns the token identity, granted scopes, and expiry (never the token value itself).
2. If the call fails or returns an invalid/expired token:
   - Tell the user the `meta-graph` MCP is not connected with a valid token.
   - Point them to `docs/meta-token-setup.md` (how to create a Meta app, a System User, and a long-lived token with `ads_management` + `business_management`), and to set it as `META_ACCESS_TOKEN` for the MCP.
   - **Stop here** — nothing else works without a valid token.
3. If valid, report the identity and which scopes are present. Warn if `ads_management` or `business_management` is missing (builds/writes will fail without them), and warn if the token expires soon.

**Wait for a working token before continuing.**
</step>

<step name="discover_accounts">
Find the ad accounts this token can manage.

1. Call `get_ad_accounts`. List every account returned with its `act_` id, name, currency, timezone, and account status.
2. If none are returned: the token's user/system-user has no ad accounts assigned. Point the user to add ad accounts to their Business Manager and assign the System User (see `docs/meta-token-setup.md`), then stop.
3. If one account: use it as the default.
4. If several (typical for agencies): ask which account to set as the **default** in the config. Note explicitly that this is only a default — they can target any of their accounts per-call, and re-running setup switches it.

**Ask the user to pick the default account if there is more than one.**
</step>

<step name="discover_assets">
Pull the page, Instagram actor, and pixels for the chosen account.

1. Call `get_account_pages` for the chosen account. If multiple pages, ask which to use as the default. Capture page id + name. Capture the connected Instagram actor id if present.
2. Call `get_pixels` for the chosen account. List each pixel (id + name). Ask which is the primary conversion pixel; ask whether CAPI is configured for it. Note any pixels the user flags as "do not use."
3. Pull currency/timezone from the account info gathered in `discover_accounts`.
</step>

<step name="capture_preferences">
Collect the configurable conventions. Offer sensible defaults; do not impose any one agency's scheme.

Ask (batch these; accept defaults if the user just confirms):
1. **UTM enforcement:** `off` (default), `append`, or `strict`. Explain: off = use URLs as supplied; append = add missing UTM params and flag it; strict = require the scheme and confirm on deviation.
2. If `append`/`strict`: capture `utm_source` (default `facebook`), `utm_medium` (default `paid`), and the `utm_campaign` convention. Keep `utm_content` as the literal `[[ad.name]]` macro.
3. **Audit-log path:** where every API write is recorded. Default `./meta-ads-audit/audit-log.md` relative to the user's working directory.
4. **Defaults:** objective (default `OUTCOME_LEADS`), bid strategy (default `LOWEST_COST_WITHOUT_CAP`), billing event (default `IMPRESSIONS`), naming convention (default `{date} - {objective} - {audience} - {variant}`). Status on create stays `PAUSED`.
</step>

<step name="write_config">
Render context/account-config.md from the template.

1. Read `@context/account-config.template.md`.
2. Substitute every `{{PLACEHOLDER}}` with the discovered/confirmed values. Leave the UTM scheme rows generic if enforcement is `off`.
3. Write the result to `context/account-config.md` (this is the file every task `@imports`). Overwrite the stub or any prior config.
4. If the audit-log path's parent directory does not exist, note that the first write will create it.

**Confirm before overwriting** if the existing account-config.md already has real (non-placeholder) values — show a short diff of what changes.
</step>

<step name="confirm">
Summarize the resulting config back to the user:
- Default account (id, name, currency, timezone)
- Page (+ Instagram actor if any)
- Primary pixel + CAPI status
- UTM enforcement mode and audit-log path
- Defaults

Tell them they're ready to run `/monster-meta plan`, and that they can re-run `/monster-meta setup` any time to change accounts or preferences.
</step>

</steps>
