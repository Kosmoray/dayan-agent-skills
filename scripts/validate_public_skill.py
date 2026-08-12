#!/usr/bin/env python3
"""Validate a public Dayan Skill bundle and its starter contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"dayan-[a-z0-9-]+$")
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")
REQUIRED = {"schema_version", "skill", "input", "output", "checks", "stop_conditions"}


def verify(skill_name: str) -> list[str]:
    errors: list[str] = []
    if not NAME.fullmatch(skill_name):
        return ["skill name must match dayan-[a-z0-9-]+"]
    root = ROOT / "skills" / skill_name
    required_files = ["SKILL.md", "PROVENANCE.md", "SANITIZATION.md", "examples/starter.json"]
    errors.extend(f"missing {item}" for item in required_files if not (root / item).is_file())
    if errors:
        return errors

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        errors.append("SKILL.md is missing frontmatter")
    if not re.search(rf"^name:\s*{re.escape(skill_name)}$", skill_text, re.M):
        errors.append("frontmatter name does not match directory")
    if not re.search(r"^description:\s*.+$", skill_text, re.M):
        errors.append("frontmatter description is missing")

    try:
        payload = json.loads((root / "examples/starter.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return errors + [f"starter.json cannot be parsed: {exc}"]
    if not isinstance(payload, dict):
        return errors + ["starter.json must be an object"]
    missing = REQUIRED - payload.keys()
    if missing:
        errors.append(f"starter.json missing fields: {', '.join(sorted(missing))}")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if payload.get("skill") != skill_name:
        errors.append("starter skill does not match directory")
    for field in ("input", "output"):
        if not isinstance(payload.get(field), dict) or not payload[field]:
            errors.append(f"{field} must be a non-empty object")
    for field in ("checks", "stop_conditions"):
        value = payload.get(field)
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{field} must be a non-empty list of strings")

    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        text = path.read_text(encoding="utf-8")
        if PRIVATE.search(text):
            errors.append(f"private path in {path.relative_to(root)}")
        if SECRET.search(text):
            errors.append(f"credential assignment in {path.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill")
    args = parser.parse_args()
    errors = verify(args.skill)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {args.skill} is a complete public Skill bundle")
    return 0


if __name__ == "__main__":
    sys.exit(main())

