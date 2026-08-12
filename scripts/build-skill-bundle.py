#!/usr/bin/env python3
"""Package a claude.ai-capable skill for upload to claude.ai.

    ./scripts/build-skill-bundle.py fitd-builder
    ./scripts/build-skill-bundle.py --list

Writes dist/<skill>-<version>.zip containing a single top-level folder with SKILL.md at its
root, which is the layout claude.ai's skill upload expects. dist/ is gitignored: the bundle
is generated from the plugin's own skill directory, so there is never a second copy of the
skill content in this repo to drift.

The skill directory is the bundle. Nothing is rewritten on the way out, which is only
possible because claude.ai-capable skills in this repo keep their frontmatter inside the six
fields the Agent Skills spec allows. This script refuses to build if that is not true, since
claude.ai would reject the upload with a hard error anyway.

Plugin scaffolding (commands/, hooks/, .claude-plugin/) lives outside the skill directory and
is therefore never in the bundle. See PLATFORMS.md for what that costs you on claude.ai.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:")

# Never ship editor droppings, caches, or the hook's throttle stamp.
EXCLUDE_DIRS = {".git", "__pycache__", ".cache", "node_modules", ".venv"}
EXCLUDE_FILES = {".DS_Store", "update-check.stamp"}


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def load_versions() -> dict:
    with open(os.path.join(REPO, "VERSIONS.json"), encoding="utf-8") as handle:
        return json.load(handle)


def frontmatter_keys(path: str) -> list[str]:
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if not lines or lines[0].strip() != "---":
        die(f"{path} has no YAML frontmatter")
    keys = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = KEY_RE.match(line)
        if match:
            keys.append(match.group(1))
    return keys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", nargs="?", help="plugin/skill name, e.g. fitd-builder")
    parser.add_argument("--list", action="store_true", help="show which skills can be bundled")
    args = parser.parse_args()

    versions = load_versions()
    plugins = versions.get("plugins", {})

    if args.list or not args.skill:
        print("claude.ai-capable skills in this marketplace:\n")
        for name, spec in sorted(plugins.items()):
            web = "claude-ai" in spec.get("platforms", [])
            mark = "yes" if web else "no "
            print(f"  [{mark}] {name} {spec.get('version', '?')}")
            if not web:
                print(f"         {spec.get('notes', '').strip()}")
        if not args.skill:
            print("\nusage: ./scripts/build-skill-bundle.py <skill>")
        return 0

    spec = plugins.get(args.skill)
    if spec is None:
        die(f"unknown skill {args.skill!r}. Known: {', '.join(sorted(plugins))}")

    if "claude-ai" not in spec.get("platforms", []):
        die(
            f"{args.skill} is not claude.ai-capable, so there is nothing useful to upload.\n"
            f"  reason: {spec.get('notes', '').strip()}"
        )

    version = spec["version"]
    skill_dir = os.path.join(REPO, spec["skill"])
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        die(f"no SKILL.md at {spec['skill']}")

    offenders = [key for key in frontmatter_keys(skill_md) if key not in SPEC_FIELDS]
    if offenders:
        die(
            f"{spec['skill']}/SKILL.md frontmatter has non-spec field(s) {offenders}.\n"
            f"  claude.ai would reject this upload outright. Allowed fields: "
            f"{sorted(SPEC_FIELDS)}\n"
            f"  Move anything else under `metadata:`, which is a free-form map."
        )

    dist = os.path.join(REPO, "dist")
    os.makedirs(dist, exist_ok=True)
    bundle = os.path.join(dist, f"{args.skill}-{version}.zip")

    count = 0
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(skill_dir):
            dirs[:] = sorted(d for d in dirs if d not in EXCLUDE_DIRS)
            for filename in sorted(files):
                if filename in EXCLUDE_FILES:
                    continue
                absolute = os.path.join(root, filename)
                relative = os.path.relpath(absolute, skill_dir)
                archive.write(absolute, os.path.join(args.skill, relative))
                count += 1

    size_kb = os.path.getsize(bundle) / 1024
    print(f"wrote dist/{os.path.basename(bundle)}  ({count} files, {size_kb:.0f} KB)")
    print()
    print("Upload it at claude.ai -> Settings -> Capabilities -> Skills -> Upload skill.")
    print("Once enabled it is available in claude.ai chat, Cowork, and cloud sessions.")
    print("See claude-ai/README.md for the full walkthrough and how to stay current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
