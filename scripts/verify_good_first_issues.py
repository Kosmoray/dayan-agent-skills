#!/usr/bin/env python3
"""Verify the public good-first-issue list is actionable and bounded."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "good-first-issues.md"
PRIVATE = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\", re.I)
SECRET = re.compile(r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")


def issue_rows(text: str) -> list[tuple[str, str, str, str, str, str]]:
    rows: list[tuple[str, str, str, str, str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| GFI-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 6:
            rows.append(tuple(cells))  # type: ignore[arg-type]
    return rows


def verify() -> list[str]:
    if not DOC.is_file():
        return ["missing docs/good-first-issues.md"]
    text = DOC.read_text(encoding="utf-8")
    errors: list[str] = []
    if PRIVATE.search(text):
        errors.append("good-first-issues contains a private path pattern")
    if SECRET.search(text):
        errors.append("good-first-issues contains a credential-like assignment")
    rows = issue_rows(text)
    if len(rows) < 8:
        errors.append("at least eight good-first-issue rows are required")
    seen: set[str] = set()
    for issue_id, task, skill, files, proof, size in rows:
        if issue_id in seen:
            errors.append(f"duplicate issue id: {issue_id}")
        seen.add(issue_id)
        if len(task.strip()) < 16:
            errors.append(f"{issue_id} task is too vague")
        if "python3" not in proof:
            errors.append(f"{issue_id} proof must name a python verifier")
        if "<" in files and ">" in files and "docs/fixtures" not in files and "skills/" not in files:
            errors.append(f"{issue_id} placeholder files must point to a public contribution area")
        for skill_name in re.findall(r"`(dayan-[a-z0-9-]+)`", skill):
            if not (ROOT / "skills" / skill_name / "SKILL.md").is_file():
                errors.append(f"{issue_id} references unknown Skill {skill_name}")
        if size not in {"small", "medium"}:
            errors.append(f"{issue_id} size must be small or medium")
    for required in ("Do not include customer data", "what the contribution does not prove", "validate_release.py"):
        if required not in text:
            errors.append(f"good-first-issues missing rule: {required}")
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len([line for line in DOC.read_text(encoding='utf-8').splitlines() if line.startswith('| GFI-')])} good-first issues are actionable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
