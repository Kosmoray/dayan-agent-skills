# Release review loop

Use this before publishing an AI-assisted artifact, Skill, documentation change, or verifier.

## Builder/checker split

| Stage | Builder owns | Checker owns |
| --- | --- | --- |
| Frame | goal, audience, artifact | missing authority, wrong audience, unsafe scope |
| Produce | implementation or content | no direct edits unless the boundary allows it |
| Verify | local tests and examples | independent failure-mode review |
| Release | package notes | evidence, limitations, human approval |

## Review checklist

- What exact claim is the release making?
- Which test proves that claim?
- Which important claim is still unproven?
- Is any customer, credential, private path, or internal strategy visible?
- Can a user install or inspect without touching their live configuration?
- Is there a feedback path for failures?

## Minimum release note

```text
What changed:
Who should try it:
What is verified:
What is not claimed:
Known blockers:
How to report a failure:
```

## Result labels

- `BLOCK`: do not publish until the named issue is fixed.
- `CONCERNS`: publish only if the limitation is explicit and acceptable.
- `CLEAN`: no blocking issue found within the review scope.

`CLEAN` never means universally safe. It only means the reviewed evidence supports the release boundary.
