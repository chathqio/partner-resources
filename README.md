# Extendly Partner Resources

Private resource library for **Extendly partner-program members**. Access to this repository is
your license to use what's inside, so please don't share it outside the program.

This repo is a **Claude Code plugin marketplace**. Each plugin is a self-contained AI tool you
install into Claude Code. More partner tools are added here over time.

You do **not** need to be technical to use this. The recommended path hands the whole setup to
Claude, which walks you through everything one plugin at a time.

---

## What's inside

| Plugin | What it does | Runs on | Setup |
|---|---|---|---|
| [`monster-meta/`](./monster-meta) | Plan, build, audit, and scale Facebook/Meta ad campaigns on your own ad accounts via the bundled meta-graph MCP. | Claude Code only | Needs `uv` + your own Meta token. See [`monster-meta/ONBOARDING.md`](./monster-meta/ONBOARDING.md). |
| [`fitd-builder/`](./fitd-builder) | Craft a complete niche-specific foot-in-the-door offer: hook + story + hydrated OfferIQ pillars + ready ad/VSL/landing copy. | Claude Code **and claude.ai** | Install and go, no token. See [`fitd-builder/ONBOARDING.md`](./fitd-builder/ONBOARDING.md). |

**No terminal? Start here instead:** [`claude-ai/README.md`](./claude-ai/README.md). fitd-builder
runs in claude.ai chat, in Cowork, and in Claude Code on the web. monster-meta genuinely cannot,
because it needs a local MCP server process and a long-lived Meta token;
[`PLATFORMS.md`](./PLATFORMS.md) explains what runs where and why.

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
# 1. Add this repo as a marketplace. Prefer the GitHub source: it's the only one
#    `claude plugin update` can pull new versions from.
claude plugin marketplace add chathqio/partner-resources
#    Not signed in to GitHub yet? Install from your local clone instead, and know
#    that updates won't work until you run `gh auth login`:
#    claude plugin marketplace add .

# 2. See what's available
claude plugin marketplace list

# 3. Install a plugin, then follow its ONBOARDING.md
claude plugin install fitd-builder@extendly-partner-resources     # no token needed
claude plugin install monster-meta@extendly-partner-resources     # then see monster-meta/ONBOARDING.md
```

Per-plugin setup lives in each plugin's `ONBOARDING.md` and `README.md`. Some plugins (like
monster-meta) need extra prerequisites; the onboarding for that plugin covers them.

---

## Staying up to date

**In Claude Code, updates are automatic** — on your own machine and on the web. Each plugin checks its own version whenever you use it
and installs the new one when it's behind, then asks you to run `/reload-plugins`. The check runs in
the background, so it never slows a tool down, and it stays quiet when you're current. If you'd
rather be asked first, set `EXTENDLY_SKILL_UPDATE_CHECK=notify`; to turn it off entirely, set it to
`off`.

It relies on GitHub access to this private repo, so run `gh auth login` once if you haven't.

Claude Code on the web (`claude.ai/code`) is covered too: it runs the same check, and a fresh cloud
session installs the plugin from the marketplace anyway, so it starts current.

**In claude.ai chat and Cowork, updates are manual.** An uploaded skill has no hook system, so it
can't check itself. Ask "what version of the fitd-builder skill are you running?", compare it
against [`VERSIONS.json`](./VERSIONS.json), and re-upload the bundle if you're behind.
[`claude-ai/README.md`](./claude-ai/README.md) walks through it.

## Support

Questions go to your Extendly partner-program support channel.
