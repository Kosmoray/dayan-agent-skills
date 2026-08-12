# Example run: Database performance list endpoint

## User input

```text
Review a list endpoint that loads projects with owner, tags, and recent activity for each row.
```

## Skill to try

`dayan-database-performance`

## Expected direction

The Skill should look for unbounded lists, N+1 queries, mixed read/write work, and missing indexes.

## Minimal output shape

```text
Risk:
The endpoint can issue one query for the project list, then one owner query, one tag query, and one activity query per project.

Required evidence:
Query count for 1, 25, and 100 rows; execution plan for filters and ordering; maximum page size.

Likely fix:
Use bounded pagination, preloaded associations or joins, targeted indexes, and separate activity summary materialization if needed.

Release condition:
Performance test passes under the agreed row count and query budget.
```

## What to verify

- The review asks for query count growth.
- It requires bounded pagination.
- It does not promise a database fix without an execution plan.
