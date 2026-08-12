from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CompatibilitySmokeTests(unittest.TestCase):
    def test_default_report_installs_wenzhen_for_both_targets(self):
        result = subprocess.run(
            [sys.executable, "scripts/compatibility_smoke.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Package release", result.stdout)
        self.assertIn("| `codex` | `dayan-wenzhen` | PASS |", result.stdout)
        self.assertIn("| `claude-code` | `dayan-wenzhen` | PASS |", result.stdout)
        self.assertIn("Summary: `2/2 PASS`", result.stdout)
        self.assertIn("host application discovery", result.stdout)

    def test_all_skills_json_matrix_covers_both_targets(self):
        with tempfile.TemporaryDirectory() as temp:
            matrix = Path(temp) / "matrix.json"
            result = subprocess.run(
                [sys.executable, "scripts/compatibility_smoke.py", "--all-skills", "--json-output", str(matrix)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = __import__("json").loads(matrix.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["total"], 112)
            self.assertEqual(payload["summary"]["pass"], 112)
            self.assertEqual(payload["summary"]["fail"], 0)
            self.assertEqual(payload["skill_scope"], "all-public-beta-skills")

    def test_all_skills_and_explicit_skill_conflict(self):
        result = subprocess.run(
            [sys.executable, "scripts/compatibility_smoke.py", "--all-skills", "--skill", "dayan-wenzhen"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("either --all-skills or --skill", result.stdout)

    def test_unknown_skill_fails_without_installing(self):
        result = subprocess.run(
            [sys.executable, "scripts/compatibility_smoke.py", "--skill", "dayan-missing"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown Skill", result.stdout)


if __name__ == "__main__":
    unittest.main()
