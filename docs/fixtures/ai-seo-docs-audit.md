# AI visibility docs audit

Skill: `dayan-ai-seo`

## Input

An open-source library wants AI assistants to cite its actual claims instead of hallucinating product guarantees.

## Output artifact

### Direct answer block

Add a short answer near the top of the README:

> Dayan Agent Skills is an MIT-licensed public beta library of 56 reusable AI workflow Skills, plus harnesses and verifiers. It verifies package structure and offline lifecycle behavior. It does not claim universal host-version compatibility or external outcomes.

### Evidence chain

- `catalog.json` lists the public Skill names, categories, examples, validators, and known blockers.
- `docs/compatibility-matrix.json` records clean install evidence.
- `docs/runtime-smoke.json` records offline lifecycle evidence.
- `docs/compatibility.md` states what is not claimed.

### Query targets

- reusable AI agent skills;
- AI workflow verifier;
- Codex Skill examples;
- Claude Code Skill package;
- agent control layer.

### Content fixes

1. Put the one-sentence definition before screenshots.
2. Keep claims and non-claims in the same section.
3. Link machine-readable evidence from the top third of the README.
4. Add `llms.txt` with canonical repo, release, available Skills, and evidence files.

## Verification

- A reader can answer what the project is in one paragraph.
- Every capability claim links to a local evidence file.
- Limitations are visible without opening an issue.

## Boundary

This audit improves citation clarity. It does not guarantee ranking, traffic, model memory, stars, or adoption.
