# Using these tools on claude.ai

Most of this repo assumes Claude Code in a terminal. You do not need a terminal to use
**fitd-builder**. It runs in claude.ai chat, in Cowork, and in Claude Code on the web.

**monster-meta does not run on claude.ai and never will.** It needs a local MCP server process
and a long-lived Meta access token, neither of which claude.ai skills can carry. If you want
monster-meta, use Claude Code on your own machine and follow
[`monster-meta/ONBOARDING.md`](../monster-meta/ONBOARDING.md). See
[`PLATFORMS.md`](../PLATFORMS.md) for the full reasoning.

Pick the path that matches how you use Claude.

---

## Path A - claude.ai chat, Cowork, or the desktop app

You upload the skill to your claude.ai account once. After that it is available in chat, in
Cowork, and in any cloud session you start.

### The easy way

Open Claude Code in this repo (or a Claude Code cloud session on it) and say:

> **Build me the fitd-builder bundle for claude.ai.**

Claude runs `./scripts/build-skill-bundle.py fitd-builder` and hands you
`dist/fitd-builder-<version>.zip`. Skip to [Upload it](#upload-it).

### The manual way, no terminal

1. In this repo on your computer, open the folder
   **`fitd-builder/skills/fitd-builder/`**.
2. Compress that folder itself, not its contents and not any folder above it.
   - macOS: right-click the `fitd-builder` folder, choose **Compress**
   - Windows: right-click it, choose **Send to > Compressed (zipped) folder**
3. You should end up with a zip whose top level is a single `fitd-builder` folder with
   `SKILL.md` directly inside it. That layout matters.

> Compressing the wrong folder is the single most common mistake here. `fitd-builder/` at the
> repo root is the **plugin**, which contains plugin scaffolding claude.ai cannot read. The
> **skill** is two levels down, at `fitd-builder/skills/fitd-builder/`.

### Upload it

1. Go to [claude.ai](https://claude.ai) and open **Settings > Capabilities > Skills**.
2. Choose **Upload skill** and pick your zip.
3. Enable it.

Then start a new chat and say what you want in plain language:

> Adapt the Speed-to-Lead offer for single-location med spas.

or

> Build me a new foot-in-the-door offer. I do Google Business Profile cleanups for HVAC
> companies.

**There are no slash commands on claude.ai.** `/fitd-builder:contextualize` and friends come
from the plugin's `commands/` folder, which only Claude Code reads. The skill knows this and
routes on what you say instead. The three workflows are the same: contextualize an existing menu
offer, build a new offer from scratch, or just research a niche.

### What is different on claude.ai

| | Claude Code | claude.ai chat / Cowork |
|---|---|---|
| Slash commands | `/fitd-builder:contextualize` | Ask in plain language |
| Visual HTML offer package | Native Artifact | Native Artifact |
| Live offer menu fetch | Yes | Yes, and falls back to the bundled snapshot |
| Where the markdown package lands | A file in your working folder | In the conversation, download it |
| Automatic version updates | Yes | No, see [Staying current](#staying-current) |

---

## Path B - Claude Code on the web, on this repo

Nothing to do. This repo's `.claude/settings.json` declares the marketplace and enables
`fitd-builder`, so a cloud session started on `chathqio/partner-resources` installs it at session
start. Open a session at [claude.ai/code](https://claude.ai/code), pick this repo, and run:

```
/fitd-builder:contextualize single-location med spas + Speed-to-Lead
```

Cloud sessions install the plugin fresh each time, so they are always on the current version.

## Path C - Claude Code on the web, on one of your own repos

Add these two keys to that repository's `.claude/settings.json` and commit them:

```json
{
  "extraKnownMarketplaces": {
    "extendly-partner-resources": {
      "source": {
        "source": "github",
        "repo": "chathqio/partner-resources"
      }
    }
  },
  "enabledPlugins": {
    "fitd-builder@extendly-partner-resources": true
  }
}
```

One caveat worth knowing before you try it: a cloud session's GitHub access is scoped to the
repositories attached to that session. Because `partner-resources` is private, a session on a
different repo may get a 403 fetching the marketplace and the plugin will not install. If that
happens, use Path A instead. An account-level skill upload has no such restriction and works in
every cloud session.

---

## Staying current

This section is about **Path A only**, an uploaded skill used in claude.ai chat or Cowork.

Each plugin checks its own version whenever you use it and updates itself when it is behind. That
check is a plugin hook, so it covers Claude Code on your machine **and Claude Code on the web**:
cloud sessions run hooks from the cloned repo, and Paths B and C install the plugin fresh at
session start anyway. Nothing to do on those paths.

An uploaded skill is different. claude.ai chat and Cowork have no hook system, so the skill cannot
notice that a newer version exists.

To check yours, ask in any claude.ai chat:

> What version of the fitd-builder skill are you running?

Claude reads `metadata.version` out of the skill's own frontmatter. Compare it against
`plugins.fitd-builder.version` in [`VERSIONS.json`](../VERSIONS.json) in this repo. If yours is
older, rebuild the bundle and upload it again, replacing the old skill.

---

## If something breaks

| Symptom | What is wrong |
|---|---|
| `Unexpected key(s) in SKILL.md frontmatter` | You zipped a file that is not from this repo's current version, or edited the frontmatter. claude.ai allows only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Re-pull this repo and rebuild the bundle |
| Upload rejected, or the skill never triggers | Your zip's top level is wrong. It must be one folder containing `SKILL.md`. Compress `fitd-builder/skills/fitd-builder/`, not the plugin folder at the repo root |
| Claude does not use the skill on its own | Name the work: "adapt an offer for &lt;niche&gt;", "build a foot-in-the-door offer". Confirm it is enabled in Settings > Capabilities > Skills |
| Skill runs but says it cannot reach the offer menu | Expected when the live menu is unreachable. It falls back to its bundled snapshot and tells you which source it used |
| You wanted monster-meta on claude.ai | Not possible. Use Claude Code on your machine, see [`PLATFORMS.md`](../PLATFORMS.md) |
