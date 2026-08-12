---
name: dayan-agent-factory
description: Compile an approved agent design into a portable, inspectable agent package with bounded tools, fixtures, and handoff instructions.
---

# Dayan Agent Factory

Use this Skill only after an agent design has a stable objective, role boundary, tool policy, output contract, and evaluation plan.

## Package

Create one directory containing:

- `AGENT.md`: role, objective, inputs, output, exclusions, and stop conditions;
- `tool-policy.json`: allowlisted capabilities and forbidden external effects;
- `output-schema.json`: machine-readable result contract;
- `examples/accepted.json` and `examples/rejected.json`;
- `EVALUATION.md`: tests, human takeover, cost/latency limits, and unresolved risks;
- `README.md`: install, run, verify, and remove instructions.

Reject packages with broad filesystem access, hidden state ownership, unbounded retries, self-approval of consequential actions, or no rejected fixture. Generate the package; do not install or deploy it without separate authorization.

