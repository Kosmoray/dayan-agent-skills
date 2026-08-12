# Public tooling

These are the small tools that make the repository inspectable. They are intentionally local, explicit, and safe to run in a clone.

| Tool | Purpose | Command | Proves | Does not prove |
| --- | --- | --- | --- | --- |
| `installers/install.py` | Install or marker-guard update one Skill into an explicit home | `python3 installers/install.py dayan-wenzhen --agent codex --home "$DAYAN_TEST_HOME"` | package copy, destination safety, marker creation | live host UI loading |
| `scripts/compatibility_smoke.py` | Run clean-home package install smoke | `python3 scripts/compatibility_smoke.py --all-skills` | 56 Skills install across two target home styles | runtime behavior |
| `scripts/runtime_smoke.py` | Run offline lifecycle smoke | `python3 scripts/runtime_smoke.py --all-skills` | discovery, trigger routing, example command, non-trigger, safe update | LLM decision quality |
| `scripts/validate_release.py` | Run the release gate | `python3 scripts/validate_release.py` | required files, manifests, matrices, fixtures, examples, validators | external adoption |
| `scripts/validate_catalog.py` | Validate `catalog.json` schema | `python3 scripts/validate_catalog.py catalog.json` | catalog shape and local artifact links | Skill quality |
| `scripts/validate_public_skill.py` | Validate one shared-format Skill bundle | `python3 scripts/validate_public_skill.py dayan-orient` | bundle files, starter contract, public redlines | real-world usefulness |
| `scripts/scan_public_redlines.py` | Scan public files for configured redlines | `python3 scripts/scan_public_redlines.py docs` | configured public redline absence | legal clearance |
| `scripts/verify_examples.py` | Verify sanitized example runs | `python3 scripts/verify_examples.py` | example completeness, links, public boundaries | model repeatability |
| `scripts/verify_fixtures.py` | Verify artifact fixtures | `python3 scripts/verify_fixtures.py` | fixture structure, links, Skill references, boundaries | production results |
| `scripts/verify_good_first_issues.py` | Verify contribution tasks | `python3 scripts/verify_good_first_issues.py` | actionable small tasks with proof commands | contributor availability |
| `scripts/verify_site.py` | Verify the public discovery site | `python3 scripts/verify_site.py` | basic page structure, links, public claims | visual taste |
| `skills/dayan-deck/scripts/verify_deck.py` | Verify the Deck starter artifact | `python3 skills/dayan-deck/scripts/verify_deck.py skills/dayan-deck/examples/starter.html` | structural deck contract | presentation persuasion |
| `skills/dayan-wenzhen/scripts/verify_contract.py` | Verify a Wenzhen task contract | `python3 skills/dayan-wenzhen/scripts/verify_contract.py skills/dayan-wenzhen/examples/starter-contract.json` | required contract fields and risk boundaries | correct strategy |
| `skills/dayan-adversarial-reviewer/scripts/verify_review.py` | Verify an adversarial review verdict | `python3 skills/dayan-adversarial-reviewer/scripts/verify_review.py skills/dayan-adversarial-reviewer/examples/block-review.json` | review schema and verdict consistency | every missed risk |

## Tooling rules

- Tools must be explicit about inputs and outputs.
- Tools must not write to a user's live home unless an explicit `--home` or target path is supplied.
- Tools must print bounded evidence, not broad claims.
- Tools that scan for secrets must avoid echoing suspected secret values.
- Tools that update files must have marker checks, staging, or another visible safety boundary.

## Add a tool

Before adding a new public tool:

1. document the exact command in this file;
2. state what it proves and what it does not prove;
3. add a test or integrate it into `scripts/validate_release.py`;
4. run the release gate.
