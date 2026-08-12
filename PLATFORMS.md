# What runs where

Not every plugin in this marketplace can run on every Claude surface, and the reasons are
structural rather than cosmetic. This file is the authoritative answer. `VERSIONS.json` carries
the same information as data (`platforms` per plugin) and is what tooling reads.

## The three surfaces

| Surface | What it is | What it supports |
|---|---|---|
| `cli` | Claude Code on your own machine: terminal, IDE extension, desktop app | Everything. Plugins, slash commands, hooks, MCP servers, `userConfig` secrets in your OS keychain |
| `cloud` | Claude Code cloud sessions: `claude.ai/code`, `claude --cloud`, routines, mobile | The cloned repo's `.claude/skills/`, any plugin declared in the repo's `.claude/settings.json`, and **hooks** from both. Never reads your local `~/.claude`. No secret store |
| `claude-ai` | claude.ai chat and Cowork, via a skill uploaded to your claude.ai account | A skill directory and its supporting files, nothing else. No slash commands, no hooks, no MCP servers, no dynamic context injection |

> **`claude.ai/code` is `cloud`, not `claude-ai`.** Both live on claude.ai, which makes this easy
> to get wrong. A cloud session is real Claude Code with a real shell: it installs plugins and runs
> their hooks. `claude-ai` here means specifically a skill uploaded to a claude.ai account and used
> in chat or Cowork, where there is no shell and no hook system.

## Compatibility matrix

| Plugin | cli | cloud | claude-ai | Why |
|---|---|---|---|---|
| `fitd-builder` | yes | yes | yes | Self-contained. No MCP, no token, network optional |
| `monster-meta` | yes | no | no | Needs a local MCP server process and a long-lived Meta token |

### Why monster-meta is CLI only

This is not a packaging gap waiting to be closed:

1. The skill is inert without the bundled `meta-graph` MCP server. A claude.ai skill is a
   directory of instructions and files; it cannot ship or start an MCP server.
2. It needs a long-lived Meta access token with `ads_management`. On the CLI that lives in your
   OS keychain via the plugin's `userConfig`. Cloud environments have no secret store, and
   Anthropic's own documentation warns against putting credentials in their environment
   variables because anyone using the environment can read them.

So monster-meta stays a CLI plugin. Its onboarding says so up front rather than letting someone
spend twenty minutes discovering it.

## The rule for claude.ai-capable skills

Outside Claude Code, `SKILL.md` frontmatter may contain **only** these six fields:

```
name  description  license  compatibility  metadata  allowed-tools
```

Anything else is a hard error, not an ignored field. claude.ai uploads, the Skills API, and
`package_skill.py` all reject the whole skill:

```
Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are:
allowed-tools, compatibility, description, license, metadata, name
```

This is what used to break fitd-builder on claude.ai. Its frontmatter carried `type`,
`version`, and `category`, so the upload failed before anyone saw the skill run. `version` and
`category` now live under `metadata`, which is a free-form map the spec allows, and `type` is
gone because nothing ever read it.

Claude Code accepts all six spec fields, so a spec-compliant skill needs no separate variant.
**The skill directory is the claude.ai bundle.** `scripts/build-skill-bundle.py` zips it as is,
and `scripts/validate.py` fails the build if a claude.ai-capable skill grows a non-spec field.
There is no second copy of the skill content in this repo, so nothing can drift.

If a skill genuinely needs a Claude Code-only field (`context: fork`, `paths`,
`disable-model-invocation`, `argument-hint`), that is a decision to drop it to `cli` only.
`validate.py` warns rather than fails for CLI-only skills.

## CLI-only paths inside a plugin

A plugin's own scaffolding never reaches claude.ai, and that is fine:

| Path | Why it is CLI only |
|---|---|
| `<plugin>/.claude-plugin/plugin.json` | Plugin manifest. Marketplace installs only |
| `<plugin>/commands/` | Slash commands. Do not exist on claude.ai |
| `<plugin>/hooks/` | Plugin hooks. No hook system on claude.ai |
| `<plugin>/scripts/check-update.sh` | Driven by those hooks |
| `<plugin>/ONBOARDING.md` | Instructions for a Claude Code install |
| `monster-meta/mcp/`, `monster-meta/.mcp.json` | MCP server |

Because `commands/` is absent on claude.ai, a portable skill must route on intent as well as on
its slash commands. fitd-builder's `<commands>` block spells out that mapping.

## Staying current

| Surface | Update mechanism |
|---|---|
| `cli` | Automatic, via the update hook. See [the self-update section in CLAUDE.md](./CLAUDE.md#skill-self-update) |
| `cloud` | Automatic twice over: a new session installs the plugin fresh from the marketplace, and the update hook runs there too, which catches a resumed or long-running session that has drifted |
| `claude-ai` | Manual. Rebuild the bundle and re-upload |

The check is a plugin hook, and hooks do run in cloud sessions: Claude Code runs hooks from the
cloned repo, and a plugin declared in the repo's `.claude/settings.json` is installed at session
start with its hooks intact. So `claude.ai/code` is covered.

**claude.ai chat and Cowork are the only gap.** An uploaded skill has no hook system, so it cannot
learn that a newer version was published. What it does have is `metadata.version` in its own
frontmatter, so you can always ask Claude which version it is running and compare that against
`VERSIONS.json`. `claude-ai/README.md` covers it.

**Not built, but the obvious fix if manual re-uploads become a problem:** publish
`VERSIONS.json` to a public path on `partner.extendly.com` (the site the offer menu already
comes from) and have the skill body fetch it on load. That would give claude.ai users a version
warning without any hook system. It needs a deploy to the `partner` repo, so it is deliberately
out of scope here.

## Adding a new plugin or skill

1. Decide its platforms. Default to `["cli", "cloud", "claude-ai"]` and only narrow it when
   something structural forces the issue, the way an MCP server does for monster-meta.
2. If it is claude.ai-capable, keep `SKILL.md` frontmatter inside the six spec fields and put
   your own data under `metadata`.
3. Add it to `VERSIONS.json` with `version` as the first key in its object, plus its
   `platforms`, `skill` path, `requires`, and `cliOnlyPaths`.
4. Add it to `.claude-plugin/marketplace.json`.
5. Add `hooks/hooks.json` (copy an existing one, change the `UserPromptExpansion` matcher to
   the plugin name) and run `./scripts/sync-plugin-scripts.sh`.
6. Add it to the `plugins` array in `scripts/sync-plugin-scripts.sh`.
7. Run `./scripts/validate.py` and fix what it reports.
8. Update the matrix above, the table in `README.md`, and the setup-cost table in `CLAUDE.md`.
