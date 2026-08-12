# Example run: Wenzhen fuzzy request

## User input

```text
I want to add AI to our internal support workflow. Make it smart and reduce workload.
```

## Skill to try

`dayan-wenzhen`

## Expected direction

The Skill should not jump straight to a chatbot proposal. It should produce a task contract that separates:

- the likely real problem;
- plausible alternatives;
- the smallest reversible bet;
- authority and risk;
- evidence needed before implementation.

## Minimal output shape

```text
Best-current problem hypothesis:
Support work is slow because repeated intake, routing, and status-summary tasks are not standardized.

Alternative hypotheses:
1. The bottleneck is missing policy knowledge, not AI capability.
2. The bottleneck is unclear ownership after intake.
3. The bottleneck is measurement: the team cannot see where time is spent.

Smallest reversible bet:
Build a read-only triage assistant for 20 sanitized historical tickets. It drafts category, priority, missing information, and next owner. No customer message is sent automatically.

Human authority:
No external reply, policy decision, refund, escalation, or personnel judgment is automated.

Evidence to continue:
Compare draft triage accuracy and time saved against a human baseline.
```

## What to verify

- The output names a falsifiable hypothesis.
- It offers at least one non-AI or smaller alternative.
- It keeps consequential actions under human authority.
- It defines the next evidence checkpoint.
