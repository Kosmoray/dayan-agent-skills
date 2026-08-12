#!/usr/bin/env python3
"""Verify public artifact fixtures are complete, linked, and sanitized."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "docs" / "fixtures"
REQUIRED_SECTIONS = ("Skill:", "## Input", "## Output artifact", "## Verification", "## Boundary")
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")
SKILL = re.compile(r"^Skill:\s*`(dayan-[a-z0-9-]+)`$", re.MULTILINE)


def linked_fixtures(readme: str) -> set[str]:
    return {
        target
        for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", readme)
        if target != "README.md"
    }


def verify() -> list[str]:
    errors: list[str] = []
    readme = FIXTURE_DIR / "README.md"
    if not readme.is_file():
        return ["missing docs/fixtures/README.md"]
    readme_text = readme.read_text(encoding="utf-8")
    fixtures = sorted(path for path in FIXTURE_DIR.glob("*.md") if path.name != "README.md")
    if len(fixtures) < 5:
        errors.append("at least five public artifact fixtures are required")
    linked = linked_fixtures(readme_text)
    for path in fixtures:
        relative_name = path.name
        text = path.read_text(encoding="utf-8")
        if relative_name not in linked:
            errors.append(f"{relative_name} is not linked from docs/fixtures/README.md")
        if not text.startswith("# "):
            errors.append(f"{relative_name} must start with a top-level heading")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{relative_name} missing {section}")
        match = SKILL.search(text)
        if not match:
            errors.append(f"{relative_name} missing public Skill marker")
        elif not (ROOT / "skills" / match.group(1) / "SKILL.md").is_file():
            errors.append(f"{relative_name} references unknown Skill {match.group(1)}")
        if PRIVATE.search(text):
            errors.append(f"{relative_name} contains a private path pattern")
        if SECRET.search(text):
            errors.append(f"{relative_name} contains a credential-like assignment")
        if "does not prove" not in text and "does not guarantee" not in text:
            errors.append(f"{relative_name} must state a non-claim boundary")
    missing_links = linked - {path.name for path in fixtures}
    for missing in sorted(missing_links):
        errors.append(f"README links missing fixture: {missing}")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len([p for p in FIXTURE_DIR.glob('*.md') if p.name != 'README.md'])} artifact fixtures are complete and sanitized")
    return 0


if __name__ == "__main__":
    sys.exit(main())
