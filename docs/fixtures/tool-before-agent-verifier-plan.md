# Tool-before-agent verifier plan

Skill: `dayan-hook-factory`

## Input

An open-source maintainer keeps reminding contributors not to ship public docs with placeholders, hidden production notes, or broad success claims.

## Output artifact

```md
# Public-doc verifier plan

## Repeated failure

Reader-facing docs sometimes include draft markers or unsupported claims.

## Deterministic rule

Block files under `docs/` when they contain configured placeholder phrases, credential-like assignments, or production-note labels.

## Accepted fixture

`docs/example-clean.md` contains only reader-facing content, scoped claims, and a verification note.

## Rejected fixture

`docs/example-draft.md` contains a visible production-note label and must fail.

## Agent workflow

The agent may edit docs, then must run:

```bash
python3 scripts/scan_public_redlines.py docs
```

If the command fails, the agent must report the blocked rule instead of rewriting the release claim.
```

## Verification

- The plan names a repeated failure.
- It defines one deterministic rule before adding agent behavior.
- It includes accepted and rejected fixture shapes.
- It gives one local verification command.

## Boundary

This fixture does not prove that the docs are persuasive, complete, legally cleared, or adopted by external users.
