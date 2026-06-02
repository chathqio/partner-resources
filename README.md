# Extendly Partner Resources

Private resource library for **Extendly partner-program members**. Access to this repository
is your license to use what's inside — do not share it outside the program.

This repo is a **Claude Code plugin marketplace**. Add it once, then install any plugin it
offers:

```
/plugin marketplace add chathqio/partner-resources
/plugin install monster-meta
```

Restart Claude Code after installing a plugin so its components (skills, MCP servers) load.

## What's inside

| Plugin | What it does |
|---|---|
| [`monster-meta/`](./monster-meta) | Strategic Facebook/Meta ad operator — plan, build, audit, and scale campaigns on your own ad accounts via the bundled meta-graph MCP. Bring your own Meta token. See its [README](./monster-meta/README.md) and [token setup guide](./monster-meta/docs/meta-token-setup.md). |

More partner projects will be added here over time, each as its own plugin in this same
marketplace.

## Prerequisites

- **Claude Code** (latest).
- **[`uv`](https://docs.astral.sh/uv/)** for plugins that bundle a Python MCP server
  (`brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`).

## Support

Questions go to your Extendly partner-program support channel.
