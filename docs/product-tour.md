# The Dayan route

Dayan Agent Skills is not a shelf of prompts. It is a public control library for work where a fluent answer is not enough.

If you only have three minutes, follow this route:

1. **See the difference.** Open the [control-library demo](demos/control-library.html) and compare a prompt collection with a workflow that exposes Skills, fixtures, verifiers, and evidence boundaries.
2. **Choose the moment where work fails.** Start with [Wenzhen](../skills/dayan-wenzhen/SKILL.md) before the work, [Deck](../skills/dayan-deck/SKILL.md) while making the artifact, or [Adversarial Reviewer](../skills/dayan-adversarial-reviewer/SKILL.md) before release.
3. **Run one bounded trial.** Use the [temporary-home quickstart](quickstart.md), so the first trial does not touch your live agent configuration.
4. **Inspect the proof.** Read the matching [example run](../examples/runs/README.md), [fixture](fixtures/README.md), and deterministic verifier. Then read the [compatibility boundary](compatibility.md) before treating the result as evidence.

## The product in four layers

| Layer | What it does | What you can inspect |
| --- | --- | --- |
| **Skill** | Chooses a repeatable workflow and its trigger boundary. | `SKILL.md`, non-trigger rules, artifact contract |
| **Method** | Captures a judgment rule that should survive across tasks. | public method card, application steps, failure pattern |
| **Fixture** | Shows the shape of a useful or unsafe result. | accepted example, rejected example, public boundary |
| **Verifier** | Checks the part that should not depend on persuasion. | deterministic command, pass/fail output, non-claims |

The layers are deliberately separate. A Skill can guide work; a fixture can make the target visible; a verifier can check a narrow contract. None of them, alone, proves factual accuracy, visual quality, universal host compatibility, or business outcomes.

## Three golden routes

### 1. Before the work: `dayan-wenzhen`

Use it when a request already contains a solution or feels too vague to trust. It turns the request into a falsifiable hypothesis, a smallest reversible bet, a pause signal, human authority, and an evidence contract.

Start with the [Wenzhen demo](demos/wenzhen.html), then run:

```bash
DAYAN_TEST_HOME="$(mktemp -d)"
python3 installers/install.py dayan-wenzhen --agent codex --home "$DAYAN_TEST_HOME"
python3 skills/dayan-wenzhen/scripts/verify_contract.py \
  skills/dayan-wenzhen/examples/starter-contract.json
```

### 2. While making the artifact: `dayan-deck`

Use it when a presentation is technically complete but the decision is still hard to see. It gives each slide one narrative job, a coherent visual grammar, and a structural check before visual inspection.

Start with the [Deck demo](demos/deck.html) and inspect the [starter](../skills/dayan-deck/examples/starter.html).

### 3. Before release: `dayan-adversarial-reviewer`

Use it when “looks good” is being mistaken for “safe to ship”. It separates failure modes, maintainability traps, and trust boundaries, then returns a bounded `BLOCK`, `CONCERNS`, or `CLEAN` verdict.

Start with the [Reviewer demo](demos/reviewer.html) and run the [blocking fixture](../skills/dayan-adversarial-reviewer/examples/block-review.json).

## What a good first visit should answer

After one short trial, you should be able to answer:

- What kind of failure does this stop?
- What artifact does it produce?
- What does the verifier actually check?
- What remains a human judgment?
- Where would I stop, roll back, or ask for a second review?

If those answers are still unclear, the right next move is to improve the route—not to add another Skill.
