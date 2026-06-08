# Extendly Partner Resources

Private resource library for **Extendly partner-program members**. Access to this repository is
your license to use what's inside, so please don't share it outside the program.

This repo is a **Claude Code plugin marketplace**. Each plugin is a self-contained AI tool you
install into Claude Code. More partner tools are added here over time.

You do **not** need to be technical to use this. The recommended path hands the whole setup to
Claude, which walks you through everything one plugin at a time.

---

## What's inside

| Plugin | What it does | Setup |
|---|---|---|
| [`monster-meta/`](./monster-meta) | Plan, build, audit, and scale Facebook/Meta ad campaigns on your own ad accounts via the bundled meta-graph MCP. | Needs `uv` + your own Meta token. See [`monster-meta/ONBOARDING.md`](./monster-meta/ONBOARDING.md). |
| [`fitd-builder/`](./fitd-builder) | Craft a complete niche-specific foot-in-the-door offer: hook + story + hydrated OfferIQ pillars + ready ad/VSL/landing copy. | Install and go, no token. See [`fitd-builder/ONBOARDING.md`](./fitd-builder/ONBOARDING.md). |

---

## Fast path - let Claude set it up for you

**1. Install Claude Code.** Follow Anthropic's installer:
<https://docs.claude.com/en/docs/claude-code/overview>. This gives you the `claude` command in your
terminal (Terminal on macOS, PowerShell on Windows).

**2. Get this repository onto your computer.** You were given access to it as part of the partner
program. In your terminal:

```bash
# one-time GitHub sign-in so you can access the private repo
gh auth login          # if you don't have the GitHub CLI, install it: https://cli.github.com

git clone https://github.com/chathqio/partner-resources.git
cd partner-resources
```

**3. Start Claude here and ask it to set you up.**

```bash
claude
```

Then type:

> **Set up the partner tools for me.**

Claude reads the onboarding runbook in this repo (`CLAUDE.md`), adds the marketplace, shows you
**which plugins are available and which you already have**, and lets you **pick what to install**.
It then sets up each one you chose, in turn, pausing only when it needs something it can't do for
you (a GitHub sign-in, a token, a restart). You can re-run this any time to add more plugins later.

---

## Manual path - do it yourself

```bash
# 1. Add this repo as a marketplace (run from inside the clone)
claude plugin marketplace add .

# 2. See what's available
claude plugin marketplace list

# 3. Install a plugin, then follow its ONBOARDING.md
claude plugin install fitd-builder@extendly-partner-resources     # no token needed
claude plugin install monster-meta@extendly-partner-resources     # then see monster-meta/ONBOARDING.md
```

Per-plugin setup lives in each plugin's `ONBOARDING.md` and `README.md`. Some plugins (like
monster-meta) need extra prerequisites; the onboarding for that plugin covers them.

## Support

Questions go to your Extendly partner-program support channel.
