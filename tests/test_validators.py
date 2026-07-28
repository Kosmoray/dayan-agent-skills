from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


catalog_validator = load_module("catalog_validator", ROOT / "scripts/validate_catalog.py")
redline_scanner = load_module("redline_scanner", ROOT / "scripts/scan_public_redlines.py")


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))

    def write_payload(self, payload, directory: str) -> Path:
        path = Path(directory) / "catalog.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_real_catalog_passes(self):
        self.assertEqual(catalog_validator.validate(ROOT / "catalog.json"), [])

    def test_duplicate_name_fails(self):
        payload = copy.deepcopy(self.payload)
        payload["skills"][1]["name"] = payload["skills"][0]["name"]
        with tempfile.TemporaryDirectory(prefix="openclaw-catalog-test-", dir="/tmp") as directory:
            errors = catalog_validator.validate(self.write_payload(payload, directory))
        self.assertTrue(any("duplicate skill name" in error for error in errors))

    def test_ready_without_evidence_fails(self):
        payload = copy.deepcopy(self.payload)
        payload["skills"][0]["maintenance_status"] = "ready"
        with tempfile.TemporaryDirectory(prefix="openclaw-catalog-test-", dir="/tmp") as directory:
            errors = catalog_validator.validate(self.write_payload(payload, directory))
        self.assertTrue(any("is ready but" in error for error in errors))

    def test_beta_requires_publishable_artifacts_and_license(self):
        payload = copy.deepcopy(self.payload)
        payload["skills"][0]["source_license"] = "pending"
        with tempfile.TemporaryDirectory(prefix="openclaw-catalog-test-", dir="/tmp") as directory:
            errors = catalog_validator.validate(self.write_payload(payload, directory))
        self.assertTrue(any("is beta but source_license is unresolved" in error for error in errors))

    def test_declared_artifact_must_exist(self):
        payload = copy.deepcopy(self.payload)
        payload["skills"][0]["example"] = "examples/missing.html"
        with tempfile.TemporaryDirectory(prefix="openclaw-catalog-test-", dir="/tmp") as directory:
            errors = catalog_validator.validate(self.write_payload(payload, directory))
        self.assertTrue(any("example does not exist" in error for error in errors))


class RedlineTests(unittest.TestCase):
    def test_clean_fixture_passes(self):
        with tempfile.TemporaryDirectory(prefix="openclaw-redline-test-", dir="/tmp") as directory:
            path = Path(directory) / "SKILL.md"
            path.write_text("A public, brand-neutral example.", encoding="utf-8")
            self.assertEqual(redline_scanner.scan(Path(directory)), [])

    def test_private_path_and_secret_assignment_are_blocked_without_value_output(self):
        with tempfile.TemporaryDirectory(prefix="openclaw-redline-test-", dir="/tmp") as directory:
            path = Path(directory) / "fixture.txt"
            path.write_text(
                "source=/Users/example/private/file\napi_key=abcdefghijklmnop\n",
                encoding="utf-8",
            )
            findings = redline_scanner.scan(Path(directory))
        rules = {item["rule"] for item in findings}
        self.assertIn("private_user_path", rules)
        self.assertIn("credential_assignment", rules)
        self.assertTrue(all("abcdefghijklmnop" not in json.dumps(item) for item in findings))


if __name__ == "__main__":
    unittest.main()
