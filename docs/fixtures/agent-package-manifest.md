# Agent package manifest

Skill: `dayan-agent-factory`

## Input

A previously approved support triage agent design needs a package manifest before implementation.

## Output artifact

### Package name

`support-triage-draft-agent`

### Purpose

Prepare a triage draft for a human support engineer. The agent does not contact users or change account state.

### Files

- `agent.md`: role, responsibilities, boundaries, and escalation rules;
- `fixtures/outage-ticket.json`: accepted fixture;
- `fixtures/unclear-ticket.json`: boundary fixture;
- `verify_agent_contract.py`: checks manifest fields and fixture safety;
- `README.md`: install and review instructions.

### Required boundaries

- read-only inputs;
- no customer replies;
- no account mutation;
- no hidden priority escalation;
- all uncertainty visible.

### Release checks

- manifest parses;
- fixtures contain no secrets or real identifiers;
- accepted and boundary fixtures both pass the contract verifier;
- README states what the agent is not allowed to do.

## Verification

- Every packaged file has a purpose.
- The package includes at least one accepted fixture and one boundary fixture.
- Human authority remains explicit.

## Boundary

This fixture does not prove the agent is deployed, safe in production, or correct for real support workflows.
