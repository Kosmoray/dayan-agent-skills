#!/usr/bin/env python3
"""Verify public method cards are linked, bounded, and sanitized."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "methods.md"
METHOD_DIR = ROOT / "docs" / "methods"
FIXTURE_DIR = ROOT / "docs" / "fixtures"
REQUIRED_SECTIONS = ("## Principle", "## Apply it", "## Failure pattern", "## Public status")
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")
PROMOTED = {
    "tool-before-agent.md": "tool-before-agent-verifier-plan.md",
    "false-positive-control.md": "false-positive-control-review.md",
    "human-authority-ledger.md": "human-authority-ledger.md",
}


def linked_methods(index_text: str) -> set[str]:
    return {
        target.rsplit("/", 1)[-1]
        for target in re.findall(r"\[[^\]]+\]\((methods/[^)]+\.md)\)", index_text)
    }


def verify() -> list[str]:
    errors: list[str] = []
    if not INDEX.is_file():
        return ["missing docs/methods.md"]
    index_text = INDEX.read_text(encoding="utf-8")
    method_files = sorted(METHOD_DIR.glob("*.md"))
    if len(method_files) < 15:
        errors.append("at least fifteen public method cards are required")
    linked = linked_methods(index_text)
    if "fifteen" not in index_text.lower() and "15" not in index_text:
        errors.append("method index must state the current method-card count")
    for path in method_files:
        text = path.read_text(encoding="utf-8")
        if path.name not in linked:
            errors.append(f"{path.name} is not linked from docs/methods.md")
        if not text.startswith("# "):
            errors.append(f"{path.name} must start with a top-level heading")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{path.name} missing {section}")
        if "not a claim" not in text and "not legal advice" not in text:
            errors.append(f"{path.name} must include a public non-claim boundary")
        if PRIVATE.search(text):
            errors.append(f"{path.name} contains a private path pattern")
        if SECRET.search(text):
            errors.append(f"{path.name} contains a credential-like assignment")
    for method_name, fixture_name in PROMOTED.items():
        if method_name not in linked:
            errors.append(f"promoted method is not linked: {method_name}")
        if not (FIXTURE_DIR / fixture_name).is_file():
            errors.append(f"promoted method fixture is missing: {fixture_name}")
    missing_links = linked - {path.name for path in method_files}
    for missing in sorted(missing_links):
        errors.append(f"method index links missing card: {missing}")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(list(METHOD_DIR.glob('*.md')))} public method cards are linked and bounded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
