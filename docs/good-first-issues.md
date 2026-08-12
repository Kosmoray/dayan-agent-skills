# Good first issues

These are small, reviewable contribution tasks. Each one should improve the single repository rather than creating a new package.

| ID | Task | Skill | Files to touch | Expected proof | Size |
| --- | --- | --- | --- | --- | --- |
| GFI-001 | Add one artifact fixture for `dayan-diagram` | `dayan-diagram` | `docs/fixtures/README.md`, `docs/fixtures/<name>.md` | `python3 scripts/verify_fixtures.py` | small |
| GFI-002 | Add one accepted and one boundary fixture idea for `dayan-agent-factory` | `dayan-agent-factory` | `docs/fixtures/agent-package-manifest.md` or a new fixture | `python3 scripts/verify_fixtures.py` | small |
| GFI-003 | Improve one example run with a clearer non-claim boundary | any listed example Skill | `examples/runs/*.md` | `python3 scripts/verify_examples.py` | small |
| GFI-004 | Add a missing local link from a README section to the fixture gallery | documentation | `README.md`, `README.zh-CN.md`, or `docs/quickstart.md` | `python3 scripts/validate_release.py` | small |
| GFI-005 | Add one rejected/boundary case to a public bundle validator proposal | any public beta Skill | `skills/<skill>/examples/` or `docs/fixtures/` | relevant validator plus `python3 scripts/validate_release.py` | medium |
| GFI-006 | Improve the compatibility issue template with one field that helps reproduce failures | compatibility | `.github/ISSUE_TEMPLATE/compatibility-report.yml` | `python3 scripts/validate_release.py` | small |
| GFI-007 | Add one artifact fixture for visual review | `dayan-deck` or `dayan-html` | `docs/fixtures/README.md`, `docs/fixtures/<name>.md` | `python3 scripts/verify_fixtures.py` | small |
| GFI-008 | Add one AI-visibility query target and evidence chain to a fixture | `dayan-ai-seo` | `docs/fixtures/ai-seo-docs-audit.md` | `python3 scripts/verify_fixtures.py` | small |

## Rules

- Keep the change public and synthetic.
- Do not include customer data, secrets, private paths, or real organization identifiers.
- Add a boundary sentence that says what the contribution does not prove.
- Prefer one small fixture, verifier improvement, or documentation link over a large speculative rewrite.

## Before submitting

Run the smallest relevant verifier, then run:

```bash
python3 scripts/validate_release.py
python3 -m unittest discover -s tests -v
```
