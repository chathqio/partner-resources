# Monster Meta

A strategic Facebook/Meta advertising operator for Claude Code. It pairs a 20-chunk
advertising framework (platform mechanics, expert methodologies, the 2026 AI-first paradigm,
and tactical playbooks) with the self-contained **meta-graph** MCP server, which talks
directly to the Meta Marketing API and **never refuses an operation the Graph API supports**.

Plan, build, audit, and scale real campaigns on **your own** ad accounts. You bring your own
Meta access token; nothing routes through Extendly and you own all ad spend.

## Install

This plugin ships in the **Extendly partner-resources** marketplace. You need access to that
private repo (it comes with your partner-program membership).

```
/plugin marketplace add chathqio/partner-resources
/plugin install monster-meta
```

Restart Claude Code after installing so the MCP server loads.

## One-time setup

1. **Install `uv`** (runs the MCP server, no manual virtualenv):
   `brew install uv`  or  `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Create a Meta token** and export it as `META_ACCESS_TOKEN`. Full walkthrough:
   [`docs/meta-token-setup.md`](./docs/meta-token-setup.md).
3. **Run `/monster-meta setup`** — it validates your token, discovers your ad accounts, pages,
   and pixels, and writes your account config.

## Commands

| Command | What it does |
|---|---|
| `/monster-meta setup` | Validate token, discover accounts/pages/pixels, write config (run this first) |
| `/monster-meta plan` | Campaign strategy: objective, audience, budget, creative approach |
| `/monster-meta build` | Deploy a campaign/ad set/ad/creative to Meta from a plan (PAUSED by default) |
| `/monster-meta audit` | Pull performance data and diagnose issues |
| `/monster-meta scale` | Scaling playbook: budget increases, audience expansion, creative refresh |
| `/monster-meta creative` | Build ad copy variants and creative briefs |

## Notes

- **Safety:** the skill creates campaign objects **PAUSED** by default and never auto-activates
  without your explicit confirmation. Every API write is recorded to the audit-log path you set
  during setup.
- **Agencies / multiple clients:** one token manages every ad account assigned to your
  Business Manager system user. Set a default account in setup; target any other account by id.
- **After a plugin update:** your account config lives inside the installed plugin and a
  `/plugin update` can reset it. Just re-run `/monster-meta setup` (it's idempotent).
- **Your token spends money.** Keep `META_ACCESS_TOKEN` out of any committed file. The MCP
  never logs the token value.

Licensed for Extendly partner-program members only. See [`LICENSE`](./LICENSE).
