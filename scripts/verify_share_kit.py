#!/usr/bin/env python3
"""Verify the public share kit and social card."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARE_KIT = ROOT / "docs" / "share-kit.md"
SOCIAL_CARD = ROOT / "assets" / "social-card.svg"
INDEX = ROOT / "docs" / "index.html"
README = ROOT / "README.md"

REQUIRED_SHARE_TOKENS = (
    "Canonical links",
    "Approved facts",
    "56 installable public beta Skills",
    "15 public method cards",
    "12 copyable artifact fixtures",
    "18 documented local repository tools",
    "112/112 clean package-install smoke checks pass",
    "112/112 offline lifecycle smoke checks pass",
    "MIT license",
    "Short copy",
    "Longer copy",
    "Post variants",
    "What not to claim",
    "Do not claim universal host-version compatibility",
    "Do not ask for bought stars",
    "star the library if it is worth returning to",
)
REQUIRED_CARD_TOKENS = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"',
    "Dayan Agent Skills social card",
    "56 Skills.",
    "One control library.",
    "Prompts say what to ask",
    "Control layers say what must be true",
    "112/112",
    "MIT",
)
REDLINE = re.compile(r"(?:/Users|/home)/|/Desktop/|API_KEY|PRIVATE KEY", re.I)


def local_markdown_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (path.parent / local_target).exists():
            errors.append(f"{path.relative_to(ROOT)} broken link {target}")
    return errors


def verify() -> list[str]:
    errors: list[str] = []
    for path in (SHARE_KIT, SOCIAL_CARD, INDEX, README):
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")
    if errors:
        return errors

    share = SHARE_KIT.read_text(encoding="utf-8")
    card = SOCIAL_CARD.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    for token in REQUIRED_SHARE_TOKENS:
        if token not in share:
            errors.append(f"share kit missing {token}")
    for token in REQUIRED_CARD_TOKENS:
        if token not in card:
            errors.append(f"social card missing {token}")
    if "docs/share-kit.md" not in readme:
        errors.append("README must link to docs/share-kit.md")
    for token in (
        'property="og:image"',
        "assets/social-card.svg",
        'name="twitter:card"',
        'property="og:title"',
    ):
        if token not in index:
            errors.append(f"landing page missing share metadata {token}")
    for path, text in ((SHARE_KIT, share), (SOCIAL_CARD, card)):
        if REDLINE.search(text):
            errors.append(f"{path.relative_to(ROOT)} contains public redline")
    errors.extend(local_markdown_links(SHARE_KIT, share))
    return errors


def main() -> int:
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: share kit and social card are linked, bounded, and verifiable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
