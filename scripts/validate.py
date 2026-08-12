#!/usr/bin/env python3
"""Consistency checks for the extendly-partner-resources marketplace.

Run this before committing a version bump or a frontmatter change:

    ./scripts/validate.py

What it enforces:

1. VERSIONS.json, <plugin>/.claude-plugin/plugin.json, and the skill's metadata.version all
   agree. The self-update hook compares plugin.json against VERSIONS.json, so a mismatch
   means partners are told to update to a version that installs as something else.
2. marketplace.json and VERSIONS.json list the same plugins.
3. Any skill declared claude.ai-capable uses only the six frontmatter fields the Agent Skills
   spec allows. claude.ai uploads, the Skills API, and package_skill.py reject anything else
   with a hard error, which is exactly the failure this repo shipped before. CLI-only skills
   get a warning instead, since they may legitimately use Claude Code-only fields.
4. Every plugin wires the update hook and ships an executable copy of the check script.

Frontmatter is parsed with a small line reader rather than PyYAML so this stays dependency
free. That is adequate for these files: flat keys, one nested metadata block.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The Agent Skills spec fields. Anything else fails a claude.ai upload outright.
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:")
NESTED_RE = re.compile(r"^\s+([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$")

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"FAIL  {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"WARN  {msg}")


def ok(msg: str) -> None:
    print(f"ok    {msg}")


def load_json(path: str):
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"missing {os.path.relpath(path, REPO)}")
    except json.JSONDecodeError as exc:
        fail(f"{os.path.relpath(path, REPO)} is not valid JSON: {exc}")
    return None


def read_frontmatter(path: str) -> tuple[list[str], dict[str, str]]:
    """Return (top-level keys in order, flattened metadata block)."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{os.path.relpath(path, REPO)} has no YAML frontmatter")
        return [], {}
    keys: list[str] = []
    metadata: dict[str, str] = {}
    in_metadata = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = KEY_RE.match(line)
        if match:
            key = match.group(1)
            keys.append(key)
            in_metadata = key == "metadata"
            continue
        if in_metadata:
            nested = NESTED_RE.match(line)
            if nested:
                metadata[nested.group(1)] = nested.group(2).strip().strip("\"'")
    return keys, metadata


def main() -> int:
    versions = load_json(os.path.join(REPO, "VERSIONS.json"))
    marketplace = load_json(os.path.join(REPO, ".claude-plugin", "marketplace.json"))
    if versions is None or marketplace is None:
        return 1

    declared = versions.get("plugins", {})
    listed = {entry["name"] for entry in marketplace.get("plugins", [])}

    if set(declared) != listed:
        fail(
            "marketplace.json and VERSIONS.json disagree on which plugins exist: "
            f"marketplace={sorted(listed)} versions={sorted(declared)}"
        )
    else:
        ok(f"plugin sets agree ({', '.join(sorted(declared))})")

    for name, spec in sorted(declared.items()):
        expected = spec.get("version")
        platforms = spec.get("platforms", [])
        web_capable = "claude-ai" in platforms

        manifest_path = os.path.join(REPO, name, ".claude-plugin", "plugin.json")
        manifest = load_json(manifest_path)
        if manifest is not None:
            if manifest.get("version") != expected:
                fail(
                    f"{name}: plugin.json version {manifest.get('version')!r} "
                    f"!= VERSIONS.json {expected!r}"
                )
            else:
                ok(f"{name}: plugin.json version {expected}")

        skill_dir = spec.get("skill")
        skill_path = os.path.join(REPO, skill_dir, "SKILL.md") if skill_dir else None
        if not skill_path or not os.path.isfile(skill_path):
            fail(f"{name}: no SKILL.md at {skill_dir}")
        else:
            keys, metadata = read_frontmatter(skill_path)
            rel = os.path.relpath(skill_path, REPO)

            if metadata.get("version") != expected:
                fail(
                    f"{name}: {rel} metadata.version {metadata.get('version')!r} "
                    f"!= VERSIONS.json {expected!r}"
                )
            else:
                ok(f"{name}: SKILL.md metadata.version {expected}")

            offenders = [key for key in keys if key not in SPEC_FIELDS]
            if offenders:
                detail = (
                    f"{name}: {rel} frontmatter has non-spec field(s) {offenders}. "
                    f"Allowed: {sorted(SPEC_FIELDS)}"
                )
                if web_capable:
                    fail(detail + " - a claude.ai upload of this skill fails with an "
                                  "'Unexpected key(s) in SKILL.md frontmatter' error")
                else:
                    warn(detail + " - fine for a CLI-only skill, but it cannot be "
                                  "uploaded to claude.ai as is")
            else:
                ok(f"{name}: SKILL.md frontmatter is spec-compliant")

            if web_capable and "compatibility" not in keys:
                warn(f"{name}: {rel} is claude.ai-capable but declares no `compatibility` field")

        hooks_path = os.path.join(REPO, name, "hooks", "hooks.json")
        hooks = load_json(hooks_path)
        if hooks is not None:
            if "check-update.sh" not in json.dumps(hooks):
                fail(f"{name}: hooks/hooks.json does not wire check-update.sh")
            else:
                ok(f"{name}: update hook wired")

        script = os.path.join(REPO, name, "scripts", "check-update.sh")
        if not os.path.isfile(script):
            fail(f"{name}: missing scripts/check-update.sh (run ./scripts/sync-plugin-scripts.sh)")
        elif not os.access(script, os.X_OK):
            fail(f"{name}: scripts/check-update.sh is not executable, so its hooks never fire")
        else:
            ok(f"{name}: check-update.sh present and executable")

    sync = subprocess.run(
        [os.path.join(REPO, "scripts", "sync-plugin-scripts.sh"), "--check"],
        capture_output=True,
        text=True,
    )
    if sync.returncode != 0:
        fail("plugin copies of check-update.sh are out of sync:\n" + sync.stdout.strip())
    else:
        ok("plugin copies of check-update.sh match the canonical script")

    print()
    if failures:
        print(f"{len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1
    print(f"all checks passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
