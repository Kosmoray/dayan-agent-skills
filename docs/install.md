# Local installation candidate

The installer requires an explicit target home so smoke tests never write to the current user's live agent configuration.

```bash
python3 installers/install.py dayan-deck --agent codex --home /path/to/test-home
python3 installers/install.py dayan-deck --agent claude-code --home /path/to/test-home
python3 installers/install.py dayan-adversarial-reviewer --agent codex --home /path/to/test-home
python3 installers/install.py dayan-adversarial-reviewer --agent claude-code --home /path/to/test-home
```

Supported installation targets in this candidate:

- Codex-compatible Skill directory: `.codex/skills/<skill-name>`;
- Claude Code-compatible Skill directory: `.claude/skills/<skill-name>`.

These are verified packaging targets, not universal behavioral compatibility claims. A real agent trigger and output smoke test is still required before `compatible_agents` is populated.

The public beta performs new installs only. It refuses to overwrite an existing directory and does not ship an automated uninstall command. Remove only the exact installed directory after verifying its `.dayan-package.json` marker. Safe update and uninstall behavior remain on the public roadmap.
