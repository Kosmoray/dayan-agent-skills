# Example run: Support triage agent design

## User input

```text
Design an agent that helps our support team triage incoming tickets. It should not send replies automatically.
```

## Skill to try

`dayan-agent-designer`

## Expected direction

The Skill should define an agent contract, not a broad automation promise.

## Minimal output shape

```text
Agent responsibility:
Classify a ticket, identify missing information, suggest priority, and draft the next internal owner.

Allowed tools:
Read-only access to ticket text, public policy snippets, and historical category labels.

Denied actions:
No customer reply, refund, escalation, account change, or policy exception.

Memory:
No raw customer messages stored in long-term memory. Store only aggregate category patterns after review.

Evaluation:
Compare classification accuracy, missing-field detection, and human edit distance against a labeled set.
```

## What to verify

- Responsibilities are explicit.
- Tool access is bounded.
- Human authority remains clear.
- Evaluation is observable rather than aspirational.
