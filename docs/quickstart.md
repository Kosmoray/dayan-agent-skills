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

## Compatibility smoke

To generate a paste-ready clean-install report:

```bash
python3 scripts/compatibility_smoke.py
```

This checks packaging into temporary Codex-style and Claude Code-style homes. It does not claim host discovery or runtime triggering.

## What this proves

This quickstart proves package structure, installation into a clean home, and fixture-level verification for the selected Skill.

It does not prove that every host application version discovers and triggers the Skill identically. See [Compatibility evidence](compatibility.md).
