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


good_first_issues = load_module("good_first_issue_verifier", ROOT / "scripts/verify_good_first_issues.py")


class GoodFirstIssueTests(unittest.TestCase):
    def test_good_first_issue_list_passes(self):
        self.assertEqual(good_first_issues.verify(), [])


if __name__ == "__main__":
    unittest.main()
