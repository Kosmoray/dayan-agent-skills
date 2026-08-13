#!/usr/bin/env python3
"""Verify the one-screen control-library positioning demo."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "docs" / "demos" / "control-library.html"
REQUIRED = (
    "<title>",
    '<meta name="viewport"',
    "<main",
    "prefers-reduced-motion",
    "Not a prompt collection",
    "Control library",
    "Prompts say what to ask",
    "Control layers say what must be true",
    "Skill",
    "Fixture",
    "Verifier",
    "112/112",
    "does not claim",
)
REDLINE = re.compile(r"(?:/Users|/home)/|/Desktop/|API_KEY|PRIVATE KEY", re.I)


def verify() -> list[str]:
    if not DEMO.is_file():
        return ["missing docs/demos/control-library.html"]
    text = DEMO.read_text(encoding="utf-8")
    errors: list[str] = []
    for token in REQUIRED:
        if token not in text:
            errors.append(f"control demo missing {token}")
    if text.count("class=\"item\"") < 6:
        errors.append("control demo must show at least six comparison items")
    if text.count("class=\"proof\"") != 1:
        errors.append("control demo must include exactly one proof strip")
    if REDLINE.search(text):
        errors.append("control demo contains public redline")
    for target in re.findall(r'(?:href|src)="([^"]+)"', text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local = (DEMO.parent / target.split("#", 1)[0]).resolve()
        if target and not local.exists():
            errors.append(f"control demo broken link {target}")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: control-library demo is one-screen, linked, and bounded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
