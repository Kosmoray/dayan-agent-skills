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


methods = load_module("methods_verifier", ROOT / "scripts/verify_methods.py")


class MethodTests(unittest.TestCase):
    def test_public_method_cards_pass(self):
        self.assertEqual(methods.verify(), [])


if __name__ == "__main__":
    unittest.main()
