# Artifact fixtures

These fixtures show what useful Skill output can look like after a clean run. They are not transcripts, benchmark claims, customer work, or model output guarantees.

Each fixture includes:

- `Skill`: the public Skill being demonstrated;
- `Input`: the safe public request shape;
- `Output artifact`: the copyable result structure;
- `Verification`: how a reviewer can check the result;
- `Boundary`: what the fixture does not prove.

## Fixtures

- [Repository orientation map](orient-repo-map.md) — `dayan-orient`
- [Support triage agent contract](agent-designer-triage-agent.md) — `dayan-agent-designer`
- [Public redline hook spec](hook-factory-public-redline.md) — `dayan-hook-factory`
- [Pagination API review](api-design-review.md) — `dayan-api-design-reviewer`
- [AI visibility docs audit](ai-seo-docs-audit.md) — `dayan-ai-seo`
- [Visual deck brief](deck-visual-brief.md) — `dayan-deck`
- [Architecture decision record](architecture-decision-record.md) — `dayan-tech-stack-evaluator`
- [Agent package manifest](agent-package-manifest.md) — `dayan-agent-factory`
- [Responsive UI acceptance plan](frontend-responsive-plan.md) — `dayan-frontend-responsive-ui`
- [Tool-before-agent verifier plan](tool-before-agent-verifier-plan.md) — `dayan-hook-factory`
- [False-positive control review](false-positive-control-review.md) — `dayan-adversarial-reviewer`
- [Human authority ledger](human-authority-ledger.md) — `dayan-agent-designer`

## Add a fixture

Use the same five-section shape and keep it public:

1. no private paths;
2. no secrets or credentials;
3. no real customer identifiers;
4. no claims that the fixture proves production success;
5. one clear verification command or checklist.

Then run:

```bash
python3 scripts/verify_fixtures.py
```
