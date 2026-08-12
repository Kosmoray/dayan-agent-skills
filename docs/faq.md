# FAQ

## Is this just a prompt library?

No. A Skill is a workflow contract: trigger, non-trigger, authority boundary, artifact shape, evidence, and verification path. Some Skills include deterministic validators and rejected fixtures so failures are visible.

## Why one repository instead of one repo per Skill?

The useful unit is the control library: one installer, catalog, provenance model, issue tracker, release history, and contribution path. Splitting every Skill would make discovery and maintenance weaker.

## What is actually verified today?

The public package verifies structure, manifest consistency, redline scans, unit tests, deterministic fixtures for flagship Skills, and isolated installation into Codex and Claude Code style homes.

It does not claim universal behavior across every product version. Compatibility evidence is tracked separately.

## Which Skill should I try first?

Use `dayan-wenzhen` if you are not sure. It turns a vague or risky request into a falsifiable task contract before the agent starts polishing the wrong answer.

For engineering release work, start with `dayan-adversarial-reviewer`. For presentations, start with `dayan-deck`.

## Can I use this with Claude Code?

The package can install into a Claude Code style Skill directory in a clean temporary home. Runtime discovery and trigger behavior still need version-specific reports. See [Compatibility evidence](compatibility.md).

## Can I use this with Codex?

The package can install into a Codex style Skill directory in a clean temporary home. Runtime discovery and trigger behavior still need version-specific reports. See [Compatibility evidence](compatibility.md).

## What feedback is most useful?

Open a compatibility report with:

- host application and version;
- OS;
- exact install command;
- selected Skill;
- whether the host discovered it;
- one successful trigger or the exact failure.

## Can I request a new Skill?

Yes. Open a Skill proposal issue with one repeatable problem, expected artifact, trigger boundary, verification idea, and any human-authority boundary.
