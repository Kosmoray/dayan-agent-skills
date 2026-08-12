from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RuntimeSmokeTests(unittest.TestCase):
    def test_default_runtime_report_covers_three_featured_skills(self):
        result = subprocess.run(
            [sys.executable, "scripts/runtime_smoke.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Summary: `6/6 PASS`", result.stdout)
        self.assertIn("| `codex` | `dayan-wenzhen` | PASS | `dayan-wenzhen` |", result.stdout)
        self.assertIn("| `claude-code` | `dayan-deck` | PASS | `dayan-deck` |", result.stdout)
        self.assertIn("safe update passed", result.stdout)
        self.assertIn("actual host application UI loading", result.stdout)

    def test_all_skills_runtime_json_matrix_covers_both_targets(self):
        with tempfile.TemporaryDirectory() as temp:
            matrix = Path(temp) / "runtime.json"
            result = subprocess.run(
                [sys.executable, "scripts/runtime_smoke.py", "--all-skills", "--json-output", str(matrix)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(matrix.read_text(encoding="utf-8"))
            self.assertEqual(payload["skill_scope"], "all-public-beta-skills")
            self.assertEqual(payload["summary"], {"fail": 0, "pass": 112, "total": 112})
            self.assertEqual(len(payload["results"]), 112)

    def test_unknown_skill_fails_before_install(self):
        result = subprocess.run(
            [sys.executable, "scripts/runtime_smoke.py", "--skill", "dayan-missing"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown Skill", result.stdout)


if __name__ == "__main__":
    unittest.main()
