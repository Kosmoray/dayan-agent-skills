# Control library, not a prompt collection

Dayan Agent Skills is not a folder of clever prompts. It is a public control library for making probabilistic AI work more repeatable, inspectable, and safe to hand off.

## The difference

| Prompt collection | Control library |
| --- | --- |
| Starts from what to say to a model | Starts from the workflow failure to control |
| Optimizes for impressive output | Optimizes for repeatable decisions and evidence |
| Trusts the model to remember constraints | Puts repeated constraints into Skills, fixtures, hooks, and verifiers |
| Treats a good answer as success | Separates artifact ready, internally verified, human accepted, released, externally observed, and economically validated |
| Hides unsafe boundaries in long instructions | Names authority, stop conditions, and non-claims beside the artifact |
| Grows by adding more prompts | Grows by adding reusable contracts, examples, tools, tests, and contribution paths |

## Five layers

1. **Skill** — when to use the workflow, when not to use it, what artifact to create, and where authority stops.
2. **Method** — the reusable judgment rule behind a family of Skills.
3. **Fixture** — a public, copyable example of what useful output looks like.
4. **Verifier** — a deterministic or checklist-based way to test the parts that should not depend on taste.
5. **Evidence boundary** — what the repository has proved and what it has not proved yet.

## A concrete example

`dayan-wenzhen` does not only say “ask better questions.” It packages a task-contract workflow:

- input risk and authority are named before solution work starts;
- the current problem hypothesis must be falsifiable;
- alternatives and defer/shrink options remain visible;
- high-risk actions require review boundaries;
- the starter contract is checked by `skills/dayan-wenzhen/scripts/verify_contract.py`.

That is a control layer. A prompt collection would usually stop at a better instruction.

## What to inspect first

- [Choose a Skill](choose-a-skill.md) if you know the failure you want to stop.
- [Core knowledge](core-knowledge.md) if you want the method layer.
- [Artifact fixtures](fixtures/README.md) if you want concrete output shapes.
- [Public tooling](tooling.md) if you want the verifier layer.
- [Compatibility matrix](compatibility-matrix.json) and [runtime smoke](runtime-smoke.json) if you want package evidence.

## What this still does not claim

This repository does not claim universal host-version compatibility, model decision quality, legal clearance, customer adoption, external popularity, or economic outcomes. It claims a public, installable, sanitized, and increasingly verified control surface.

## Why one repository

The useful unit is the library: one catalog, one installer, one issue tracker, one release gate, one set of examples, one Pages front door, and one contributor path. Splitting each Skill into a small repository would make the system harder to evaluate and would dilute the public signal.
