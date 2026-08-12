# Local installation candidate

The installer requires an explicit target home so smoke tests never write to the current user's live agent configuration.

```bash
python3 installers/install.py dayan-deck --agent codex --home /path/to/test-home
python3 installers/install.py dayan-deck --agent claude-code --home /path/to/test-home
python3 installers/install.py dayan-adversarial-reviewer --agent codex --home /path/to/test-home
python3 installers/install.py dayan-adversarial-reviewer --agent claude-code --home /path/to/test-home
python3 installers/install.py dayan-wenzhen --agent codex --home /path/to/test-home
python3 installers/install.py dayan-wenzhen --agent claude-code --home /path/to/test-home
```

All 56 Skills listed in `catalog.json` use the same command. Replace the first argument with the selected Skill name.

Supported installation targets in this candidate:

- Codex-compatible Skill directory: `.codex/skills/<skill-name>`;
- Claude Code-compatible Skill directory: `.claude/skills/<skill-name>`.

These are verified packaging targets. The offline lifecycle smoke tests discovery, trigger routing, declared example commands, and safe update in temporary homes; product-version-specific host behavior still requires external reports before `compatible_agents` is populated.

By default the installer performs new installs only. It refuses to overwrite an existing directory.

Use `--update` only when replacing a Skill that was already installed from this package:

```bash
python3 installers/install.py dayan-deck \
  --agent codex \
  --home /path/to/test-home \
  --update
```

The update path replaces only directories whose `.dayan-package.json` marker matches `dayan-agent-skills`, the same Skill name, and the same target agent. The package does not ship an automated uninstall command. Remove only the exact installed directory after verifying its marker.
