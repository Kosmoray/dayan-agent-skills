# Compatibility evidence

Compatibility is earned by a clean temporary-home installation and a behavior smoke test. A format that resembles an agent's Skill convention is not sufficient evidence.

## Current matrix

| Target | Package install | Discovery evidence | Trigger evidence | Status |
| --- | --- | --- | --- | --- |
| Codex-style home | PASS in isolated temporary homes | PASS in offline lifecycle smoke | PASS in offline lifecycle smoke | package + offline lifecycle verified |
| Claude Code-style home | PASS in isolated temporary homes | PASS in offline lifecycle smoke | PASS in offline lifecycle smoke | package + offline lifecycle verified |
| Other hosts | Not claimed | Not claimed | Not claimed | proposal welcome |

The installer writes to `.codex/skills/<skill-name>` or `.claude/skills/<skill-name>` under the explicit `--home` path. It refuses to overwrite an existing Skill directory.

## One-command package smoke

Run this before opening a compatibility issue:

```bash
python3 scripts/compatibility_smoke.py
```

Default behavior:

- creates a temporary clean home;
- installs `dayan-wenzhen` into Codex-style and Claude Code-style Skill directories;
- checks `SKILL.md` and `.dayan-package.json`;
- prints a paste-ready Markdown report;
- removes the temporary home.

Try additional Skills:

```bash
python3 scripts/compatibility_smoke.py \
  --skill dayan-deck \
  --skill dayan-adversarial-reviewer
```

Smoke every public beta Skill and write a machine-readable matrix:

```bash
python3 scripts/compatibility_smoke.py \
  --all-skills \
  --json-output docs/compatibility-matrix.json
```

The current checked-in matrix is [`docs/compatibility-matrix.json`](compatibility-matrix.json). It proves clean package installation for every public beta Skill across both packaging targets.

Keep the temporary home only when you need to inspect it:

```bash
python3 scripts/compatibility_smoke.py --keep-home
```

## Offline lifecycle smoke

Run this after package smoke when you want a stronger local contract:

```bash
python3 scripts/runtime_smoke.py
```

Default behavior:

- creates a temporary clean home;
- installs the three featured Skills into Codex-style and Claude Code-style Skill directories;
- discovers installed Skills from `.dayan-package.json` markers and `SKILL.md`;
- routes each Skill's catalog trigger to the expected installed Skill;
- runs each Skill's declared example command;
- reruns installation with `--update` and replaces only matching Dayan-owned directories;
- verifies that an unrelated casual prompt does not route.

Run the full 56-Skill lifecycle matrix:

```bash
python3 scripts/runtime_smoke.py \
  --all-skills \
  --json-output docs/runtime-smoke.json
```

The current checked-in runtime matrix is [`docs/runtime-smoke.json`](runtime-smoke.json). It proves offline discovery, trigger routing, declared example command execution, non-trigger rejection, and safe update across 56 Skills and both packaging targets.

It still does not prove actual product UI loading, LLM model decision quality, networked marketplace flows, or uninstall behavior in a live user configuration.

## Required evidence per supported agent

1. documented destination and discovery mechanism;
2. clean install;
3. one successful trigger;
4. one non-trigger or rejected input;
5. update path;
6. uninstall path;
7. captured tool and version information.

The catalog intentionally contains empty `compatible_agents` arrays until this evidence exists.

## Report a clean-environment result

Open a compatibility report with:

- host application and version;
- OS;
- exact install command;
- `scripts/compatibility_smoke.py` output;
- `docs/compatibility-matrix.json` if you ran the all-Skill matrix;
- `scripts/runtime_smoke.py` output or `docs/runtime-smoke.json` if you ran the lifecycle matrix;
- selected Skill;
- whether the host discovered it;
- one successful trigger or the exact failure;
- any relevant output with secrets and private paths removed.
