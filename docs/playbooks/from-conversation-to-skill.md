# From conversation to Skill

Use this when an effective repeated conversation pattern is worth packaging.

## Extraction route

1. Name the repeated user problem in one sentence.
2. Separate the reusable method from project-specific facts.
3. Write the trigger and non-trigger boundary.
4. Define the output artifact.
5. Add one accepted example.
6. Add one rejected, unsafe, or out-of-scope example.
7. Add provenance and sanitization notes.
8. Add a validator when the artifact has a stable structure.
9. Register the Skill in the catalog and plugin package.

## Public Skill skeleton

```markdown
---
name: dayan-example-skill
description: One sentence that tells a stranger exactly when to use it.
---

# Dayan Example Skill

## Use when

- ...

## Do not use when

- ...

## Workflow

1. Frame the request.
2. Produce the artifact.
3. Verify the boundary.
4. State known evidence gaps.

## Output contract

- ...

## Safety

- ...
```

## Evidence rule

Do not turn internal success into public maturity. A clean public Skill can honestly say:

- installable;
- structurally validated;
- fixture-tested;
- not yet proven across every host runtime.
