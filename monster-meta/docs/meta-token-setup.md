# Getting your Meta access token

Monster Meta talks to your own Meta Ads account through the `meta-graph` MCP server. The
server needs **one thing from you: a long-lived Meta access token** with ad-management
permissions. You create it once. This guide walks you through it.

You are bringing your **own** Meta app and token — nothing routes through Extendly, and you
own all ad spend on your accounts.

> **Time:** ~15 minutes the first time. **You need:** a Facebook account that is an admin of
> a Meta Business Manager that owns (or has access to) the ad accounts you want to manage.

---

## What you're creating

| Piece | Why |
|---|---|
| A **Meta Developer app** | The container Meta requires for any API access. Stays in Development mode — never needs App Review, because you only ever access your **own** accounts. |
| A **System User** in your Business Manager | A non-human identity whose token does not expire when a person logs out. This is the recommended token source for ongoing automation. |
| Asset assignments | You grant the System User access to the specific ad accounts + pages it should manage. |
| A **long-lived System User token** | The string you paste into the MCP config as `META_ACCESS_TOKEN`. |

---

## Step 1 — Create a Meta app

1. Go to <https://developers.facebook.com/apps> and click **Create App**.
2. Use case: choose **Other** → app type **Business**.
3. Name it (e.g. "My Agency Ads MCP"), pick your Business Manager as the business, and create it.
4. In the app dashboard, add the **Marketing API** product (find it under "Add products").

You do **not** need to submit for App Review and you do **not** need to switch the app to
Live, because you will only call the API against accounts your own Business Manager controls.

## Step 2 — Create a System User

1. Open **Business Settings** at <https://business.facebook.com/settings>.
2. Left sidebar → **Users → System Users** → **Add**.
3. Name it (e.g. "ads-mcp"), role **Admin** (or Employee if you prefer tighter scope), create.

## Step 3 — Assign assets to the System User

Still in System Users, with your new system user selected, click **Assign Assets** and add:

- **Ad Accounts** — every ad account (yours and your clients') you want Monster Meta to manage. Give **Manage** (full control) access.
- **Pages** — the Facebook Page(s) ads will run from. Give **Manage** access.
- (Optional) **Pixels / Datasets** if you'll set up conversion tracking through the tool.

> **Agencies:** this is how one token manages many clients. Any ad account assigned to this
> system user is reachable by passing its `act_…` id. Add a client's ad account here when you
> onboard them; remove it when you offboard.

## Step 4 — Generate the token

1. With the system user selected, click **Generate New Token**.
2. Select your app from Step 1.
3. Token expiration: choose **Never** (System User tokens can be non-expiring).
4. Select these permissions (scopes):
   - `ads_management` — create/edit campaigns, ad sets, ads (required for build/scale)
   - `ads_read` — read performance + structure (required for audit)
   - `business_management` — read/manage Business Manager assets
   - `pages_read_engagement` and `pages_manage_ads` — needed when ads post from a Page
5. Generate, then **copy the token now** — Meta shows it only once. Store it in your password manager.

## Step 5 — Give the token to the plugin

The plugin asks for your token as a **secure config value** (`meta_access_token`). Claude Code
stores it in your **operating system's keychain** — not a plaintext file — and hands it to the MCP
server automatically. You enter it once.

Two ways to provide it:

- **Secure (recommended)** — inside Claude Code, run the slash command and paste the token at the
  **masked** prompt:
  ```
  /plugin install monster-meta@extendly-partner-resources
  ```
  Already installed? Set or update the token the same masked way:
  ```
  /plugin configure monster-meta
  ```
- **Non-interactive** — pass it on the command line (note: this records the token in your shell
  history; rotate it afterward if you're on a shared machine):
  ```bash
  claude plugin install monster-meta@extendly-partner-resources --config meta_access_token=YOUR_TOKEN
  ```

> **Prerequisite:** the MCP server runs via [`uv`](https://docs.astral.sh/uv/). Install it once:
> `brew install uv` (macOS) or `curl -LsSf https://astral.sh/uv/install.sh | sh`. `uv` builds the
> server's isolated Python environment on first launch — you do not create a virtualenv yourself.

After setting the token, **restart Claude Code** so the `meta-graph` MCP server loads with it.

## Step 6 — Verify

After restarting Claude Code, run `/monster-meta:setup`. It calls `whoami` to confirm the token
is valid, shows which scopes you granted, lists the ad accounts it can see, and writes your
account config. If `whoami` fails, re-check Steps 4–5 (most often: you didn't restart after
setting the token, the token wasn't saved, or a required scope is missing).

---

## Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `whoami` says token invalid/expired | Token not saved, didn't restart Claude Code after setting it, or you generated an expiring user token instead of a System User token. Set it via `/plugin configure monster-meta`, restart, and re-do Step 4 with expiration **Never** if needed. |
| `mcp__meta-graph__*` tools missing | The MCP didn't load: confirm you restarted Claude Code after setting the token, and that `uv` is installed. |
| `get_ad_accounts` returns nothing | The System User has no ad accounts assigned. Go back to Step 3 and assign them. |
| Writes fail with a permissions error | Missing `ads_management`, or the system user has only **View** (not **Manage**) on the ad account. |
| "uv: command not found" | Install `uv` (see prerequisite above) and restart Claude Code. |
| Ads won't deliver from the Page | Add `pages_manage_ads` + `pages_read_engagement` and assign the Page to the system user. |

Your token is sensitive — it can spend money on your ad accounts. Claude Code keeps it in your OS
keychain and the MCP never prints or logs the value. If you ever pass it via `--config` on the
command line, clear it from your shell history (or rotate the token) on shared machines.
