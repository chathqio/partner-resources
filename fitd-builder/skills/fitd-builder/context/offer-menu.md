# Offer menu resolution + output path

This file tells the skill **where the offer menu comes from** and **where the
hydrated package goes**. It carries no offer data itself - the data lives in
`offers.yaml` (resolved below).

## The offer menu

The list of buildable FITD offers is a data-only YAML file. The skill reads it on
**every run** to know which offers are on the menu and to seed the chosen offer's
mechanics. Each offer record carries: `id`, `name`, `status`, `summary`,
`one_problem`, `one_problem_why`, `target_market` (niche + fits), `proof`, and a
`pillars` block (lead_magnet, intake, training_block, implementation,
test_and_launch, ascension_hook). Schema: see the menu's own README.

### Resolution order (each run, stop at the first that succeeds)

1. **Live (preferred).** `WebFetch` the published menu:
   ```
   https://partner.extendly.com/offeriq/offer_menu/offers.yaml
   ```
   This is the source of truth and is always current; offers can be added or edited
   there without updating this skill.
2. **Local working copy (Extendly-internal only).** If the fetch fails and a local
   `partner/offeriq/offer_menu/offers.yaml` is reachable from the cwd, read that
   (covers pre-deploy edits).
3. **Bundled snapshot (offline fallback).** Read `offer-menu-snapshot.yaml` next to
   this file. It ships with the current offers so the skill always works offline and
   in the distributed plugin (where `partner/offeriq` does not exist).

Tell the user which source you used (live vs. snapshot) so they know whether the menu
is current. Only offers with `status: active` are selectable.

### If the URL ever changes

The live URL above is the single editable constant. If the deployed path changes,
update this one line; nothing else in the skill hardcodes it.

## Output path

The hydrated package is written as one markdown file named after the niche
(kebab-case), e.g. `single-location-med-spas.md`.

- **Default:** `./niche-offers/<niche>.md` (relative to the cwd). Create the folder
  if missing. This keeps the skill identical in every install.
- **Extendly-internal:** point runs at `partner/offeriq/niche_contex/<niche>.md` when
  building for the OfferIQ workspace.

Always confirm the resolved output path with the user before writing.
