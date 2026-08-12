# Repository orientation map

Skill: `dayan-orient`

## Input

A maintainer says:

> I cloned a small task-runner repository. Before changing code, map what to read first and what commands prove the project still works.

## Output artifact

### Purpose

The repository appears to provide a command-line task runner with a small library layer, a parser, and a command entry point.

### Runtime path

1. `src/cli.py` parses command-line arguments.
2. `src/config.py` loads the project configuration file.
3. `src/runner.py` expands tasks and executes steps.
4. `src/report.py` formats success, failure, and skipped task output.

### Read first

- `README.md` for supported commands and examples.
- `pyproject.toml` for package metadata and test tooling.
- `src/cli.py` for the entry point.
- `src/runner.py` for execution semantics.
- `tests/test_runner.py` for expected behavior.

### Safe starter exercise

Add one skipped-task fixture before changing execution logic. A useful first change is a test that proves skipped dependencies are reported once, not once per downstream task.

## Verification

- Every architecture claim names a repository-relative path.
- Suggested commands come from visible project files.
- No code change is recommended before the map is written.

## Boundary

This fixture does not prove the target repository exists, nor that the inferred architecture is correct for every task-runner project.
