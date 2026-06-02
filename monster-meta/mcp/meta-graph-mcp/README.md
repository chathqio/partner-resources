# meta-graph-mcp

A **comprehensive, self-contained** Facebook/Meta Graph + Marketing API MCP server, bundled
with the Monster Meta plugin.

**Design tenet:** *this server never refuses an operation the Graph API supports.* Generic
passthrough primitives reach **any node, edge, field, HTTP verb, and API version**; ~80 named
convenience tools are thin and additive — they forward unknown params untouched and never gate.
If a named tool doesn't model something, drop to a primitive. Meta's own error object is
returned verbatim — an API rejection is never reinterpreted as a tool limitation.

> Licensed for Extendly partner-program members only. See `LICENSE`.

## How it runs

Inside the Monster Meta plugin, the plugin's `.mcp.json` launches this server with
[`uv`](https://docs.astral.sh/uv/):

```
uv run --directory ${CLAUDE_PLUGIN_ROOT}/mcp/meta-graph-mcp meta-graph-mcp
```

`uv` builds the isolated Python environment (3.11+, `mcp` + `httpx`) on first launch — you do
not create a virtualenv. Install `uv` once: `brew install uv` or
`curl -LsSf https://astral.sh/uv/install.sh | sh`.

## Authentication — bring your own token

The server resolves its access token from `META_ACCESS_TOKEN`. You supply your own long-lived
Meta token (System User token recommended). See the plugin's `docs/meta-token-setup.md`. The
token value is never returned by any tool or written to any log.

## Config (env)

| Var | Default | Meaning |
|---|---|---|
| `META_ACCESS_TOKEN` | (required) | Your user/system-user access token |
| `GRAPH_API_VERSION` | `v25.0` | Graph/Marketing API version (per-call override available) |
| `META_DEFAULT_ACCOUNT` | (unset) | Expands the `{account}` placeholder to an `act_…` id |
| `META_APP_SECRET` | (unset) | If set, every call sends `appsecret_proof` |
| `META_GRAPH_READONLY` | `0` | `1` blocks all writes (reads still work) |

## Primitives

| Tool | Purpose |
|---|---|
| `graph_get` | GET any node/edge (supports nested field expansion) |
| `graph_post` | POST = create **or** update any node/edge; `validate_only` (Meta dry run) and `dry_run` (local preview) supported |
| `graph_delete` | DELETE a node (prefer pausing campaign objects) |
| `graph_paginate` | GET an edge, auto-follow cursors |
| `graph_batch` | Graph Batch API — many ops, one round-trip |
| `graph_call` | Escape hatch — any verb/path/version |
| `whoami` | Token identity, scopes, expiry, validity (token value never returned) |
| `meta_graph_help` | Structure + common recipes |

Named convenience tools cover campaigns, ad sets, ads, creatives, assets, insights (+ async),
audiences (+ PII hashing), CAPI, targeting, estimates, catalogs, leadgen, previews, pixels, and
business assets.

## Security

- `httpx`/`httpcore` logging forced to WARNING so the token (a query param) never reaches logs.
- Any `access_token=…` in returned bodies (e.g. paging URLs) is redacted.
- Meta rate-limit headers (`X-App-Usage`, `X-Business-Use-Case-Usage`, `X-Ad-Account-Usage`)
  are surfaced, not hidden.

## Conventions

- Campaign objects are created/left **PAUSED** unless activation is explicitly authorized.
- Budget changes are financially material — preview with `dry_run=True` or `validate_only=True`,
  confirm, then write. These are surfaced as previews/warnings, **never refusals**.
- The Monster Meta skill records every Graph **write** to the audit-log path you configure
  during `/monster-meta setup`.

## Your token spends money

`META_ACCESS_TOKEN` can create and edit ads on your accounts. Keep it out of any committed
file. You are responsible for all activity and spend on accounts you direct the server to.
