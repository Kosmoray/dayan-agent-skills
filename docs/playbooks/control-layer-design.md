# Control-layer design

Use this when you have a repeated AI workflow and need to decide what to build.

## Decision ladder

| Problem shape | Build | Why |
| --- | --- | --- |
| The same check catches the same failure every time | deterministic script or hook | cheaper, testable, fewer model degrees of freedom |
| The workflow has a repeatable trigger and artifact | Skill | the model needs judgment, but the boundary is stable |
| The work spans multiple tools, memory, and handoffs | agent contract | coordination matters more than a single prompt |
| The output is consequential or public | verifier plus human release | fluent generation must not approve itself |

## Minimum contract

Write this before implementation:

```text
Repeated problem:
User trigger:
Non-trigger:
Allowed actions:
Human authority:
Artifact:
Accepted example:
Rejected or boundary example:
Verifier or review rule:
Known evidence gap:
```

## Stop conditions

Do not promote a workflow to a public Skill when:

- it only describes one private project;
- the trigger needs private context to make sense;
- there is no accepted example;
- there is no rejected example or boundary;
- publication would expose customer material, credentials, private paths, or internal strategy.

## Upgrade path

1. Checklist: stable human process.
2. Skill: stable trigger plus model judgment.
3. Hook or verifier: stable failure pattern.
4. Agent: multiple responsibilities, tools, and state.
5. Marketplace package: install, provenance, sanitization, validation, and contribution route.
