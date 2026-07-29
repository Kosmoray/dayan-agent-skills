#!/usr/bin/env python3
"""Validate a machine-readable adversarial-review verdict."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath

VERDICTS = {"BLOCK", "CONCERNS", "CLEAN"}
SEVERITIES = {"CRITICAL", "WARNING", "NOTE"}
REQUIRED_ROOT = {
    "schema_version",
    "scope",
    "verdict",
    "summary",
    "findings",
    "residual_assumptions",
}
REQUIRED_FINDING = {"severity", "title", "evidence", "risk", "fix"}
REQUIRED_EVIDENCE = {"path", "line", "trigger"}
REQUIRED_ASSUMPTIONS = {"failure_mode", "maintainer", "trust_boundary"}
SENSITIVE_PATTERNS = {
    "private machine path": re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\", re.IGNORECASE),
    "private key": re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY"),
    "credential token": re.compile(
        r"\b(?:gh[opsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,})\b"
    ),
    "credential value": re.compile(
        r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
    ),
}


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def safe_relative_path(value: object) -> bool:
    if not nonempty_string(value):
        return False
    text = str(value)
    path = PurePosixPath(text)
    return not path.is_absolute() and ".." not in path.parts and "\\" not in text


def verify(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot parse review JSON: {exc}"]

    if not isinstance(payload, dict):
        return ["review must be a JSON object"]

    missing = REQUIRED_ROOT - payload.keys()
    if missing:
        errors.append(f"missing root fields: {', '.join(sorted(missing))}")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    for field in ("scope", "summary"):
        if not nonempty_string(payload.get(field)):
            errors.append(f"{field} must be a non-empty string")

    verdict = payload.get("verdict")
    if verdict not in VERDICTS:
        errors.append("verdict must be BLOCK, CONCERNS, or CLEAN")

    findings = payload.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be an array")
        findings = []

    severities: list[str] = []
    titles: set[str] = set()
    for index, finding in enumerate(findings):
        where = f"findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{where} must be an object")
            continue
        missing_finding = REQUIRED_FINDING - finding.keys()
        if missing_finding:
            errors.append(f"{where} missing fields: {', '.join(sorted(missing_finding))}")
        severity = finding.get("severity")
        if severity not in SEVERITIES:
            errors.append(f"{where}.severity is invalid")
        else:
            severities.append(severity)
        for field in ("title", "risk", "fix"):
            if not nonempty_string(finding.get(field)):
                errors.append(f"{where}.{field} must be a non-empty string")
        title = finding.get("title")
        if nonempty_string(title):
            if title in titles:
                errors.append(f"duplicate finding title: {title}")
            titles.add(str(title))

        evidence = finding.get("evidence")
        if not isinstance(evidence, dict):
            errors.append(f"{where}.evidence must be an object")
            continue
        missing_evidence = REQUIRED_EVIDENCE - evidence.keys()
        if missing_evidence:
            errors.append(f"{where}.evidence missing fields: {', '.join(sorted(missing_evidence))}")
        if not safe_relative_path(evidence.get("path")):
            errors.append(f"{where}.evidence.path must be repository-relative")
        line = evidence.get("line")
        if not isinstance(line, int) or isinstance(line, bool) or line < 1:
            errors.append(f"{where}.evidence.line must be a positive integer")
        if not nonempty_string(evidence.get("trigger")):
            errors.append(f"{where}.evidence.trigger must be a non-empty string")

    assumptions = payload.get("residual_assumptions")
    if not isinstance(assumptions, dict):
        errors.append("residual_assumptions must be an object")
    else:
        missing_assumptions = REQUIRED_ASSUMPTIONS - assumptions.keys()
        if missing_assumptions:
            errors.append(
                f"residual_assumptions missing fields: {', '.join(sorted(missing_assumptions))}"
            )
        for field in REQUIRED_ASSUMPTIONS:
            if field in assumptions and not nonempty_string(assumptions[field]):
                errors.append(f"residual_assumptions.{field} must be a non-empty string")

    if "CRITICAL" in severities and verdict != "BLOCK":
        errors.append("a CRITICAL finding requires verdict BLOCK")
    if verdict == "BLOCK" and "CRITICAL" not in severities:
        errors.append("verdict BLOCK requires at least one CRITICAL finding")
    if "CRITICAL" not in severities and "WARNING" in severities and verdict != "CONCERNS":
        errors.append("a WARNING without CRITICAL requires verdict CONCERNS")
    if verdict == "CONCERNS" and ("WARNING" not in severities or "CRITICAL" in severities):
        errors.append("verdict CONCERNS requires WARNING and no CRITICAL finding")
    if verdict == "CLEAN" and any(item in {"CRITICAL", "WARNING"} for item in severities):
        errors.append("verdict CLEAN permits NOTE findings only")

    serialized = json.dumps(payload, ensure_ascii=False)
    for label, pattern in SENSITIVE_PATTERNS.items():
        if pattern.search(serialized):
            errors.append(f"{label} detected; report location without reproducing the value")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    args = parser.parse_args()
    errors = verify(args.review)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {args.review} satisfies the adversarial-review contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
