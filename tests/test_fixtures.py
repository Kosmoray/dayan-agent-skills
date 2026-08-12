from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


fixtures = load_module("fixture_verifier", ROOT / "scripts/verify_fixtures.py")


class FixtureTests(unittest.TestCase):
    def test_public_artifact_fixtures_pass(self):
        self.assertEqual(fixtures.verify(), [])


if __name__ == "__main__":
    unittest.main()
