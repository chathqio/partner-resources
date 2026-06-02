# Monster Meta

A strategic Facebook/Meta advertising operator for Claude Code. It pairs a 20-chunk advertising
framework (platform mechanics, expert methodologies, the 2026 AI-first paradigm, and tactical
playbooks) with the self-contained **meta-graph** MCP server, which talks directly to the Meta
Marketing API and **never refuses an operation the Graph API supports**.

Plan, build, audit, and scale real campaigns on **your own** ad accounts. You bring your own Meta
access token; nothing routes through Extendly and you own all ad spend.

## Easiest install: let Claude do it

From the root of the `partner-resources` repo, start Claude and say **"Set up Monster Meta for me."**
Claude follows the onboarding runbook (the repo's `CLAUDE.md`) and handles everything below, pausing
only when it needs you to sign in to GitHub, create your Meta token, or restart Claude Code. See the
repo [README](../README.md).

## Manual install

This plugin ships in the **Extendly partner-resources** marketplace (private; comes with your
partner-program membership).

```
# 1. Install uv (runs the MCP server, no manual virtualenv)
brew install uv        # or: curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Add the marketplace (run from inside your clone of partner-resources)
claude plugin marketplace add .

# 3. Create your Meta token first (see docs/meta-token-setup.md), then install.
#    Secure: run this inside Claude Code and paste the token at the masked prompt —
#        /plugin install monster-meta@extendly-partner-resources
#    Or non-interactively:
claude plugin install monster-meta@extendly-partner-resources --config meta_access_token=YOUR_TOKEN
```

Then **restart Claude Code** so the MCP server loads, and run `/monster-meta:setup`.

### Your token

The plugin asks for one secret: `meta_access_token`. Claude Code stores it in your **OS keychain**
(never a plaintext file) and feeds it to the MCP server automatically. To change it later, run
`/plugin configure monster-meta`. Full walkthrough: [`docs/meta-token-setup.md`](./docs/meta-token-setup.md).

## Commands

| Command | What it does |
|---|---|
| `/monster-meta` | Open the skill (routes to any workflow) |
| `/monster-meta:setup` | Validate token, discover accounts/pages/pixels, write config (run this first) |
| `/monster-meta:plan` | Campaign strategy: objective, audience, budget, creative approach |
| `/monster-meta:build` | Deploy a campaign/ad set/ad/creative to Meta from a plan (PAUSED by default) |
| `/monster-meta:audit` | Pull performance data and diagnose issues |
| `/monster-meta:scale` | Scaling playbook: budget increases, audience expansion, creative refresh |
| `/monster-meta:creative` | Build ad copy variants and creative briefs |

## Notes

- **Safety:** campaign objects are created **PAUSED** by default; the skill never auto-activates
  without your explicit confirmation. Every API write is recorded to the audit-log path you set
  during setup.
- **Agencies / multiple clients:** one token manages every ad account assigned to your Business
  Manager system user. Set a default account in setup; target any other account by id.
- **After a plugin update:** your account config lives inside the installed plugin and a
  `/plugin update` can reset it. Just re-run `/monster-meta:setup` (it's idempotent). Your token is
  unaffected — it lives in the keychain.
- **Your token spends money.** You own all activity on accounts you direct the server to. The MCP
  never logs the token value.

Licensed for Extendly partner-program members only. See [`LICENSE`](./LICENSE).
