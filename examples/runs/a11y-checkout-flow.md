# Example run: Checkout flow accessibility audit

## User input

```text
Audit a checkout page for accessibility before release. The page has product summary, address, payment, and submit sections.
```

## Skill to try

`dayan-a11y-audit`

## Expected direction

The Skill should translate accessibility into user-visible ability: can someone see, navigate, understand, and complete the flow?

## Minimal output shape

```text
Critical checks:
- Every input has a programmatic label.
- Keyboard focus order follows the visual flow.
- Error messages are announced and tied to the field.
- Color is not the only signal for required or failed fields.
- The final submit action is reachable and named.

Release risk:
If payment errors are only visual, keyboard or screen-reader users may be blocked from checkout.

Evidence needed:
Keyboard-only pass, screen-reader smoke, contrast check, and rejected fixture for unlabeled payment fields.
```

## What to verify

- Findings map to user ability, not only WCAG labels.
- Critical checkout blockers are separated from polish issues.
- Evidence is requested before release.
