---
name: dayan-hook-factory
description: Design a deterministic, least-privilege lifecycle hook with explicit triggers, failure policy, tests, and rollback.
---

# Dayan Hook Factory

Use a hook only for a frequent action with a stable trigger and predictable failure behavior. Prefer a command or checklist for low-frequency work.

## Contract

1. Name one lifecycle event and the narrowest matcher.
2. Use an explicit executable path, argument list, timeout, and project-local scope.
3. Make the command deterministic, idempotent, and safe when invoked twice.
4. Choose fail-open for productivity assistance or fail-closed for a proven safety invariant; document the tradeoff.
5. Provide accepted, ignored, malformed, timeout, and repeated-event fixtures.
6. Provide logs that name the rule without exposing content or credentials.
7. Provide a rollback that disables exactly this hook.

Do not auto-install hooks or edit user-level configuration without explicit approval. Hooks must not delete, publish, send, change credentials, or execute downloaded content.

