# Example run: Public redline hook

## User input

```text
Create a guardrail that blocks public docs if they contain secrets, private paths, or internal notes.
```

## Skill to try

`dayan-hook-factory`

## Expected direction

The Skill should recommend a deterministic hook or script before relying on a model review.

## Minimal output shape

```text
Hook goal:
Block public-facing files that contain credential-like assignments, private key headers, private local paths, or production notes.

Scope:
docs/, README files, examples/, and public Skill packages.

Accepted fixture:
A clean markdown file with public links and no private paths.

Rejected fixture:
A markdown file containing a private local path, a credential-like assignment, or audience-visible production notes.

Failure mode:
The hook must report the file and pattern label without printing secret values.
```

## What to verify

- The check is deterministic.
- Rejected examples exist.
- Secret values are not echoed.
- The hook scope is narrow enough to avoid noisy blocking.
