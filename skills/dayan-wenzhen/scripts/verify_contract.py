#!/usr/bin/env python3
"""Validate the machine-readable Wenzhen task contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WORK_TYPES = {"answer", "decision", "research", "build", "experiment", "specialist_review"}
RISK_LEVELS = {"L0", "L1", "L2", "L3"}
ROOT_FIELDS = {"schema_version", "title", "triage", "hypothesis", "contract", "options", "reversible_bet", "next_route"}
TRIAGE_FIELDS = {"work_type", "risk_level", "allowed_action", "release_authority", "minimum_evidence"}
HYPOTHESIS_FIELDS = {"surface_request", "best_current_hypothesis", "supporting_facts", "alternatives", "falsification_signal"}
CONTRACT_FIELDS = {"goal", "outcome", "context", "risks_review", "output", "evidence"}
OPTION_FIELDS = {"current_route", "alternative_route", "third_route", "defer_or_shrink"}
BET_FIELDS = {"next_step", "expected_signal", "pause_signal", "checkpoint", "continue_evidence", "rollback"}
HIGH_RISK_ACTIONS = re.compile(r"\b(?:publish|send|spend|deploy|delete|sign|credential)\w*\b", re.IGNORECASE)
PRIVATE_PATH = re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\", re.IGNORECASE)
CREDENTIAL = re.compile(r"(?i)\b(?:api[_-]?key|token|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}")


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_fields(payload: object, required: set[str], label: str, errors: list[str]) -> dict:
    if not isinstance(payload, dict):
        errors.append(f"{label} must be an object")
        return {}
    missing = required - payload.keys()
    if missing:
        errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
    return payload


def verify(path: Path) -> list[str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot parse contract JSON: {exc}"]

    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["contract must be a JSON object"]
    missing = ROOT_FIELDS - payload.keys()
    if missing:
        errors.append(f"missing root fields: {', '.join(sorted(missing))}")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not nonempty(payload.get("title")):
        errors.append("title must be a non-empty string")
    if payload.get("next_route") not in WORK_TYPES:
        errors.append("next_route must be a valid work type")

    triage = require_fields(payload.get("triage"), TRIAGE_FIELDS, "triage", errors)
    if triage.get("work_type") not in WORK_TYPES:
        errors.append("triage.work_type is invalid")
    if triage.get("risk_level") not in RISK_LEVELS:
        errors.append("triage.risk_level is invalid")
    for field in TRIAGE_FIELDS - {"work_type", "risk_level"}:
        if not nonempty(triage.get(field)):
            errors.append(f"triage.{field} must be a non-empty string")

    hypothesis = require_fields(payload.get("hypothesis"), HYPOTHESIS_FIELDS, "hypothesis", errors)
    for field in HYPOTHESIS_FIELDS - {"supporting_facts", "alternatives"}:
        if not nonempty(hypothesis.get(field)):
            errors.append(f"hypothesis.{field} must be a non-empty string")
    for field in ("supporting_facts", "alternatives"):
        value = hypothesis.get(field)
        if not isinstance(value, list) or not value or not all(nonempty(item) for item in value):
            errors.append(f"hypothesis.{field} must be a non-empty list of strings")

    for label, required in (("contract", CONTRACT_FIELDS), ("options", OPTION_FIELDS), ("reversible_bet", BET_FIELDS)):
        section = require_fields(payload.get(label), required, label, errors)
        for field in required:
            if not nonempty(section.get(field)):
                errors.append(f"{label}.{field} must be a non-empty string")

    if triage.get("risk_level") in {"L2", "L3"}:
        if HIGH_RISK_ACTIONS.search(str(triage.get("allowed_action", ""))):
            errors.append("L2/L3 allowed_action must not authorize an external or irreversible action")
        review_text = str(payload.get("contract", {}).get("risks_review", ""))
        if not re.search(r"\b(?:review|approve|stop|pause|rollback)\b", review_text, re.IGNORECASE):
            errors.append("L2/L3 risks_review must name a review or stop boundary")

    serialized = json.dumps(payload, ensure_ascii=False)
    if PRIVATE_PATH.search(serialized):
        errors.append("private machine path detected")
    if CREDENTIAL.search(serialized):
        errors.append("credential assignment detected")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    args = parser.parse_args()
    errors = verify(args.contract)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {args.contract} satisfies the Wenzhen task-contract schema")
    return 0


if __name__ == "__main__":
    sys.exit(main())

