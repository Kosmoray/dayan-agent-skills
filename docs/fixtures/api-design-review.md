# Pagination API review

Skill: `dayan-api-design-reviewer`

## Input

A proposed endpoint returns all audit events for an organization:

```text
GET /v1/audit-events?organization_id=org_public_example
```

The draft response has no `limit`, no cursor, and no ordering contract.

## Output artifact

### Verdict

`BLOCK`

### Findings

1. The endpoint has unbounded response size.
2. Ordering is not specified, so clients cannot paginate safely later.
3. The query uses an organization identifier but does not state the authorization boundary.
4. Error cases do not distinguish invalid cursor, expired cursor, unauthorized organization, and empty result.

### Minimal safer contract

```text
GET /v1/audit-events?organization_id=org_public_example&limit=50&cursor=cursor_public_example
```

Response:

```json
{
  "items": [],
  "next_cursor": null,
  "order": "created_at_desc"
}
```

### Required before merge

- maximum `limit`;
- stable ordering;
- cursor format owned by the server;
- authorization statement;
- explicit empty-state response.

## Verification

- The verdict blocks the unbounded endpoint.
- The replacement contract includes `limit`, `cursor`, ordering, and empty-state behavior.
- The fixture contains no real organization identifier.

## Boundary

This review does not prove database performance or authorization implementation correctness.
