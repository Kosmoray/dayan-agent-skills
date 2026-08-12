from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills/dayan-wenzhen"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


contract_verifier = load_module("contract_verifier", SKILL_ROOT / "scripts/verify_contract.py")


class WenzhenVerifierTests(unittest.TestCase):
    def setUp(self):
        self.starter = json.loads((SKILL_ROOT / "examples/starter-contract.json").read_text(encoding="utf-8"))
        self.rejected = SKILL_ROOT / "examples/rejected-missing-stop.json"

    def verify_payload(self, payload: dict) -> list[str]:
        with tempfile.TemporaryDirectory(prefix="dayan-wenzhen-test-", dir="/tmp") as directory:
            path = Path(directory) / "contract.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return contract_verifier.verify(path)

    def test_starter_fixture_passes(self):
        self.assertEqual(contract_verifier.verify(SKILL_ROOT / "examples/starter-contract.json"), [])

    def test_rejected_fixture_fails_for_unsafe_l2_action(self):
        errors = contract_verifier.verify(self.rejected)
        self.assertTrue(any("must not authorize" in error for error in errors))

    def test_missing_defer_option_fails(self):
        payload = copy.deepcopy(self.starter)
        del payload["options"]["defer_or_shrink"]
        errors = self.verify_payload(payload)
        self.assertTrue(any("options missing fields" in error for error in errors))

    def test_l3_needs_a_review_or_stop_boundary(self):
        payload = copy.deepcopy(self.starter)
        payload["triage"]["risk_level"] = "L3"
        payload["contract"]["risks_review"] = "A qualified person is named."
        errors = self.verify_payload(payload)
        self.assertTrue(any("must name a review or stop boundary" in error for error in errors))

    def test_private_path_is_rejected(self):
        payload = copy.deepcopy(self.starter)
        payload["contract"]["context"] = "Read a file from /Users/example/private-note."
        errors = self.verify_payload(payload)
        self.assertIn("private machine path detected", errors)


if __name__ == "__main__":
    unittest.main()

