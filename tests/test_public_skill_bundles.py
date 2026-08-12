from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS = (
    "dayan-orient",
    "dayan-plan",
    "dayan-agent-designer",
    "dayan-agent-factory",
    "dayan-hook-factory",
    "dayan-html",
    "dayan-huashu-design",
    "dayan-diagram",
    "dayan-ai-seo",
)

CORE_LIBRARY_SKILLS = tuple(
    path.parent.parent.name
    for path in sorted((ROOT / "skills").glob("*/examples/starter.json"))
    if path.parent.parent.name not in PUBLIC_SKILLS
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validator = load_module("public_skill_validator", ROOT / "scripts/validate_public_skill.py")


class PublicSkillBundleTests(unittest.TestCase):
    def test_all_bundles_pass(self):
        for skill_name in PUBLIC_SKILLS + CORE_LIBRARY_SKILLS:
            with self.subTest(skill=skill_name):
                self.assertEqual(validator.verify(skill_name), [])


if __name__ == "__main__":
    unittest.main()
