# Example run: Adversarial review verdict

## User input

```text
Review this change before release:

- Adds a CSV import endpoint.
- Accepts uploaded files from authenticated users.
- Parses rows and writes records to the database.
- Logs failed rows for debugging.
```

## Skill to try

`dayan-adversarial-reviewer`

## Expected direction

The review should not return a generic "looks good." It should split the assessment into failure modes, maintainability, and trust boundaries.

## Minimal verdict shape

```text
Verdict: BLOCK

Failure mode:
Large or malformed CSV files can exhaust memory or partially write records without a resumable boundary.

Maintainability:
Parsing, validation, persistence, and logging are described as one endpoint responsibility. The change needs explicit contracts between those steps.

Trust boundary:
Uploaded file content and failed-row logs are untrusted. Logs must not contain raw sensitive row data.

Release condition:
Add file-size limits, streaming or bounded parsing, transactional behavior, sanitized logging, and accepted/rejected fixtures before release.
```

## What to verify

- The verdict is tied to concrete release conditions.
- Untrusted input and logs are reviewed as trust boundaries.
- The review distinguishes blocking risk from optional cleanup.
