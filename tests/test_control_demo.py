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


control_demo = load_module("control_demo_verifier", ROOT / "scripts/verify_control_demo.py")


class ControlDemoTests(unittest.TestCase):
    def test_control_library_demo_passes(self):
        self.assertEqual(control_demo.verify(), [])


if __name__ == "__main__":
    unittest.main()
