#!/usr/bin/env python3
"""Validate the local public-skill catalog without asserting runtime readiness."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EXPECTED_COUNT = 56
ALLOWED_CATEGORIES = {"create", "think", "build", "verify-grow"}
ALLOWED_RISKS = {"low", "medium", "high"}
ALLOWED_STATUSES = {"candidate", "beta", "ready", "paused", "retired"}
REQUIRED_FIELDS = {
    "name",
    "category",
    "trigger",
    "compatible_agents",
    "required_tools",
    "risk_level",
    "public_version",
    "quickstart",
    "example",
    "validator",
    "source_license",
    "maintenance_status",
    "star_potential",
    "public_readiness",
    "blockers",
}
READY_FIELDS = {
    "quickstart",
    "example",
    "validator",
    "source_license",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot parse catalog: {exc}"]

    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    skills = payload.get("skills")
    if not isinstance(skills, list):
        return errors + ["skills must be an array"]
    if len(skills) != EXPECTED_COUNT:
        errors.append(f"expected {EXPECTED_COUNT} skills, found {len(skills)}")

    seen: set[str] = set()
    for index, entry in enumerate(skills):
        where = f"skills[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{where} must be an object")
            continue
        missing = REQUIRED_FIELDS - entry.keys()
        if missing:
            errors.append(f"{where} missing fields: {', '.join(sorted(missing))}")
        name = entry.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"dayan-[a-z0-9-]+", name):
            errors.append(f"{where}.name must match dayan-[a-z0-9-]+")
        elif name in seen:
            errors.append(f"duplicate skill name: {name}")
        else:
            seen.add(name)
        if entry.get("category") not in ALLOWED_CATEGORIES:
            errors.append(f"{where}.category is invalid")
        if entry.get("risk_level") not in ALLOWED_RISKS:
            errors.append(f"{where}.risk_level is invalid")
        status = entry.get("maintenance_status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{where}.maintenance_status is invalid")
        for list_field in ("compatible_agents", "required_tools", "blockers"):
            if not isinstance(entry.get(list_field), list):
                errors.append(f"{where}.{list_field} must be an array")
        for score_field in ("star_potential", "public_readiness"):
            score = entry.get(score_field)
            if not isinstance(score, int) or not 0 <= score <= 100:
                errors.append(f"{where}.{score_field} must be an integer from 0 to 100")
        if status in {"beta", "ready"}:
            for field in READY_FIELDS:
                value = entry.get(field)
                if value in (None, "", "pending"):
                    errors.append(f"{where} is {status} but {field} is unresolved")
        if status == "ready":
            if entry.get("blockers"):
                errors.append(f"{where} is ready but blockers are not empty")
            if not entry.get("compatible_agents"):
                errors.append(f"{where} is ready but has no verified compatible agent")
        for field in ("quickstart", "example", "validator"):
            value = entry.get(field)
            if value not in (None, ""):
                target = (path.parent / value).resolve()
                if path.parent.resolve() not in target.parents:
                    errors.append(f"{where}.{field} escapes the package root")
                elif not target.is_file():
                    errors.append(f"{where}.{field} does not exist: {value}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", nargs="?", default="catalog.json")
    args = parser.parse_args()
    errors = validate(Path(args.catalog))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: catalog contains {EXPECTED_COUNT} unique, schema-valid candidates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
