from __future__ import annotations

import subprocess
import sys
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
        self.assertIn("host application discovery", result.stdout)

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
