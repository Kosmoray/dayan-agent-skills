from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


deck_verifier = load_module(
    "deck_verifier",
    ROOT / "skills/dayan-deck/scripts/verify_deck.py",
)
installer = load_module("dayan_installer", ROOT / "installers/install.py")


class DeckVerifierTests(unittest.TestCase):
    def test_starter_passes(self):
        result = deck_verifier.verify(ROOT / "skills/dayan-deck/examples/starter.html")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["slides"], 4)

    def test_remote_dependency_fails(self):
        source = (ROOT / "skills/dayan-deck/examples/starter.html").read_text(encoding="utf-8")
        source = source.replace("</head>", '<script src="https://example.invalid/app.js"></script></head>')
        with tempfile.TemporaryDirectory(prefix="openclaw-deck-test-", dir="/tmp") as directory:
            path = Path(directory) / "remote.html"
            path.write_text(source, encoding="utf-8")
            result = deck_verifier.verify(path)
        self.assertIn("remote URL dependency detected", result["errors"])

    def test_two_active_slides_fail(self):
        source = (ROOT / "skills/dayan-deck/examples/starter.html").read_text(encoding="utf-8")
        source = source.replace('<section class="slide" id="problem"', '<section class="slide active" id="problem"')
        with tempfile.TemporaryDirectory(prefix="openclaw-deck-test-", dir="/tmp") as directory:
            path = Path(directory) / "two-active.html"
            path.write_text(source, encoding="utf-8")
            result = deck_verifier.verify(path)
        self.assertTrue(any("exactly one initially active slide" in error for error in result["errors"]))

    def test_presenter_note_language_fails(self):
        source = (ROOT / "skills/dayan-deck/examples/starter.html").read_text(encoding="utf-8")
        source = source.replace("</main>", "<p>Presenter notes: say this slowly.</p></main>")
        with tempfile.TemporaryDirectory(prefix="openclaw-deck-test-", dir="/tmp") as directory:
            path = Path(directory) / "notes.html"
            path.write_text(source, encoding="utf-8")
            result = deck_verifier.verify(path)
        self.assertTrue(any("presenter or production-note" in error for error in result["errors"]))

    def test_slide_without_own_heading_fails(self):
        source = (ROOT / "skills/dayan-deck/examples/starter.html").read_text(encoding="utf-8")
        source = source.replace('<h2 id="problem-title">More elements create less clarity.</h2>', "<p>More elements create less clarity.</p>")
        with tempfile.TemporaryDirectory(prefix="openclaw-deck-test-", dir="/tmp") as directory:
            path = Path(directory) / "missing-heading.html"
            path.write_text(source, encoding="utf-8")
            result = deck_verifier.verify(path)
        self.assertIn("every slide needs its own h1 or h2 heading", result["errors"])

    def test_remote_css_dependency_fails(self):
        source = (ROOT / "skills/dayan-deck/examples/starter.html").read_text(encoding="utf-8")
        source = source.replace("</style>", ".remote{background:url(https://example.invalid/a.png)}</style>")
        with tempfile.TemporaryDirectory(prefix="openclaw-deck-test-", dir="/tmp") as directory:
            path = Path(directory) / "remote-css.html"
            path.write_text(source, encoding="utf-8")
            result = deck_verifier.verify(path)
        self.assertIn("remote URL dependency detected", result["errors"])


class InstallerTests(unittest.TestCase):
    def test_installs_beta_skills_into_both_isolated_agent_homes(self):
        with tempfile.TemporaryDirectory(prefix="openclaw-install-test-", dir="/tmp") as directory:
            home = Path(directory)
            for skill_name in ("dayan-deck", "dayan-adversarial-reviewer", "dayan-wenzhen"):
                for agent in ("codex", "claude-code"):
                    destination = installer.install(home, agent, skill_name)
                    self.assertTrue((destination / "SKILL.md").is_file())
                    self.assertTrue((destination / ".dayan-package.json").is_file())

    def test_refuses_any_overwrite(self):
        with tempfile.TemporaryDirectory(prefix="openclaw-install-test-", dir="/tmp") as directory:
            home = Path(directory)
            destination = installer.safe_destination(home, "codex", "dayan-deck")
            destination.mkdir(parents=True)
            with self.assertRaises(FileExistsError):
                installer.install(home, "codex", "dayan-deck")


if __name__ == "__main__":
    unittest.main()
