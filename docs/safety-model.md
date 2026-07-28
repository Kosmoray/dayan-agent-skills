# Safety model

Public Skills are instructions and optional deterministic helpers. They do not transfer responsibility for consequential actions.

## Default boundaries

- Read-only inspection may run when it is scoped to user-provided material.
- File mutation must stay inside the explicit task workspace.
- Deletion, credential changes, spending, publication, production deployment, and external messages require explicit approval.
- High-stakes legal, medical, financial, security, or employment outputs require qualified human review.
- Validators report what they checked and what remains unverified.

## Release safety evidence

Every ready Skill needs:

- one accepted fixture;
- one rejected or unsafe fixture;
- a deterministic validator where practical;
- explicit human-review and stop conditions;
- a public redline scan;
- license and third-party asset review.
