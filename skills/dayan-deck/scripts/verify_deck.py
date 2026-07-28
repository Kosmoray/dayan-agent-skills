#!/usr/bin/env python3
"""Deterministic preflight for self-contained HTML slide decks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REMOTE_RE = re.compile(
    r"""(?ix)
    (?:
      (?:src|href)\s*=\s*["'](?:https?:)?//
      |
      (?:url|@import|fetch|import)\s*\([^)]*(?:https?:)?//
    )
    """
)
PRIVATE_PATH_RE = re.compile(r"(?:/Users/|/home/)[A-Za-z0-9._-]+/")
SECRET_RE = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
)
AUDIENCE_REDLINE_RE = re.compile(
    r"(?i)(?:speaker notes?|presenter notes?|production note|制作备注|讲述者注意|待填|待删|待替换)"
)


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sections: list[dict[str, str]] = []
        self.ids: list[str] = []
        self.buttons = 0
        self.labelled_buttons = 0
        self.headings = 0
        self.progressbars = 0
        self.viewport = False
        self.slide_heading_counts: list[int] = []
        self._slide_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "section" and "slide" in data.get("class", "").split():
            self.sections.append(data)
            self.slide_heading_counts.append(0)
            self._slide_depth += 1
        if tag == "button":
            self.buttons += 1
            if data.get("aria-label"):
                self.labelled_buttons += 1
        if tag in {"h1", "h2"}:
            self.headings += 1
            if self._slide_depth and self.slide_heading_counts:
                self.slide_heading_counts[-1] += 1
        if data.get("role") == "progressbar":
            self.progressbars += 1
        if tag == "meta" and data.get("name") == "viewport":
            self.viewport = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "section" and self._slide_depth:
            self._slide_depth -= 1


def verify(path: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return {"file": str(path), "errors": [f"cannot read UTF-8 HTML: {exc}"], "warnings": []}

    parser = DeckParser()
    parser.feed(text)

    if not text.lstrip().lower().startswith("<!doctype html>"):
        errors.append("missing HTML5 doctype")
    if not parser.viewport:
        errors.append("missing viewport meta")
    if len(parser.sections) < 3:
        errors.append("deck must contain at least three section.slide elements")
    active = [item for item in parser.sections if "active" in item.get("class", "").split()]
    if len(active) != 1:
        errors.append(f"expected exactly one initially active slide, found {len(active)}")
    slide_ids = [item.get("id", "") for item in parser.sections]
    if any(not item for item in slide_ids):
        errors.append("every slide needs a stable id")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("HTML ids must be unique")
    if any(count < 1 for count in parser.slide_heading_counts):
        errors.append("every slide needs its own h1 or h2 heading")
    if parser.buttons < 2 or parser.labelled_buttons != parser.buttons:
        errors.append("provide at least two controls and label every button")
    if parser.progressbars < 1:
        errors.append("missing labelled progressbar")

    required_contracts = {
        "16:9 stage": "aspect-ratio: 16 / 9",
        "print styles": "@media print",
        "reduced motion": "prefers-reduced-motion",
        "keyboard navigation": "keydown",
        "active-slide switching": "classList.toggle",
    }
    compact = re.sub(r"\s+", " ", text)
    for label, needle in required_contracts.items():
        if needle not in text and needle not in compact:
            errors.append(f"missing {label} contract")

    if REMOTE_RE.search(text):
        errors.append("remote URL dependency detected")
    if PRIVATE_PATH_RE.search(text):
        errors.append("private user path detected")
    if SECRET_RE.search(text):
        errors.append("credential-like assignment detected")
    if AUDIENCE_REDLINE_RE.search(text):
        errors.append("audience artifact contains presenter or production-note language")
    if "<img" in text.lower():
        warnings.append("images require manual alt-text and license review")

    return {
        "file": str(path),
        "slides": len(parser.sections),
        "errors": errors,
        "warnings": warnings,
        "limitations": [
            "does not prove visual quality or absence of clipping",
            "does not verify factual accuracy",
            "does not verify PPTX editability",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = verify(Path(args.html))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["errors"]:
        for error in result["errors"]:
            print(f"ERROR: {error}")
    else:
        print(f"PASS: {result['file']} satisfies the structural deck contract ({result['slides']} slides)")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
