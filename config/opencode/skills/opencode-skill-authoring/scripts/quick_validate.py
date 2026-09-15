#!/usr/bin/env python3
"""Structural validator for OpenCode skills.

This helper validates only the selected contract's static requirements. It does
not prove OpenCode discovery, effective permissions, skill loading, reference
loading, or behavior.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

V1_ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
V2_KNOWN = {"name", "description", "slash", "metadata", "license", "compatibility"}
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.DOTALL)


def parse_frontmatter(skill_md: Path) -> tuple[dict | None, str | None]:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return None, None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in frontmatter: {exc}") from exc
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a YAML mapping")
    return data, match.group(1)


def validate_description(value: object, required: bool) -> list[str]:
    errors: list[str] = []
    if value is None:
        if required:
            errors.append("Missing 'description' in frontmatter")
        return errors
    if not isinstance(value, str):
        return [f"Description must be a string, got {type(value).__name__}"]
    description = value.strip()
    if required and not description:
        errors.append("Description must not be empty")
    if "<" in description or ">" in description:
        errors.append("Description cannot contain angle brackets (< or >)")
    if len(description) > 1024:
        errors.append(f"Description is too long ({len(description)} characters); maximum is 1024")
    return errors


def validate_legacy_v1(skill_dir: Path, frontmatter: dict | None) -> list[str]:
    if frontmatter is None:
        return ["Legacy V1 contract requires YAML frontmatter"]

    errors: list[str] = []
    unexpected = set(frontmatter) - V1_ALLOWED
    if unexpected:
        errors.append(
            "Unexpected V1 frontmatter key(s): "
            + ", ".join(sorted(unexpected))
            + "; verify target support before adding them"
        )

    name = frontmatter.get("name")
    if name is None:
        errors.append("Missing 'name' in frontmatter")
    elif not isinstance(name, str):
        errors.append(f"Name must be a string, got {type(name).__name__}")
    else:
        name = name.strip()
        if not name:
            errors.append("Name must not be empty")
        elif not KEBAB.fullmatch(name):
            errors.append(f"Name '{name}' must use lowercase kebab-case")
        elif len(name) > 64:
            errors.append(f"Name is too long ({len(name)} characters); maximum is 64")
        if name and name != skill_dir.name:
            errors.append(
                f"Name '{name}' does not match directory '{skill_dir.name}' for the maintained V1 convention"
            )

    errors.extend(validate_description(frontmatter.get("description"), required=True))
    return errors


def validate_v2(skill_dir: Path, frontmatter: dict | None) -> list[str]:
    errors: list[str] = []
    # Current upstream V2 permits frontmatter to be absent. Directory-form skills
    # still derive their runtime ID from the path.
    if not KEBAB.fullmatch(skill_dir.name):
        errors.append(
            f"Directory ID '{skill_dir.name}' should use lowercase kebab-case for a portable V2 skill"
        )
    if len(skill_dir.name) > 64:
        errors.append(
            f"Directory ID is too long ({len(skill_dir.name)} characters); keep portable IDs at 64 or fewer"
        )

    if frontmatter is None:
        return errors

    name = frontmatter.get("name")
    if name is not None and not isinstance(name, str):
        errors.append(f"Display name must be a string, got {type(name).__name__}")
    description = frontmatter.get("description")
    errors.extend(validate_description(description, required=False))

    slash = frontmatter.get("slash")
    if slash is not None and not isinstance(slash, bool):
        errors.append(f"'slash' must be boolean when present, got {type(slash).__name__}")

    metadata = frontmatter.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        errors.append(f"'metadata' must be a mapping when present, got {type(metadata).__name__}")

    # Unknown fields are not rejected here. V2 and portability metadata can
    # evolve; target-runtime evidence remains authoritative.
    _ = set(frontmatter) - V2_KNOWN
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory", type=Path)
    parser.add_argument("--contract", choices=("legacy-v1", "v2"), required=True)
    args = parser.parse_args()

    skill_dir = args.skill_directory.resolve()
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        print("ERROR: SKILL.md not found")
        return 1

    try:
        frontmatter, _ = parse_frontmatter(skill_md)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    errors = (
        validate_legacy_v1(skill_dir, frontmatter)
        if args.contract == "legacy-v1"
        else validate_v2(skill_dir, frontmatter)
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"PASS: static {args.contract} skill structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
