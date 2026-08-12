# Architecture decision record

Skill: `dayan-tech-stack-evaluator`

## Input

A team needs to choose between a single repository and multiple small repositories for a public Skill library.

## Output artifact

### Decision

Use one repository for the public Skill library.

### Context

The library's useful unit is not one isolated folder. The useful unit is the shared installer, catalog, issue templates, release history, examples, validators, provenance, sanitization records, and contribution path.

### Options

1. One repository with all public Skills.
2. One repository per Skill.
3. One repository for featured Skills and another for the long tail.

### Chosen option

Option 1.

### Consequences

- Star count, issues, releases, and contributors accumulate in one place.
- Shared validation becomes easier.
- Documentation can cross-link Skills by failure mode.
- The repository must keep navigation strong enough that 56 folders do not become noise.

### Reversal trigger

Split only if one Skill develops an independent runtime, package manager, release cadence, and contributor group that would be harmed by the shared release cycle.

## Verification

- The decision names alternatives.
- Consequences include both benefits and costs.
- The reversal trigger is concrete enough to be revisited.

## Boundary

This fixture does not prove that a monorepo is correct for every open-source project or every package ecosystem.
