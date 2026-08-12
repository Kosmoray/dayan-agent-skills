---
name: dayan-agent-designer
description: Decide whether a system needs agents, then define roles, state ownership, tools, boundaries, and evaluation before implementation.
---

# Dayan Agent Designer

Use this Skill when designing an agent or multi-agent system. Start with the least complex viable form:

`rule → pipeline → single agent → supervisor and specialists → parallel workers and reviewer`

Every escalation needs evidence that the simpler form fails.

## Design contract

- Task surface: objective, untrusted inputs, output schema, completion and stop conditions.
- Roles: one responsibility, one bounded input, one output contract, explicit exclusions, and a unique name.
- Tools: minimum permissions, read/write boundaries, external effects, and credential handling.
- State: one owner for each mutable state; no invisible shared memory.
- Coordination: dependencies, concurrency limits, timeout, retry, cancellation, and conflict resolution.
- Evaluation: accepted fixture, rejected fixture, adversarial case, cost/latency budget, and human takeover point.

Do not deploy or spawn agents unless the user separately authorizes execution. A design is not runtime evidence.

