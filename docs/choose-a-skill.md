# Choose a Skill

Start with the work you are trying to control. Do not browse the full catalog first.

## I need to know what to build

Use:

- `dayan-wenzhen` when the request is vague, risky, or already biased toward a solution.
- `dayan-clarify` when you only need the few questions that would change the route.
- `dayan-plan` when the goal is clear but the execution path has dependencies.
- `dayan-orient` when the first task is understanding an unfamiliar repository.

## I need to create an artifact

Use:

- `dayan-deck` for a focused HTML presentation.
- `dayan-html` for a self-contained page, report, or dashboard.
- `dayan-diagram` for an editable SVG process or system map.
- `dayan-huashu-design` for a polished static HTML prototype or demo.
- `dayan-copywriting` when the artifact is conversion copy rather than a UI.

## I need to build agent infrastructure

Use:

- `dayan-agent-designer` to define responsibilities, tools, memory, boundaries, and evaluation.
- `dayan-agent-factory` after the design is approved and needs packaging.
- `dayan-hook-factory` when a repeated guardrail should be deterministic.
- `dayan-prompt-factory` when the reusable unit is a prompt contract.
- `dayan-marketplace-publishing` when a local Skill or agent is ready for public packaging.

## I need to verify before release

Use:

- `dayan-adversarial-reviewer` for a release or PR verdict.
- `dayan-code-reviewer` for normal code review risk.
- `dayan-api-design-reviewer` before an API contract becomes expensive to change.
- `dayan-a11y-audit` when users may not be able to see, navigate, or operate the UI.
- `dayan-database-performance` when slow queries or unbounded access can become production incidents.

## I need growth or discoverability

Use:

- `dayan-ai-seo` for AI answer visibility.
- `dayan-seo` for traditional search.
- `dayan-content-production` for a reader-ready content package with publication authority separated.
- `dayan-content-evidence-loop` for turning posts and comments into traceable experiments.

## Five starter routes

| If you have... | Try first | Then try |
| --- | --- | --- |
| a fuzzy product idea | `dayan-wenzhen` | `dayan-plan`, `dayan-agent-designer` |
| an unfamiliar codebase | `dayan-orient` | `dayan-code-reviewer`, `dayan-update-docs` |
| a release candidate | `dayan-adversarial-reviewer` | `dayan-a11y-audit`, `dayan-api-design-reviewer` |
| a presentation or report | `dayan-deck` | `dayan-html`, `dayan-diagram` |
| a Skill you want to publish | `dayan-skill-builder` | `dayan-marketplace-publishing` |

For the machine-readable list, use [`catalog.json`](../catalog.json).

For copyable output shapes, inspect the [artifact fixtures](fixtures/README.md).
