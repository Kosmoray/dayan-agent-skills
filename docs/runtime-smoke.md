# Runtime smoke evidence

`scripts/runtime_smoke.py` is an offline lifecycle harness for the public package. It uses a temporary home so it does not touch a user's live agent configuration.

## What it checks

For each selected Skill and target agent style, the harness verifies:

1. the Skill was installed into the expected clean-home directory;
2. `.dayan-package.json` identifies the package, Skill, and target agent;
3. installed Skills can be discovered by scanning the agent-style Skill directory;
4. the catalog trigger routes to the expected installed Skill;
5. the declared example command exits successfully;
6. a casual unrelated prompt does not route;
7. `installers/install.py --update` replaces only a matching Dayan-owned install.

## Run the featured smoke

```bash
python3 scripts/runtime_smoke.py
```

This covers `dayan-wenzhen`, `dayan-deck`, and `dayan-adversarial-reviewer` for Codex-style and Claude Code-style homes.

## Run the full lifecycle matrix

```bash
python3 scripts/runtime_smoke.py \
  --all-skills \
  --json-output docs/runtime-smoke.json
```

The checked-in matrix is [`runtime-smoke.json`](runtime-smoke.json).

## Boundary

This is stronger than package installation because it tests discovery, trigger routing, example execution, non-trigger behavior, and update safety. It still does not claim:

- actual host application UI loading;
- LLM model decision quality;
- networked marketplace install flows;
- uninstall behavior in a user's live configuration.
