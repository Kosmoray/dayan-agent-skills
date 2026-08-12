# Visual deck brief

Skill: `dayan-deck`

## Input

A maintainer wants a five-slide project introduction that explains why agent work needs control layers without relying on screenshots.

## Output artifact

### Narrative

1. Problem: probabilistic output is useful but hard to trust.
2. Missing layer: workflows, hooks, and verifiers are usually rebuilt per project.
3. Library: 56 Skills make repeated work explicit.
4. Evidence: package install, lifecycle smoke, fixtures, and validators.
5. Ask: try one Skill, report compatibility, or add a fixture.

### Visual system

- background: warm paper;
- accent: deep navy and signal red;
- type: large headings, short body copy;
- layout: one decision per slide;
- motion: optional fade only, with reduced-motion support.

### Slide contract

Each slide has one `h1` or `h2`, one primary claim, and one visible proof element. No speaker notes appear inside the audience-facing HTML.

## Verification

- Run the deck structural verifier on the final HTML.
- Confirm keyboard navigation, print view, and reduced-motion behavior.
- Check that every claim links to repository evidence.

## Boundary

This fixture does not prove visual taste, audience persuasion, factual accuracy beyond cited files, or PPTX export quality.
