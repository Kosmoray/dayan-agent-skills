# Example run: Deck from outline

## User input

```text
Make a short deck explaining why our agent workflow needs guardrails. Audience: engineering leads. Keep it practical.
```

## Skill to try

`dayan-deck`

## Expected direction

The Skill should produce a self-contained HTML deck where each slide has one job:

1. name the practical problem;
2. show the control-layer model;
3. show a concrete release path;
4. end with the next action.

## Minimal output request

```text
Create a four-slide HTML deck.
Use editable text, no remote runtime dependencies, keyboard navigation, print support, responsive layout, and reduced-motion handling.
After generation, run the structural verifier.
```

## Verification

```bash
python3 skills/dayan-deck/scripts/verify_deck.py output.html
```

## What to verify

- The deck is self-contained.
- Every slide has its own heading.
- Only one slide is active at load time.
- Audience-facing HTML contains no presenter notes or production reminders.
