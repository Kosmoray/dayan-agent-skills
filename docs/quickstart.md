# Quickstart

Use this path when you want to inspect the library without touching your live agent configuration.

## 1. Clone

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills
```

## 2. Install one Skill into a temporary home

```bash
DAYAN_TEST_HOME="$(mktemp -d)"

python3 installers/install.py dayan-wenzhen \
  --agent codex \
  --home "$DAYAN_TEST_HOME"
```

The installer creates:

```text
$DAYAN_TEST_HOME/.codex/skills/dayan-wenzhen/
```

For Claude Code packaging, change the target:

```bash
python3 installers/install.py dayan-wenzhen \
  --agent claude-code \
  --home "$DAYAN_TEST_HOME"
```

## 3. Inspect what was installed

```bash
find "$DAYAN_TEST_HOME" -maxdepth 4 -type f | sort
```

Every installed Skill includes a `.dayan-package.json` marker so you can tell it came from this package.

## 4. Run a deterministic verifier

```bash
python3 skills/dayan-wenzhen/scripts/verify_contract.py \
  skills/dayan-wenzhen/examples/starter-contract.json
```

Expected result:

```text
PASS: starter-contract.json satisfies the Wenzhen contract
```

## 5. Pick the next Skill

- Vague request or risky task: `dayan-wenzhen`
- Presentation or visual artifact: `dayan-deck`
- Code or release review: `dayan-adversarial-reviewer`
- Unknown repository: `dayan-orient`
- Agent system design: `dayan-agent-designer`

See [Choose a Skill](choose-a-skill.md) for the complete route.

## 6. Inspect output fixtures

Use the [artifact fixtures](fixtures/README.md) when you want to see copyable output shapes before running a full workflow:

- repository orientation map;
- support triage agent contract;
- public redline hook spec;
- pagination API review;
- AI visibility docs audit.

Verify them with:

```bash
python3 scripts/verify_fixtures.py
```

## Compatibility smoke

To generate a paste-ready clean-install report:

```bash
python3 scripts/compatibility_smoke.py
```

This checks packaging into temporary Codex-style and Claude Code-style homes. It does not claim host discovery or runtime triggering.

To smoke all public beta Skills and produce JSON:

```bash
python3 scripts/compatibility_smoke.py \
  --all-skills \
  --json-output docs/compatibility-matrix.json
```

## Runtime smoke

To test the offline lifecycle contract:

```bash
python3 scripts/runtime_smoke.py
```

This installs into a temporary home, discovers installed Skills from agent-style directories, routes catalog trigger text to the expected Skill, runs the declared example command, and verifies marker-guarded `--update`.

To run the same lifecycle smoke for all public beta Skills:

```bash
python3 scripts/runtime_smoke.py \
  --all-skills \
  --json-output docs/runtime-smoke.json
```

## What this proves

This quickstart proves package structure, installation into a clean home, fixture-level verification, offline discovery, trigger routing, and safe update for the selected Skill.

It does not prove that every host application version loads the Skill UI or that every model routes identically. See [Compatibility evidence](compatibility.md).
