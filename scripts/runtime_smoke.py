#!/usr/bin/env python3
"""Run an offline Skill lifecycle smoke test in a clean temporary home."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime
import json
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
INSTALLER = ROOT / "installers" / "install.py"
AGENTS = ("codex", "claude-code")
DEFAULT_SKILLS = ("dayan-wenzhen", "dayan-deck", "dayan-adversarial-reviewer")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "before",
    "for",
    "from",
    "in",
    "into",
    "of",
    "or",
    "the",
    "this",
    "to",
    "with",
}


@dataclass(frozen=True)
class Skill:
    name: str
    trigger: str
    description: str
    example: str
    validator: str


@dataclass
class RuntimeResult:
    agent: str
    skill: str
    ok: bool
    checks: dict[str, bool]
    evidence: str
    routed_skill: str | None
    command: list[str]

    def as_json(self) -> dict[str, object]:
        return {
            "agent": self.agent,
            "skill": self.skill,
            "result": "pass" if self.ok else "fail",
            "checks": self.checks,
            "routed_skill": self.routed_skill,
            "command": self.command,
            "evidence": self.evidence,
        }


def load_catalog() -> tuple[str, dict[str, Skill]]:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    skills: dict[str, Skill] = {}
    for item in payload["skills"]:
        skill_md = ROOT / "skills" / item["name"] / "SKILL.md"
        skills[item["name"]] = Skill(
            name=item["name"],
            trigger=item["trigger"],
            description=frontmatter_description(skill_md),
            example=item["example"],
            validator=item["validator"],
        )
    return str(payload["release"]), skills


def frontmatter_description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip("'\"") if match else ""


def destination(home: Path, agent: str) -> Path:
    return home / (".codex/skills" if agent == "codex" else ".claude/skills")


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


def install_skill(home: Path, agent: str, skill: str, *, update: bool = False) -> bool:
    command = [
        sys.executable,
        str(INSTALLER),
        skill,
        "--agent",
        agent,
        "--home",
        str(home),
    ]
    if update:
        command.append("--update")
    result = run(command)
    return result.returncode == 0


def discover(home: Path, agent: str, catalog: dict[str, Skill]) -> dict[str, Skill]:
    root = destination(home, agent)
    discovered: dict[str, Skill] = {}
    if not root.is_dir():
        return discovered
    for marker in sorted(root.glob("*/.dayan-package.json")):
        try:
            payload = json.loads(marker.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        skill_name = payload.get("name")
        if (
            payload.get("agent") == agent
            and payload.get("package") == "dayan-agent-skills"
            and isinstance(skill_name, str)
            and (marker.parent / "SKILL.md").is_file()
            and skill_name in catalog
        ):
            discovered[skill_name] = catalog[skill_name]
    return discovered


def tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) > 2 and token not in STOPWORDS
    }


def route(prompt: str, candidates: dict[str, Skill]) -> str | None:
    prompt_tokens = tokens(prompt)
    best_name: str | None = None
    best_score = 0
    for skill in candidates.values():
        if prompt.strip().lower() == skill.trigger.strip().lower():
            score = 1000
        else:
            route_text = " ".join([skill.name.replace("-", " "), skill.trigger, skill.description])
            score = len(prompt_tokens & tokens(route_text))
        if score > best_score:
            best_score = score
            best_name = skill.name
    return best_name if best_score >= 3 else None


def validator_command(skill: Skill) -> list[str]:
    if skill.validator == "scripts/validate_public_skill.py":
        return [sys.executable, skill.validator, skill.name]
    return [sys.executable, skill.validator, skill.example]


def run_runtime_case(home: Path, agent: str, skill: Skill, candidates: dict[str, Skill]) -> RuntimeResult:
    installed = (destination(home, agent) / skill.name / "SKILL.md").is_file()
    marker = destination(home, agent) / skill.name / ".dayan-package.json"
    marker_ok = False
    if marker.is_file():
        try:
            payload = json.loads(marker.read_text(encoding="utf-8"))
            marker_ok = payload.get("name") == skill.name and payload.get("agent") == agent
        except json.JSONDecodeError:
            marker_ok = False
    routed_skill = route(skill.trigger, candidates)
    command = validator_command(skill)
    command_result = run(command)
    update_ok = install_skill(home, agent, skill.name, update=True)
    checks = {
        "discovery_found_skill": skill.name in candidates,
        "skill_md_present": installed,
        "marker_valid": marker_ok,
        "trigger_routes_to_expected_skill": routed_skill == skill.name,
        "example_command_exit_zero": command_result.returncode == 0,
        "safe_update_exit_zero": update_ok,
    }
    ok = all(checks.values())
    evidence = "discovered, trigger routed, example command passed, safe update passed"
    if not ok:
        evidence = (command_result.stderr or command_result.stdout or "runtime smoke check failed").strip()
    return RuntimeResult(
        agent=agent,
        skill=skill.name,
        ok=ok,
        checks=checks,
        evidence=evidence,
        routed_skill=routed_skill,
        command=command,
    )


def build_matrix(results: list[RuntimeResult], release: str, selected_all: bool) -> dict[str, object]:
    return {
        "schema_version": 1,
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "package_release": release,
        "target_home": "temporary-clean-directory",
        "skill_scope": "all-public-beta-skills" if selected_all else "featured-runtime-skills",
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
            "actual host application UI loading",
            "LLM model decision quality",
            "networked marketplace install flows",
            "uninstall behavior in a user's live configuration",
        ],
    }


def render_markdown(results: list[RuntimeResult], release: str, kept_home: Path | None, selected_all: bool) -> str:
    passed = sum(1 for item in results if item.ok)
    lines = [
        "# Dayan Agent Skills runtime smoke report",
        "",
        f"- Package release: `{release}`",
        f"- Python: `{platform.python_version()}`",
        f"- OS: `{platform.platform()}`",
        "- Target home: temporary clean directory",
        f"- Scope: `{'all public beta Skills' if selected_all else 'featured runtime Skills'}`",
        f"- Summary: `{passed}/{len(results)} PASS`",
    ]
    if kept_home is not None:
        lines.append(f"- Kept home: `{kept_home}`")
    lines.extend(
        [
            "",
            "| Agent target | Skill | Result | Routed Skill | Evidence |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        evidence = result.evidence.replace("\n", " ")[:180]
        lines.append(
            f"| `{result.agent}` | `{result.skill}` | {status} | `{result.routed_skill}` | {evidence} |"
        )
    lines.extend(
        [
            "",
            "## What this proves",
            "",
            "- installed Skills can be discovered from a clean agent-style home;",
            "- catalog trigger text routes to the expected installed Skill in the offline host contract;",
            "- the selected Skill's declared example command exits successfully;",
            "- `--update` replaces only directories that carry the matching Dayan package marker.",
            "",
            "## What this does not prove",
            "",
            "- actual host application UI loading;",
            "- LLM model decision quality;",
            "- networked marketplace install flows;",
            "- uninstall behavior in a user's live configuration.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", action="append", help="Skill to test; may be repeated. Default: three featured Skills")
    parser.add_argument("--all-skills", action="store_true", help="Test every public beta Skill listed in catalog.json")
    parser.add_argument("--agent", choices=[*AGENTS, "all"], default="all")
    parser.add_argument("--json-output", type=Path, help="Write a machine-readable runtime matrix JSON file")
    parser.add_argument("--keep-home", action="store_true", help="Keep the temporary home for inspection")
    args = parser.parse_args()

    release, catalog = load_catalog()
    if args.all_skills and args.skill:
        print("ERROR: use either --all-skills or --skill, not both")
        return 1
    selected_names = list(catalog) if args.all_skills else (args.skill or list(DEFAULT_SKILLS))
    unknown = sorted(set(selected_names) - set(catalog))
    if unknown:
        print("ERROR: unknown Skill(s): " + ", ".join(unknown))
        return 1
    selected_agents = list(AGENTS) if args.agent == "all" else [args.agent]

    temp_home = Path(tempfile.mkdtemp(prefix="dayan-runtime-"))
    results: list[RuntimeResult] = []
    try:
        for agent in selected_agents:
            for skill_name in selected_names:
                if not install_skill(temp_home, agent, skill_name):
                    results.append(
                        RuntimeResult(
                            agent=agent,
                            skill=skill_name,
                            ok=False,
                            checks={"install_exit_zero": False},
                            evidence="initial install failed",
                            routed_skill=None,
                            command=[],
                        )
                    )
            candidates = discover(temp_home, agent, catalog)
            non_trigger_ok = route("tell me a casual joke about cats", candidates) is None
            for skill_name in selected_names:
                result = run_runtime_case(temp_home, agent, catalog[skill_name], candidates)
                result.checks["non_trigger_prompt_not_routed"] = non_trigger_ok
                result.ok = result.ok and non_trigger_ok
                results.append(result)

        kept_home = temp_home if args.keep_home else None
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
