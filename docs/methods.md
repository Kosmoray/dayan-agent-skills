# Dayan public methods

Twelve compact methods explain the decision rules shared across the public Skills.

For applied routes, start with the [public playbooks](playbooks/README.md).

- [Complexity ladder](methods/complexity-ladder.md) — Prefer a deterministic rule, then a pipeline, then an agent. Escalate only when the simpler form cannot handle uncertainty or tool choice.
- [Multi-pass decomposition](methods/multi-pass-decomposition.md) — Separate framing, generation, evidence collection, verification, and release so one fluent output cannot silently approve itself.
- [Adversarial validation](methods/adversarial-validation.md) — Use a checker with a different objective and, where possible, fewer permissions than the builder.
- [Confidence and evidence chain](methods/confidence-evidence-chain.md) — Tie every strong conclusion to observable evidence, scope, date, and a signal that would change it.
- [Reversible action](methods/reversible-action.md) — Move quickly on bounded reversible work. Require explicit authority before publication, spending, credentials, deletion, signing, or production impact.
- [Falsifiable problem framing](methods/falsifiable-framing.md) — State a best-current problem hypothesis, plausible alternatives, and the real-world signal that would disprove it.
- [Human authority and AI boundaries](methods/human-authority.md) — AI may accelerate analysis and production; consequential authority, accountability, takeover, and release remain explicit human responsibilities.
- [Six levels of completion](methods/completion-levels.md) — Distinguish artifact ready, internally verified, human accepted, reality released, external outcome verified, and economically validated.
- [Project harness](methods/project-harness.md) — Represent work as a dependency topology with waves, approvals, evidence receipts, stop conditions, and an archive that can be resumed.
- [Delivery asset pipeline](methods/delivery-assets.md) — A reusable delivery includes the artifact, deterministic checks, evidence, handoff, version, and a path to reuse or retire it.
- [Simple altruistic communication](methods/simple-altruistic-communication.md) — Lead with the decision, explain why it matters to this reader, show evidence, and end with the one useful action.
- [Audience-clean artifacts](methods/audience-clean-artifacts.md) — Reader-visible output contains only reader-relevant content; production notes, placeholders, internal roles, and hidden instructions live elsewhere.
