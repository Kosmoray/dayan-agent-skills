# Human authority ledger

Skill: `dayan-agent-designer`

## Input

Design an agent-assisted release workflow for a public documentation repository. The agent may edit files and run local checks, but publication and external communication must remain controlled.

## Output artifact

```md
# Release authority ledger

| Action | Authority | Required evidence | Stop signal |
| --- | --- | --- | --- |
| Draft docs | agent-execute | diff is limited to repository files | request changes scope |
| Run local verifier | agent-execute | command output and exit code | verifier fails |
| Commit | agent-execute | clean diff and passing release gate | unrelated user changes overlap |
| Tag and push | human-review | explicit release instruction and passing checks | version conflict |
| Public release notes | human-review | tag exists and CI is green | unsupported claim |
| External announcement | human-only | platform-specific approval | missing approval |

## Handoff rule

The agent may prepare evidence, but must not convert missing approval into an assumption.
```

## Verification

- Every consequential action has an authority level.
- Each boundary has required evidence.
- The external announcement remains human-only.
- The stop signal is visible before execution.

## Boundary

This fixture does not prove legal compliance, production safety, or that every organization should use the same authority levels.
