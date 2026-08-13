#!/usr/bin/env python3
"""Verify the public positioning page explains the control-library claim."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "control-layer-vs-prompt-collection.md"
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")
REQUIRED_PHRASES = (
    "not a prompt collection",
    "public control library",
    "Skill",
    "Method",
    "Fixture",
    "Verifier",
    "Evidence boundary",
    "does not claim",
    "one repository",
)


def verify() -> list[str]:
    if not DOC.is_file():
        return ["missing docs/control-layer-vs-prompt-collection.md"]
    text = DOC.read_text(encoding="utf-8")
    errors: list[str] = []
    lowered = text.lower()
    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            errors.append(f"positioning page missing required phrase: {phrase}")
    if text.count("|") < 20:
        errors.append("positioning page must include a comparison table")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (DOC.parent / local_target).exists():
            errors.append(f"broken local link: {target}")
    if PRIVATE.search(text):
        errors.append("positioning page contains a private path pattern")
    if SECRET.search(text):
        errors.append("positioning page contains a credential-like assignment")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: public positioning page explains the control-library boundary")
    return 0


if __name__ == "__main__":
    sys.exit(main())
