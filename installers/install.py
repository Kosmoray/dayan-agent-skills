#!/usr/bin/env python3
"""Install or update a packaged Skill in an explicit agent home."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

AGENTS = {
    "codex": Path(".codex/skills"),
    "claude-code": Path(".claude/skills"),
}
PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def safe_destination(home: Path, agent: str, skill_name: str) -> Path:
    home = home.expanduser().resolve()
    destination = (home / AGENTS[agent] / skill_name).resolve()
    if home == destination or home not in destination.parents:
        raise ValueError("destination escapes the selected home")
    return destination


def marker_payload(agent: str, skill_name: str) -> dict[str, str]:
    return {"name": skill_name, "agent": agent, "package": "dayan-agent-skills"}


def read_owned_marker(destination: Path, agent: str, skill_name: str) -> dict[str, object]:
    marker = destination / ".dayan-package.json"
    if not marker.is_file():
        raise FileExistsError("destination exists but has no Dayan package marker")
    payload = json.loads(marker.read_text(encoding="utf-8"))
    expected = marker_payload(agent, skill_name)
    if any(payload.get(key) != value for key, value in expected.items()):
        raise FileExistsError("destination exists but is not owned by this package, Skill, and agent target")
    return payload


def copy_skill(source: Path, destination: Path, agent: str, skill_name: str) -> None:
    shutil.copytree(source, destination)
    (destination / ".dayan-package.json").write_text(
        json.dumps(marker_payload(agent, skill_name), indent=2),
        encoding="utf-8",
    )


def replace_owned_destination(source: Path, destination: Path, agent: str, skill_name: str) -> None:
    read_owned_marker(destination, agent, skill_name)
    backup = destination.with_name(f".{destination.name}.dayan-update-backup")
    staging = destination.with_name(f".{destination.name}.dayan-update-staging")
    if backup.exists() or staging.exists():
        raise FileExistsError("stale Dayan update staging directory exists; inspect and remove it before retrying")
    shutil.copytree(source, staging)
    (staging / ".dayan-package.json").write_text(
        json.dumps(marker_payload(agent, skill_name), indent=2),
        encoding="utf-8",
    )
    try:
        destination.rename(backup)
        staging.rename(destination)
    except OSError:
        if backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
        if backup.exists():
            shutil.rmtree(backup)


def install(home: Path, agent: str, skill_name: str, *, update: bool = False) -> Path:
    source = PACKAGE_ROOT / "skills" / skill_name
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError(f"packaged skill does not exist: {skill_name}")
    destination = safe_destination(home, agent, skill_name)
    if destination.exists():
        if not update:
            raise FileExistsError("destination already exists; rerun with --update only if it was installed from this package")
        replace_owned_destination(source, destination, agent, skill_name)
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy_skill(source, destination, agent, skill_name)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill")
    parser.add_argument("--agent", choices=sorted(AGENTS), required=True)
    parser.add_argument("--home", type=Path, required=True, help="explicit target home; use a temporary directory for smoke tests")
    parser.add_argument(
        "--update",
        action="store_true",
        help="replace an existing Skill only when its Dayan package marker matches this package, Skill, and agent target",
    )
    args = parser.parse_args()
    try:
        destination = install(args.home, args.agent, args.skill, update=args.update)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    action = "updated" if args.update else "installed"
    print(f"PASS: {action} {args.skill} for {args.agent} at {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
