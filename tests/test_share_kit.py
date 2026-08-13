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


share_kit = load_module("share_kit_verifier", ROOT / "scripts/verify_share_kit.py")


class ShareKitTests(unittest.TestCase):
    def test_share_kit_passes(self):
        self.assertEqual(share_kit.verify(), [])


if __name__ == "__main__":
    unittest.main()
