#!/usr/bin/env python3
"""Verify the public tooling catalog is complete and bounded."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "tooling.md"
ROW = re.compile(r"^\| `([^`]+)` \| ([^|]+) \| `([^`]+)` \| ([^|]+) \| ([^|]+) \|$")
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")


def verify() -> list[str]:
    if not DOC.is_file():
        return ["missing docs/tooling.md"]
    text = DOC.read_text(encoding="utf-8")
    errors: list[str] = []
    if PRIVATE.search(text):
        errors.append("tooling catalog contains a private path pattern")
    if SECRET.search(text):
        errors.append("tooling catalog contains a credential-like assignment")
    rows = [match for line in text.splitlines() if (match := ROW.match(line))]
    if len(rows) < 12:
        errors.append("at least twelve public tools must be documented")
    seen: set[str] = set()
    for match in rows:
        tool, purpose, command, proves, non_claim = match.groups()
        if tool in seen:
            errors.append(f"duplicate tool row: {tool}")
        seen.add(tool)
        if not (ROOT / tool).is_file():
            errors.append(f"documented tool does not exist: {tool}")
        if "python3" not in command:
            errors.append(f"{tool} command must be directly runnable with python3")
        if len(purpose.strip()) < 12:
            errors.append(f"{tool} purpose is too vague")
        if len(proves.strip()) < 12:
            errors.append(f"{tool} proof claim is too vague")
        if len(non_claim.strip()) < 8:
            errors.append(f"{tool} non-claim is too vague")
    for required in ("must not write to a user's live home", "what it proves", "what it does not prove"):
        if required not in text:
            errors.append(f"tooling catalog missing rule: {required}")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len([line for line in DOC.read_text(encoding='utf-8').splitlines() if line.startswith('| `')])} public tools are documented")
    return 0


if __name__ == "__main__":
    sys.exit(main())
