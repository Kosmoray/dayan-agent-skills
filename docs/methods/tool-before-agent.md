# Tool-before-agent

## Principle

If a failure can be detected deterministically, make a tool detect it before asking an agent to remember it.

## Apply it

1. Name the repeated failure in one sentence.
2. Write the smallest rule that would catch the failure.
3. Build a local verifier or checklist before widening the workflow.
4. Add one accepted fixture and one rejected or boundary fixture.
5. Let the agent call the verifier; do not make the agent replace it.

## Failure pattern

The method has failed when the same issue is handled by repeated reminders, reviewer taste, or long prompt text even though a local check could have caught it earlier.

## Public status

This is a compact public method card, not a claim that every workflow needs automation or that tools can judge all product quality. MIT licensed as part of Dayan Agent Skills.
