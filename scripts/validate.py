#!/usr/bin/env python3
"""Validate the published skill library using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def skill_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        frontmatter = text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError("unterminated YAML frontmatter") from error
    metadata: dict[str, str] = {}
    for line in frontmatter.splitlines():
        key, separator, value = line.partition(":")
        if separator:
            metadata[key.strip()] = value.strip()
    return metadata


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_name = path.parent.name
    try:
        metadata = skill_metadata(path)
    except ValueError as error:
        return [f"{path.relative_to(ROOT)}: {error}"]

    if metadata.get("name") != skill_name:
        errors.append(f"{path.relative_to(ROOT)}: name must be {skill_name!r}")
    if not metadata.get("description"):
        errors.append(f"{path.relative_to(ROOT)}: description is required")

    agent = path.parent / "agents" / "openai.yaml"
    if not agent.is_file():
        errors.append(f"{agent.relative_to(ROOT)}: file is required")
    else:
        agent_text = agent.read_text(encoding="utf-8")
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in agent_text:
                errors.append(f"{agent.relative_to(ROOT)}: missing {field[:-1]}")
        if f"${skill_name}" not in agent_text:
            errors.append(f"{agent.relative_to(ROOT)}: default prompt must name ${skill_name}")
    return errors


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {target!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(ROOT.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("no skill packages found")
    for path in skill_files:
        errors.extend(validate_skill(path))
    for path in sorted(ROOT.rglob("*.md")):
        errors.extend(validate_links(path))
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {error}")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_files)} skills, local Markdown links, and JSON files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
