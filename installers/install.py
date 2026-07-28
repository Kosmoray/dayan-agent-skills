#!/usr/bin/env python3
"""Install a packaged Skill into an isolated agent home."""

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


def install(home: Path, agent: str, skill_name: str) -> Path:
    source = PACKAGE_ROOT / "skills" / skill_name
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError(f"packaged skill does not exist: {skill_name}")
    destination = safe_destination(home, agent, skill_name)
    if destination.exists():
        raise FileExistsError("destination already exists; the public beta does not perform destructive updates")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    (destination / ".dayan-package.json").write_text(
        json.dumps({"name": skill_name, "agent": agent, "package": "dayan-agent-skills"}, indent=2),
        encoding="utf-8",
    )
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill")
    parser.add_argument("--agent", choices=sorted(AGENTS), required=True)
    parser.add_argument("--home", type=Path, required=True, help="explicit target home; use a temporary directory for smoke tests")
    args = parser.parse_args()
    try:
        destination = install(args.home, args.agent, args.skill)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"PASS: installed {args.skill} for {args.agent} at {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
