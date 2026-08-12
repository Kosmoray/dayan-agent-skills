# Example run: Orient an unknown repository

## User input

```text
I need to make a small change in this repository, but I do not know the structure yet. Map it before editing.
```

## Skill to try

`dayan-orient`

## Expected direction

The Skill should not start editing. It should first produce an orientation map:

- main entry points;
- build and test commands;
- configuration files;
- risky directories;
- likely owner boundaries;
- the smallest safe file-reading path.

## Minimal output shape

```text
Repository purpose:
Unknown until package metadata, README, and test layout are inspected.

First evidence to read:
README, package manifest or build file, tests, CI workflow, and nearest agent instructions.

Risk:
Do not edit generated artifacts, lockfiles, credentials, or deployment configuration until the change target is proven.

Next step:
Open the files directly involved in the requested behavior, then propose the smallest patch.
```

## What to verify

- The output cites repository files rather than guessing.
- It separates facts from likely inferences.
- It names files that should not be touched without stronger evidence.
