# False-positive control review

Skill: `dayan-adversarial-reviewer`

## Input

A generated landing page looks polished, loads without script errors, and passes a structural HTML check. The team wants to mark it ready for public launch.

## Output artifact

```md
# False-positive review

Verdict: CONCERNS

## Passing signals

- The page renders.
- The headings are readable.
- The local structure check exits successfully.

## Missing proof

- No source is attached for the headline outcome claim.
- The call to action points to a placeholder form.
- Mobile review has not been captured.
- No human owner has approved public release.

## Required next evidence

1. Replace or cite the outcome claim.
2. Verify the call to action target.
3. Add mobile screenshot evidence.
4. Record human approval before publishing.

## Non-claim

The current PASS signal proves structure, not launch readiness.
```

## Verification

- The review separates passing signals from missing proof.
- It rejects launch readiness without dismissing useful structure evidence.
- It names the next evidence required to change the verdict.

## Boundary

This fixture does not prove conversion, market demand, visual taste, or legal clearance.
