#!/usr/bin/env python3
"""Validate the public beta package before push or tag."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SANITIZATION.md",
    "THIRD_PARTY_NOTICES.md",
    "ROADMAP.md",
    "CITATION.cff",
    "catalog.json",
    "llms.txt",
    "assets/dayan-mark.svg",
    "assets/dayan-mark-on-dark.svg",
    "assets/hero.svg",
    ".codex-plugin/plugin.json",
    ".github/workflows/ci.yml",
    "docs/index.html",
    "docs/robots.txt",
    "docs/sitemap.xml",
    "docs/demos/wenzhen.html",
    "docs/demos/deck.html",
    "docs/demos/reviewer.html",
    "docs/quickstart.md",
    "docs/choose-a-skill.md",
    "docs/faq.md",
    "docs/compatibility.md",
    "docs/launch-kit.md",
    "docs/publication-runbook.md",
    "scripts/verify_site.py",
    "skills/dayan-deck/SKILL.md",
    "skills/dayan-deck/examples/starter.html",
    "skills/dayan-deck/scripts/verify_deck.py",
    "skills/dayan-adversarial-reviewer/SKILL.md",
    "skills/dayan-adversarial-reviewer/references/rubric.md",
    "skills/dayan-adversarial-reviewer/examples/clean-review.json",
    "skills/dayan-adversarial-reviewer/examples/block-review.json",
    "skills/dayan-adversarial-reviewer/scripts/verify_review.py",
    "skills/dayan-adversarial-reviewer/PROVENANCE.md",
    "skills/dayan-adversarial-reviewer/SANITIZATION.md",
    "skills/dayan-wenzhen/SKILL.md",
    "skills/dayan-wenzhen/references/contract-schema.md",
    "skills/dayan-wenzhen/examples/starter-contract.json",
    "skills/dayan-wenzhen/examples/rejected-missing-stop.json",
    "skills/dayan-wenzhen/scripts/verify_contract.py",
    "skills/dayan-wenzhen/PROVENANCE.md",
    "skills/dayan-wenzhen/SANITIZATION.md",
    "scripts/validate_public_skill.py",
]
PROHIBITED_PUBLIC_PATTERNS = {
    "private user path": re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/|/Desktop/"),
    "private workflow marker": re.compile(r"(?i)(?:private[_-]workflow|internal[_-](?:only|strategy|control))"),
    "private key header": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
}


def run(command: list[str]) -> list[str]:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        return [result.stdout.strip() or result.stderr.strip() or f"command failed: {' '.join(command)}"]
    return []


def main() -> int:
    errors = [f"missing required file: {item}" for item in REQUIRED_FILES if not (ROOT / item).is_file()]

    try:
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        plugin = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"manifest parse failure: {exc}")
        catalog = {}
        plugin = {}

    if catalog.get("release") != "0.5.2-beta.1":
        errors.append("catalog release must be 0.5.2-beta.1")
    skills = catalog.get("skills", [])
    beta = [item for item in skills if item.get("maintenance_status") == "beta"]
    beta_names = [item.get("name") for item in beta]
    if len(beta_names) != 56:
        errors.append("all 56 catalog Skills must be public beta in v0.5.2-beta.1")
    if plugin.get("version") != catalog.get("release"):
        errors.append("plugin and catalog versions must match")
    if plugin.get("license") != "MIT":
        errors.append("plugin license must be MIT")
    if plugin.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")

    for markdown_name in ("README.md", "README.zh-CN.md", "CONTRIBUTING.md", "ROADMAP.md"):
        markdown_path = ROOT / markdown_name
        markdown = markdown_path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (markdown_path.parent / local_target).exists():
                errors.append(f"broken local link in {markdown_name}: {target}")

    for skill_name in beta_names:
        skill_text = (ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
        if not skill_text.startswith("---\n"):
            errors.append(f"{skill_name} SKILL.md is missing frontmatter")
        if not re.search(rf"^name:\s*{re.escape(skill_name)}$", skill_text, re.MULTILINE):
            errors.append(f"{skill_name} frontmatter name is invalid")
        if not re.search(r"^description:\s*.+$", skill_text, re.MULTILINE):
            errors.append(f"{skill_name} frontmatter description is missing")

    detector_files = {
        Path("scripts/validate_release.py"),
        Path("scripts/scan_public_redlines.py"),
        Path("skills/dayan-deck/scripts/verify_deck.py"),
        Path("skills/dayan-adversarial-reviewer/scripts/verify_review.py"),
        Path("skills/dayan-wenzhen/scripts/verify_contract.py"),
        Path("scripts/validate_public_skill.py"),
        Path("scripts/verify_site.py"),
    }
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and ".git" not in item.parts):
        relative = path.relative_to(ROOT)
        if relative in detector_files or relative.parts[0] == "tests":
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".zip", ".pdf"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in PROHIBITED_PUBLIC_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label} in {relative}")

    errors.extend(run([sys.executable, "scripts/validate_catalog.py", "catalog.json"]))
    errors.extend(run([sys.executable, "scripts/scan_public_redlines.py", "skills"]))
    errors.extend(run([sys.executable, "scripts/verify_site.py"]))
    errors.extend(
        run(
            [
                sys.executable,
                "skills/dayan-deck/scripts/verify_deck.py",
                "skills/dayan-deck/examples/starter.html",
            ]
        )
    )

    legacy = {"dayan-deck", "dayan-adversarial-reviewer", "dayan-wenzhen"}
    for skill_name in beta_names:
        if skill_name not in legacy:
            errors.extend(run([sys.executable, "scripts/validate_public_skill.py", skill_name]))
    for fixture in ("clean-review.json", "block-review.json"):
        errors.extend(
            run(
                [
                    sys.executable,
                    "skills/dayan-adversarial-reviewer/scripts/verify_review.py",
                    f"skills/dayan-adversarial-reviewer/examples/{fixture}",
                ]
            )
        )

    errors.extend(
        run(
            [
                sys.executable,
                "skills/dayan-wenzhen/scripts/verify_contract.py",
                "skills/dayan-wenzhen/examples/starter-contract.json",
            ]
        )
    )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: public beta release package is internally consistent ({len(REQUIRED_FILES)} required files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
