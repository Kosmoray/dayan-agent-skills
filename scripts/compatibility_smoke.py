#!/usr/bin/env python3
"""Run clean-home install smoke checks and print a paste-ready report."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
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

    def as_json(self) -> dict[str, object]:
        return {
            "agent": self.agent,
            "skill": self.skill,
            "result": "pass" if self.ok else "fail",
            "checks": {
                "install_exit_zero": self.ok,
                "skill_md_present": self.ok,
                "marker_valid": self.marker_ok,
            },
            "evidence": self.detail,
        }


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


def build_matrix(results: list[Result], release: str, selected_all: bool) -> dict[str, object]:
    return {
        "schema_version": 1,
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "package_release": release,
        "target_home": "temporary-clean-directory",
        "skill_scope": "all-public-beta-skills" if selected_all else "selected-skills",
        "agents": list(AGENTS),
        "environment": {
            "python": platform.python_version(),
            "os": platform.platform(),
        },
        "summary": {
            "total": len(results),
            "pass": sum(1 for item in results if item.ok),
            "fail": sum(1 for item in results if not item.ok),
        },
        "results": [item.as_json() for item in results],
        "not_claimed": [
            "host application discovery",
            "runtime trigger behavior",
            "update or uninstall behavior in a user's live configuration",
        ],
    }


def render_markdown(results: list[Result], release: str, kept_home: Path | None, selected_all: bool) -> str:
    passed = sum(1 for item in results if item.ok)
    lines = [
        "# Dayan Agent Skills compatibility smoke report",
        "",
        f"- Package release: `{release}`",
        f"- Python: `{platform.python_version()}`",
        f"- OS: `{platform.platform()}`",
        "- Target home: temporary clean directory",
        f"- Scope: `{'all public beta Skills' if selected_all else 'selected Skills'}`",
        f"- Summary: `{passed}/{len(results)} PASS`",
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
    parser.add_argument("--all-skills", action="store_true", help="Test every public beta Skill listed in catalog.json")
    parser.add_argument("--agent", choices=[*AGENTS, "all"], default="all")
    parser.add_argument("--json-output", type=Path, help="Write a machine-readable compatibility matrix JSON file")
    parser.add_argument("--keep-home", action="store_true", help="Keep the temporary home for inspection")
    args = parser.parse_args()

    all_skills = skill_names()
    available = set(all_skills)
    if args.all_skills and args.skill:
        print("ERROR: use either --all-skills or --skill, not both")
        return 1
    selected_skills = all_skills if args.all_skills else (args.skill or ["dayan-wenzhen"])
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
        release = catalog_release()
        if args.json_output:
            args.json_output.parent.mkdir(parents=True, exist_ok=True)
            args.json_output.write_text(
                json.dumps(build_matrix(results, release, args.all_skills), indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
        print(render_markdown(results, release, kept_home, args.all_skills))
        return 0 if all(item.ok for item in results) else 1
    finally:
        if not args.keep_home:
            shutil.rmtree(temp_home, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
