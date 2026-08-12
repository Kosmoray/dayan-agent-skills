# Wenzhen contract schema

`verify_contract.py` accepts a JSON object with this required shape:

```json
{
  "schema_version": 1,
  "title": "short working title",
  "triage": {
    "work_type": "research",
    "risk_level": "L1",
    "allowed_action": "review public information and prepare an internal comparison",
    "release_authority": "project owner",
    "minimum_evidence": "two current primary sources"
  },
  "hypothesis": {
    "surface_request": "what was asked for",
    "best_current_hypothesis": "the current explanation",
    "supporting_facts": ["verified observation"],
    "alternatives": ["plausible alternative"],
    "falsification_signal": "an observable result that would change the conclusion"
  },
  "contract": {
    "goal": "what should change and who owns that goal",
    "outcome": "the real-world success condition",
    "context": "verified facts, assumptions, unknowns, and available resources",
    "risks_review": "restrictions, review point, stop condition, and rollback boundary",
    "output": "the artifact or permitted action for this stage",
    "evidence": "what evidence is required before claiming success"
  },
  "options": {
    "current_route": "the current route",
    "alternative_route": "a credible alternative",
    "third_route": "a route that changes the framing",
    "defer_or_shrink": "the no-action, defer, or smaller-bet option"
  },
  "reversible_bet": {
    "next_step": "smallest reversible test",
    "expected_signal": "leading signal expected",
    "pause_signal": "signal that triggers a pause",
    "checkpoint": "when the test will be reviewed",
    "continue_evidence": "new evidence needed to continue",
    "rollback": "how the test is stopped or reversed"
  },
  "next_route": "research"
}
```

Allowed `work_type` values are `answer`, `decision`, `research`, `build`, `experiment`, and `specialist_review`. Allowed `risk_level` values are `L0` through `L3`.

For `L2` and `L3`, the contract must designate a human release authority and describe a review or stop boundary. The verifier rejects output text that presents publishing, sending, spending, deployment, credential changes, deletion, or signing as currently allowed for those levels.

