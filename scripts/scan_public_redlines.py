#!/usr/bin/env python3
"""Scan prospective public files for release blockers without printing secret values."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".zip", ".pdf"}
RULES = {
    "private_user_path": re.compile(r"(?:/Users/|/home/)[A-Za-z0-9._-]+/"),
    "credential_assignment": re.compile(
        r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
    ),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "customer_marker": re.compile(r"(?i)(?:customer|client)[_-]?(?:name|id)\s*[:=]"),
    "internal_control_marker": re.compile(r"(?i)(?:internal[_-](?:only|strategy|control)|private[_-]workflow)"),
}


def scan(root: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    if not root.exists():
        return findings
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule_name, pattern in RULES.items():
                if pattern.search(line):
                    findings.append(
                        {
                            "file": str(path.relative_to(root)),
                            "line": line_number,
                            "rule": rule_name,
                        }
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="skills")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    if not root.exists():
        print(f"PASS: {root} does not exist; no public Skill source has been staged")
        return 0
    findings = scan(root)
    if args.json:
        print(json.dumps({"root": str(root), "findings": findings}, indent=2))
    elif findings:
        for item in findings:
            print(f"BLOCK: {item['file']}:{item['line']} [{item['rule']}]")
    else:
        print(f"PASS: no configured public redline matched under {root}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
