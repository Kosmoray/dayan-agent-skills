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
