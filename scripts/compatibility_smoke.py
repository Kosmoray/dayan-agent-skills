#!/usr/bin/env python3
"""Run clean-home install smoke checks and print a paste-ready report."""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "installers" / "install.py"
CATALOG = ROOT / "catalog.json"
AGENTS = ("codex", "claude-code")


@dataclass
class Result:
    agent: str
    skill: str
    ok: bool
    detail: str
    marker_ok: bool


def catalog_release() -> str:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    return str(payload.get("release", "unknown"))


def skill_names() -> list[str]:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    return [item["name"] for item in payload["skills"]]


def destination(home: Path, agent: str, skill: str) -> Path:
    prefix = ".codex/skills" if agent == "codex" else ".claude/skills"
    return home / prefix / skill


def run_install(home: Path, agent: str, skill: str) -> Result:
    command = [
        sys.executable,
        str(INSTALLER),
        skill,
        "--agent",
        agent,
        "--home",
        str(home),
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    dest = destination(home, agent, skill)
    marker = dest / ".dayan-package.json"
    marker_ok = False
    if marker.is_file():
        try:
            payload = json.loads(marker.read_text(encoding="utf-8"))
            marker_ok = payload.get("name") == skill and payload.get("agent") == agent
        except json.JSONDecodeError:
            marker_ok = False
    ok = completed.returncode == 0 and (dest / "SKILL.md").is_file() and marker_ok
    detail = "installed, SKILL.md present, marker valid" if ok else (completed.stderr or completed.stdout or "unknown failure")
    return Result(agent=agent, skill=skill, ok=ok, detail=detail.strip(), marker_ok=marker_ok)


def render_markdown(results: list[Result], release: str, kept_home: Path | None) -> str:
    lines = [
        "# Dayan Agent Skills compatibility smoke report",
        "",
        f"- Package release: `{release}`",
        f"- Python: `{platform.python_version()}`",
        f"- OS: `{platform.platform()}`",
        "- Target home: temporary clean directory",
    ]
    if kept_home is not None:
        lines.append(f"- Kept home: `{kept_home}`")
    lines.extend(
        [
            "",
            "| Agent target | Skill | Result | Evidence |",
            "| --- | --- | --- | --- |",
        ]
    )
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        evidence = result.detail.replace("\n", " ")[:180]
        lines.append(f"| `{result.agent}` | `{result.skill}` | {status} | {evidence} |")
    lines.extend(
        [
            "",
            "## What this proves",
            "",
            "- clean temporary-home installation works for the selected targets;",
            "- the installed Skill directory contains `SKILL.md`;",
            "- the `.dayan-package.json` marker matches the Skill and target agent.",
            "",
            "## What this does not prove",
            "",
            "- host application discovery;",
            "- runtime trigger behavior;",
            "- update or uninstall behavior in a user's live configuration.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", action="append", help="Skill to test; may be repeated. Default: dayan-wenzhen")
    parser.add_argument("--agent", choices=[*AGENTS, "all"], default="all")
    parser.add_argument("--keep-home", action="store_true", help="Keep the temporary home for inspection")
    args = parser.parse_args()

    available = set(skill_names())
    selected_skills = args.skill or ["dayan-wenzhen"]
    unknown = sorted(set(selected_skills) - available)
    if unknown:
        print("ERROR: unknown Skill(s): " + ", ".join(unknown))
        return 1

    selected_agents = list(AGENTS) if args.agent == "all" else [args.agent]
    temp_home = Path(tempfile.mkdtemp(prefix="dayan-compat-"))
    results: list[Result] = []
    try:
        for skill in selected_skills:
            for agent in selected_agents:
                results.append(run_install(temp_home, agent, skill))
        kept_home = temp_home if args.keep_home else None
        print(render_markdown(results, catalog_release(), kept_home))
        return 0 if all(item.ok for item in results) else 1
    finally:
        if not args.keep_home:
            shutil.rmtree(temp_home, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
