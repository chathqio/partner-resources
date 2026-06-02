# Extendly Partner Resources

Private resource library for **Extendly partner-program members**. Access to this repository is
your license to use what's inside — please don't share it outside the program.

This repo is a **Claude Code plugin marketplace**. Today it ships **Monster Meta**: an AI operator
that plans, builds, audits, and scales Facebook/Meta ad campaigns on your own ad accounts. More
partner tools will be added here over time.

You do **not** need to be technical to use this. The recommended path hands the whole setup to
Claude, which walks you through everything.

---

## What you'll need

- A **computer** (macOS, Windows, or Linux).
- A **Facebook/Meta Business Manager** you administer, with the ad accounts you want to manage.
- About **20 minutes** for first-time setup (most of it is creating a Meta access token, once).

That's it. Claude installs the technical bits (a tool called `uv`, the plugin, the ad-API server)
for you.

---

## Fast path — let Claude set it up for you

**1. Install Claude Code.** Follow Anthropic's installer: <https://docs.claude.com/en/docs/claude-code/overview>.
This gives you the `claude` command in your terminal (Terminal on macOS, PowerShell on Windows).

**2. Get this repository onto your computer.** You were given access to it as part of the partner
program. In your terminal:

```bash
# one-time GitHub sign-in so you can access the private repo
gh auth login          # if you don't have the GitHub CLI, install it: https://cli.github.com

git clone https://github.com/chathqio/partner-resources.git
cd partner-resources
```

**3. Start Claude here and ask it to set up Monster Meta.**

```bash
claude
```

Then type:

> **Set up Monster Meta for me.**

Claude reads the onboarding runbook in this repo (`CLAUDE.md`) and takes over: it installs the
prerequisites, adds the marketplace, installs the plugin, helps you create and securely store your
Meta token, and verifies everything works. It will pause and ask you only when it needs you to do
something it can't — sign in to GitHub, create your Meta token in the browser, and restart Claude
Code once. When it's done, it confirms Monster Meta is live and shows you the commands.

> Your Meta token is stored in your operating system's **keychain** (never in a plain text file),
> entered at a **masked** prompt. Claude doesn't keep a copy.

---

## Manual path — do it yourself

Prefer to run the steps yourself? Each is a normal command.

```bash
# 1. Install uv (runs the ad-API server). Pick one:
brew install uv                                            # macOS w/ Homebrew
curl -LsSf https://astral.sh/uv/install.sh | sh            # macOS/Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" # Windows

# 2. Add this repo as a marketplace (run from inside the clone)
claude plugin marketplace add .

# 3. Create your Meta token first — see monster-meta/docs/meta-token-setup.md
#    Then install the plugin. Secure option: run the slash command inside Claude Code and
#    paste the token at the masked prompt:
#        /plugin install monster-meta@extendly-partner-resources
#    Or non-interactively (token goes into your shell history — rotate it afterward on shared machines):
claude plugin install monster-meta@extendly-partner-resources --config meta_access_token=YOUR_TOKEN

# 4. Restart Claude Code so the ad-API server loads, then run setup inside Claude:
#        /monster-meta:setup
```

Full token walkthrough: [`monster-meta/docs/meta-token-setup.md`](./monster-meta/docs/meta-token-setup.md).
Plugin details and commands: [`monster-meta/README.md`](./monster-meta/README.md).

---

## What's inside

| Plugin | What it does |
|---|---|
| [`monster-meta/`](./monster-meta) | Plan, build, audit, and scale Meta ad campaigns on your own accounts via the bundled meta-graph MCP. Bring your own Meta token. |

## Using it after setup

- `/monster-meta` — open the skill
- `/monster-meta:plan` · `:build` · `:audit` · `:scale` · `:creative` — the workflows
- `/monster-meta:setup` — re-run setup (switch default account, change preferences)

Campaigns are created **PAUSED** by default; nothing activates without your confirmation. Your token
can spend money on your ad accounts — you own all activity on them.

## Support

Questions go to your Extendly partner-program support channel.
