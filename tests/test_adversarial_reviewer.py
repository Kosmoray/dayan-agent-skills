from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills/dayan-adversarial-reviewer"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


review_verifier = load_module(
    "review_verifier",
    SKILL_ROOT / "scripts/verify_review.py",
)


class AdversarialReviewVerifierTests(unittest.TestCase):
    def setUp(self):
        self.clean = json.loads(
            (SKILL_ROOT / "examples/clean-review.json").read_text(encoding="utf-8")
        )
        self.block = json.loads(
            (SKILL_ROOT / "examples/block-review.json").read_text(encoding="utf-8")
        )

    def verify_payload(self, payload: dict) -> list[str]:
        with tempfile.TemporaryDirectory(prefix="openclaw-review-test-", dir="/tmp") as directory:
            path = Path(directory) / "review.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return review_verifier.verify(path)

    def test_public_fixtures_pass(self):
        self.assertEqual(
            review_verifier.verify(SKILL_ROOT / "examples/clean-review.json"),
            [],
        )
        self.assertEqual(
            review_verifier.verify(SKILL_ROOT / "examples/block-review.json"),
            [],
        )

    def test_critical_finding_requires_block(self):
        payload = copy.deepcopy(self.block)
        payload["verdict"] = "CLEAN"
        errors = self.verify_payload(payload)
        self.assertTrue(any("CRITICAL finding requires verdict BLOCK" in error for error in errors))

    def test_warning_requires_concerns(self):
        payload = copy.deepcopy(self.clean)
        payload["findings"][0]["severity"] = "WARNING"
        errors = self.verify_payload(payload)
        self.assertTrue(any("WARNING without CRITICAL requires verdict CONCERNS" in error for error in errors))

    def test_concerns_with_warning_passes(self):
        payload = copy.deepcopy(self.clean)
        payload["verdict"] = "CONCERNS"
        payload["findings"][0]["severity"] = "WARNING"
        self.assertEqual(self.verify_payload(payload), [])

    def test_absolute_and_parent_paths_fail(self):
        for unsafe_path in ("/tmp/source.py", "../source.py", "src\\source.py"):
            payload = copy.deepcopy(self.clean)
            payload["findings"][0]["evidence"]["path"] = unsafe_path
            errors = self.verify_payload(payload)
            self.assertTrue(any("must be repository-relative" in error for error in errors))

    def test_missing_residual_lens_fails(self):
        payload = copy.deepcopy(self.clean)
        del payload["residual_assumptions"]["trust_boundary"]
        errors = self.verify_payload(payload)
        self.assertTrue(any("residual_assumptions missing fields" in error for error in errors))

    def test_credential_value_is_rejected_without_echoing_value(self):
        payload = copy.deepcopy(self.clean)
        sensitive_value = "api_key=abcdefghijklmnop"
        payload["summary"] = sensitive_value
        errors = self.verify_payload(payload)
        self.assertTrue(any("credential value detected" in error for error in errors))
        self.assertTrue(all(sensitive_value not in error for error in errors))

    def test_credential_token_is_rejected_without_echoing_value(self):
        payload = copy.deepcopy(self.clean)
        sensitive_value = "gho_abcdefghijklmnopqrstuvwxyz"
        payload["summary"] = sensitive_value
        errors = self.verify_payload(payload)
        self.assertTrue(any("credential token detected" in error for error in errors))
        self.assertTrue(all(sensitive_value not in error for error in errors))

    def test_duplicate_titles_fail(self):
        payload = copy.deepcopy(self.block)
        payload["findings"][1]["title"] = payload["findings"][0]["title"]
        errors = self.verify_payload(payload)
        self.assertTrue(any("duplicate finding title" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
