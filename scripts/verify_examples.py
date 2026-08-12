#!/usr/bin/env python3
"""Verify public example-run markdown stays complete, linked, and sanitized."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_DIR = ROOT / "examples" / "runs"
REQUIRED_HEADINGS = (
    "## User input",
    "## Skill to try",
    "## Expected direction",
    "## What to verify",
)
REDLINES = {
    "private path": re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|/Desktop/"),
    "credential marker": re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]"),
    "private key": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
}


def verify_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# Example run: "):
        errors.append(f"{path.relative_to(ROOT)} must start with '# Example run: '")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{path.relative_to(ROOT)} missing {heading}")
    if "```" not in text:
        errors.append(f"{path.relative_to(ROOT)} needs at least one fenced block")
    if not re.search(r"`dayan-[a-z0-9-]+`", text):
        errors.append(f"{path.relative_to(ROOT)} must name one public Skill in backticks")
    for label, pattern in REDLINES.items():
        if pattern.search(text):
            errors.append(f"{label} in {path.relative_to(ROOT)}")
    return errors


def verify_index(files: list[Path]) -> list[str]:
    errors: list[str] = []
    index = EXAMPLE_DIR / "README.md"
    text = index.read_text(encoding="utf-8")
    for path in files:
        if path.name == "README.md":
            continue
        if f"]({path.name})" not in text:
            errors.append(f"examples/runs/README.md does not link {path.name}")
    return errors


def main() -> int:
    files = sorted(EXAMPLE_DIR.glob("*.md"))
    errors: list[str] = []
    if len([path for path in files if path.name != "README.md"]) < 10:
        errors.append("expected at least 10 public example runs")
    for path in files:
        if path.name != "README.md":
            errors.extend(verify_file(path))
    errors.extend(verify_index(files))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(files) - 1} public example runs are complete and sanitized")
    return 0


if __name__ == "__main__":
    sys.exit(main())
