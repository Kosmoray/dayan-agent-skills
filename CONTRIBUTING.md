# Contributing

Thank you for helping make AI control layers more useful and inspectable.

## Before opening a pull request

1. Describe one repeatable user problem.
2. Keep the trigger and non-trigger boundary explicit.
3. Add one accepted fixture.
4. Add one rejected, unsafe, or boundary fixture.
5. Add a deterministic validator when practical; otherwise define the human-review boundary.
6. Record the source and license of every borrowed asset or implementation.
7. Run:

```bash
python3 scripts/validate_catalog.py catalog.json
python3 scripts/scan_public_redlines.py skills
python3 scripts/verify_fixtures.py
python3 scripts/verify_methods.py
python3 scripts/verify_positioning.py
python3 scripts/verify_good_first_issues.py
python3 scripts/verify_tooling.py
python3 scripts/validate_release.py
python3 -m unittest discover -s tests -v
```

Do not include customer data, credentials, private paths, hidden prompts, unlicensed assets, or claims that the tests do not prove.

## Proposing a Skill

Open a Skill proposal issue. Explain:

- who repeatedly needs it;
- what artifact it should create;
- why a current Skill cannot cover it;
- how a maintainer can verify success;
- which consequential actions retain human authority.

Small, evidenced Skills are preferred over large speculative frameworks.

## Good first issues

If you want a bounded first contribution, start with [`docs/good-first-issues.md`](docs/good-first-issues.md). Most good first issues should touch one fixture, one example, one issue template, or one documentation link.

If you want to improve the repository tooling layer, start with [`docs/tooling.md`](docs/tooling.md) and add one verifier-backed change.

## Reporting compatibility

Use the compatibility report issue template when you test a clean install in Codex, Claude Code, or another host. The most useful report includes the host version, OS, exact install command, selected Skill, discovery result, trigger result, and the smallest output that proves the behavior.

## Turning a pattern into a Skill

Start with the [From conversation to Skill](docs/playbooks/from-conversation-to-skill.md) playbook. A good public contribution should include an accepted example, a rejected or boundary example, provenance, sanitization notes, and either a deterministic validator or a clear human-review contract.
