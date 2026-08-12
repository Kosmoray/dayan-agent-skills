# Compatibility evidence

Compatibility is earned by a clean temporary-home installation and a behavior smoke test. A format that resembles an agent's Skill convention is not sufficient evidence.

## Current matrix

| Target | Package install | Discovery evidence | Trigger evidence | Status |
| --- | --- | --- | --- | --- |
| Codex-style home | PASS in isolated temporary homes | Pending external reports | Pending external reports | packaging verified, runtime unclaimed |
| Claude Code-style home | PASS in isolated temporary homes | Pending external reports | Pending external reports | packaging verified, runtime unclaimed |
| Other hosts | Not claimed | Not claimed | Not claimed | proposal welcome |

The installer writes to `.codex/skills/<skill-name>` or `.claude/skills/<skill-name>` under the explicit `--home` path. It refuses to overwrite an existing Skill directory.

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
- selected Skill;
- whether the host discovered it;
- one successful trigger or the exact failure;
- any relevant output with secrets and private paths removed.
