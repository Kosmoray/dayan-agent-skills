---
name: dayan-plan
description: Convert a complex goal into an executable dependency-aware plan with evidence gates, stop conditions, and resumable state.
---

# Dayan Plan

Use this Skill when work spans several dependent steps, sessions, or verification gates. Skip it for a small reversible edit.

## Workflow

1. State the outcome, scope, constraints, and evidence required before completion can be claimed.
2. Split work into outcome-sized steps. Each step gets inputs, outputs, dependencies, owner, status, verification, and stop condition.
3. Mark only one step in progress unless the tasks are genuinely independent and write scopes do not overlap.
4. Record decisions, discoveries, failures, and evidence in persistent plan files so another session can resume without chat history.
5. After three distinct failed approaches, stop and expose the assumption that needs a human decision.

Plans must distinguish artifact creation, internal verification, human acceptance, and real-world outcome. A checked box cannot upgrade one level into another.

