# Public redline hook spec

Skill: `dayan-hook-factory`

## Input

A public documentation repository needs a deterministic pre-commit check that blocks common publication redlines before review.

## Output artifact

### Hook name

`public-redline-scan`

### Trigger

Run on changed Markdown, HTML, JSON, YAML, and plain-text files.

### Checks

- private machine path patterns;
- credential-like assignments;
- private key block headers;
- production-note phrases in audience-facing artifacts;
- unresolved placeholder phrases such as `TODO before publishing`.

### Allowed exceptions

- detector source code may contain pattern names;
- test fixtures may contain synthetic redline examples when the verifier confirms the value is not echoed.

### Failure output

Return file path, line number, rule name, and remediation. Do not print the suspected secret value.

## Verification

- A clean fixture passes.
- A private path fixture fails.
- A credential-like assignment fixture fails without echoing the value.
- Detector code and test fixtures are handled by explicit allow rules.

## Boundary

This hook does not prove legal clearance, factual accuracy, or ownership of every asset.
