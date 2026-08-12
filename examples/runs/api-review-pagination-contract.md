# Example run: API pagination contract review

## User input

```text
Review this API change: GET /customers returns all customers for the current account. The frontend will filter locally.
```

## Skill to try

`dayan-api-design-reviewer`

## Expected direction

The Skill should review the endpoint as a durable contract, not just a route implementation.

## Minimal verdict shape

```text
Verdict: BLOCK

Contract issue:
An unbounded list endpoint can become slow, expensive, and difficult to change after clients depend on it.

Required contract:
Use pagination, stable sorting, filter parameters, maximum page size, and explicit authorization scope.

Compatibility:
Document default ordering and versioning before clients ship.

Release condition:
Add accepted fixtures for normal pagination and rejected fixtures for excessive limit, missing auth scope, and invalid cursor.
```

## What to verify

- The review names client compatibility risk.
- It requires bounded access.
- It asks for accepted and rejected fixtures.
