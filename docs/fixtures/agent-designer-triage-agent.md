# Support triage agent contract

Skill: `dayan-agent-designer`

## Input

A team wants an agent that reads incoming support tickets and prepares a triage draft without contacting customers or changing account data.

## Output artifact

### Responsibility

Create a triage note that helps a human support engineer decide priority and next action.

### Inputs

- ticket title;
- user-provided description;
- product area;
- visible error text;
- recent release notes supplied by the operator.

### Outputs

- priority proposal: `P0`, `P1`, `P2`, or `P3`;
- suspected product area;
- missing information;
- safest next human action;
- exact evidence copied from the ticket.

### Tools

Read-only ticket view and read-only documentation search.

### Hard boundaries

- do not send customer replies;
- do not change account state;
- do not infer billing, identity, or security facts without evidence;
- do not hide uncertainty.

### Evaluation

Five historical tickets are enough for a first fixture set: one outage, one known bug, one user setup issue, one unclear report, and one non-product request.

## Verification

- Every priority proposal cites ticket evidence.
- Missing information is explicit.
- No output pretends to have contacted a customer or modified data.

## Boundary

This contract does not prove a deployed agent, support accuracy, or production readiness. It is not a substitute for support ownership.
