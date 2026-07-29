# Public adversarial-review rubric

## Severity

### Critical

Use `CRITICAL` only when the evidence shows a credible path to data loss, unauthorized access, secret exposure, production outage, irreversible corruption, or an unsafe migration with no reliable recovery.

A critical finding forces the top-level verdict to `BLOCK`.

### Warning

Use `WARNING` for a likely boundary failure, missing rollback path, material regression risk, misleading success state, or maintenance trap that should be repaired or consciously accepted before release.

A warning forces at least `CONCERNS`.

### Note

Use `NOTE` for a low-risk improvement, localized clarity issue, or useful test enhancement. Notes alone do not prevent a `CLEAN` verdict.

## Evidence quality

A finding is actionable only when it contains:

- a repository-relative path;
- a positive line number;
- the input or state that triggers the problem;
- the concrete failure or harm;
- one bounded repair.

If a risk cannot be tied to those fields, place it under residual assumptions instead of inventing a finding.

## Verdict consistency

| Findings | Verdict |
| --- | --- |
| One or more critical findings | `BLOCK` |
| No critical findings and one or more warnings | `CONCERNS` |
| Notes only or no findings | `CLEAN` |

## Limits

This rubric supports structured engineering review. It does not certify security, legal compliance, performance, accessibility, privacy, or fitness for high-stakes use.
