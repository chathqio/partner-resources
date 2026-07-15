# Artifact Rendering - the niche package as a native Artifact

This is the standard for turning an approved contextualize package into a
**visual, self-contained HTML artifact**. It runs as the last stage of
`tasks/contextualize-offer.md`, after the markdown package is written and has
passed `checklists/offer-quality.md`. The markdown file is always the source of
truth; the artifact is the same content in a shippable visual form.

The design is a faithful port of Extendly's Offer Package Viewer: a light "paper
document" with a navy cover, a scroll-spy section rail, a 7-pillar scorecard, and
copy-to-clipboard on every deployable asset. It is deliberately single-theme (an
offer package reads as a printed sheet), so it keeps the light look even when the
viewer is in dark mode.

## What you produce

One self-contained HTML document rendered from
`templates/offer-package-artifact.html`, delivered one of two ways:

1. **Native Artifact (preferred).** Publish with the `Artifact` tool. It renders
   on claude.ai / artifact-capable clients and returns a private URL.
2. **Self-contained `.html` file (fallback).** When the `Artifact` tool is not
   available in the current client, write the same document to a file next to the
   markdown so it opens in any browser.

## The one hard constraint: no external hosts

A native Artifact runs under a strict Content Security Policy that **blocks every
external host** - CDN scripts, external stylesheets, webfonts, remote images, and
all `fetch`/`XHR`/WebSocket. Everything must be inline. This is why the skill does
**not** ship the React app: the app loads React, Babel, Font Awesome, and Raleway
from CDNs, none of which resolve inside an Artifact.

The template is already CSP-clean. Keep it that way:

- **Icons** are the inline `<svg><symbol>` library at the top of the template,
  used via `<svg class="ic"><use href="#i-name"/></svg>`. Need an icon that is not
  defined? Add a new `<symbol>` to the `<defs>` block. Never link Font Awesome or
  any icon CDN. Line icons use `class="ic"`; solid ones use `class="ic solid"`.
- **Fonts** fall back to the system stack (Raleway is named first and simply used
  if the viewer has it). Do not add a Google Fonts `<link>` or `@import`.
- **The brand mark** is a base64 data URI in the `--mk` CSS variable. Do not point
  it at a file path or URL.
- **No `<script src>`, no `<link href>`, no remote `url()`.** If you are tempted to
  fetch anything, inline it instead.

## Procedure

### Step 1 - Fill the template

Copy `templates/offer-package-artifact.html` and replace **only the human-readable
content** inside each `<!-- ===== SECTION ===== -->` region with the approved
package content. Leave the `<style>`, the `<svg><defs>` icon library, and the
`<script>` at the end untouched.

Prefer copying the file and editing it region by region (reliable) over
regenerating the whole document from scratch (error-prone). The sample content in
the template is a worked example of the expected shape and voice - overwrite it.

Add or remove repeatable units to match the real package; do not preserve the
sample counts. Freely repeatable: `.prof-chip`, `.comm-chip`, `.search-chip`,
`.alt-row`, `.vocab-chip`, `.sb-stat` (the stat grid auto-fits any count),
`.fitd-story p`, `.fitd-hook` (5-10), `.fitd-lp-block`, `.fitd-notes li`.
**Fixed counts** (do not change): `.fitd-fact` = 3, `.fitd-secret` = 3,
`.fitd-pillar` = 7. **The cover glance strip** (`.fitd-glance`) is a fixed 4-cell
summary (verdict, one money stat, the price band, an assets tally); keep all four
cells or delete the whole `<div class="fitd-glance">` block - do not add or drop
individual cells (the responsive borders assume four).

**Copy buttons need no separate text.** Each `.fitd-copy` button reads the visible
asset next to it (`.h-text`, `.sc-body`, `.lp-text`), so editing the shown copy is
the only step - there is no `data-copy` attribute to keep in sync.

**The story** (`.fitd-story p`): the **first** paragraph always gets the drop cap,
so lead with the backstory beat. Add `class="epiphany"` to the single paragraph
that **is** the epiphany realization, wherever it falls (not a fixed position).

House rules carry through: **no em dashes**, the niche's own vocabulary, and the
**attraction hook** (cover hookbar + ad hooks) kept distinct from the **call hook**
(pillar 2 detail).

### Step 2 - Set the identity fields

- `<title>` -> `FITD Offer Package · {Offer Name} × {Niche}` (middot separator, a
  real `×`). This becomes the artifact / browser-tab name.
- The cover niche paragraph (`.fitd-cover-niche`), offer name (gradient
  `.fitd-cover-offer`), one-liner (`.fitd-cover-oneliner`), the one belief, the
  attraction hook, the cover tag, the rail title, and the doc footer all get this
  package's values. Do not leave sample text in any of them.
- When you publish, use favicon `🎯`, and a one-line description naming the offer
  and niche.

### Step 3 - Deliver

**If the `Artifact` tool is available:** write the filled document to a working
file (e.g. the output folder or a temp path) and publish it with `Artifact`
(`favicon: "🎯"`). Give the user the returned URL and note it is private until they
share it from the artifact's own menu. Keep the `<title>` and favicon stable if you
later republish the same package.

**If the `Artifact` tool is NOT available:** wrap the filled document in the shell
below and write it to `{same-folder-as-markdown}/{niche-slug}.html`. Tell the user
the path and that it opens in any browser offline.

Move the template's leading `<title>` up into `<head>` so the browser tab shows the
offer name (a `<title>` left in `<body>` is invalid and ignored). The `<style>`,
markup, and `<script>` stay in `<body>`:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>FITD Offer Package · {Offer Name} × {Niche}</title>
</head>
<body>
<!-- the filled template's <style>, markup, and <script> go here (title moved above) -->
</body>
</html>
```

When **publishing** as a native Artifact instead, do **not** add this wrapper: pass
the template as-is (its leading `<title>` and inline `<style>`/`<script>` are fine),
and the Artifact tool adds its own `<!doctype>/<head>/<body>` skeleton at publish
time.

## Data -> section mapping

The artifact mirrors the markdown package section for section.

| Package (`niche-offer-package.md`) | Artifact region | Notes |
|---|---|---|
| §0 Snapshot | `#snapshot` cover | niche paragraph; offer name in gradient text; the offer one-liner under it; the one belief on the yellow rule; attraction hook in the hookbar; the fixed 4-cell at-a-glance strip (or omit it) |
| §1 Niche definition | `#niche` | customer summary + attribute chips; communities + search chips; alternatives table; vocabulary phrase bank; dollars-at-stake stat band |
| §2 The one problem | `#problem` | the pull-quote + the three fact cards (close-to-money, verifiable, price-fit) |
| §3 Narrative | `#narrative` | new opportunity, new vehicle, big domino, the epiphany-bridge story (mark the epiphany beat), the 3 secrets |
| §4 The 7 pillars | `#scorecard` | verdict banner + the 7-pillar table with pass / needs-work badges |
| §5 Deployable assets | `#assets` | 5a ad hooks (angle-tagged, copyable), 5b VSL script (copyable), 5c landing-page blocks (copyable), 5d AI Studio brief (the `.fitd-brief` `<pre>`, copyable) |
| Build notes | `#notes` | the footnote list |

**§5d AI Studio brief.** The artifact carries the **truncated** Build-mode prompt
(see `frameworks/ai-studio-brief.md`); the **full** brief (Build prompt + Assist map
+ checklist) lives in the markdown package's §5d. Fill the `.br-body` `<pre>` with
the condensed prompt. **Every line must start at column 0** with no HTML-source
indentation - a `<pre>` renders leading spaces verbatim, so an indented block looks
wrong on the page. Use ASCII `->`, not em dashes. Its Copy button reads the block
automatically (no separate copy string) and dedents, so the pasted prompt stays
clean even if the source was indented - but the on-page render still needs column-0
lines.

The rail nav, the scroll-spy, and the mobile contents sheet are wired by the
template's `<script>`; the section `id`s above must stay as written for them to work.

## Rendering a failing pillar

The template ships all-pass. When a pillar does not pass (a §4 `n`, carried from
the quality checklist), the verdict shows in **six** places - change all of them so
the document does not contradict itself. Use one phrasing everywhere:
`{passing} of 7 pillars pass`.

1. **The pillar row** - add `fail` to its class: `<div class="fitd-pillar fail">`.
2. **The badge** - swap to `<span class="fitd-badge fail"><svg class="ic"><use
   href="#i-warning"/></svg>Needs work</span>`.
3. **The flag note** - add, inside the pillar's text column, a
   `<div class="p-flag"><svg class="ic"><use href="#i-flag"/></svg><span>reason
   this pillar fails and what is needed</span></div>`.
4. **The verdict banner** (`#scorecard`) - switch `fitd-verdict pass` to
   `fitd-verdict flag`, its icon `<use>` to `#i-warning`, the count to
   `N of 7 pillars pass`, and the sub to the honest verdict line.
5. **The rail chip** - switch `fitd-verdict-chip pass` to `flag`, its icon to
   `#i-warning`, and the value to `N of 7 pillars pass`.
6. **The cover glance cell** (`#snapshot`) - the Verdict `.g-val` reads
   `N of 7 pillars pass` and, when not all pass, **drop its `pass` class** (that
   class paints it green). Otherwise the cover claims success the scorecard denies.

`#i-warning` and `#i-flag` are already defined in the icon library for this.

## Acceptance

- [ ] Rendered from the template; `<style>` / `<defs>` / `<script>` untouched
- [ ] Zero external hosts (no CDN, webfont, remote image, or fetch)
- [ ] All content is the approved package; no sample (lawn/landscape) text left in any field
- [ ] In the niche's vocabulary, no em dashes; attraction hook distinct from the call hook
- [ ] Scorecard visual matches the real pass/fail (failing pillars use the flag variant)
- [ ] The verdict reads the same in all six surfaces (rail chip, banner, glance cell, and each pillar); the glance cell is not green unless all pass
- [ ] The one epiphany paragraph carries `class="epiphany"`; the first story paragraph is the backstory (it gets the drop cap)
- [ ] §5d brief holds the truncated Build-mode prompt (flush-left `<pre>`, ASCII arrows, no em dashes), consistent with the markdown §5d and §5c copy
- [ ] Delivered as a native Artifact, or as the wrapped `.html` fallback file (title in `<head>`)
- [ ] The section `id`s are intact so the rail, scroll-spy, and mobile sheet work
