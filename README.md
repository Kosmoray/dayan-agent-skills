<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/dayan-mark-on-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/dayan-mark.svg">
    <img src="assets/dayan-mark.svg" width="104" alt="Dayan">
  </picture>
</p>

<h1 align="center">DAYAN AGENT SKILLS</h1>

<p align="center"><strong>Give probabilistic AI a control layer.</strong></p>

<p align="center">
  Open skills, harnesses, hooks, and verifiers for making agent work more repeatable, inspectable, and human-friendly.
</p>

<p align="center">
  <a href="https://kosmoray.github.io/dayan-agent-skills/"><strong>OPEN THE DAYAN DECK DEMO</strong></a>
  ·
  <a href="README.zh-CN.md">中文</a>
  ·
  <a href="https://github.com/Kosmoray/dayan-agent-skills"><strong>★ STAR THIS CONTROL LAYER</strong></a>
</p>

<p align="center">
  <a href="https://kosmoray.github.io/dayan-agent-skills/">
    <img src="assets/hero.svg" alt="Dayan Agent Skills turns probabilistic AI into repeatable workflows">
  </a>
</p>

## The idea

Early AI feels like a manual film camera: powerful, but every focus, exposure, and timing decision is left to the operator.

Agent skills are the semi-automatic modes. A Skill chooses the workflow. A harness holds the process together. Hooks stop predictable mistakes. Verifiers check whether the result earned the claim.

This repository publishes those control layers instead of hiding them.

## Available now

### `dayan-deck` · public beta

Turn a topic, outline, or source document into a self-contained HTML presentation with:

- one narrative job per slide;
- a locked visual and motion system;
- editable text instead of full-slide screenshots;
- keyboard, print, responsive, and reduced-motion behavior;
- a deterministic structural verifier;
- explicit limits for visual quality, factual accuracy, and PPTX export.

[Read the Skill](skills/dayan-deck/SKILL.md) · [Open the live starter](https://kosmoray.github.io/dayan-agent-skills/) · [Inspect the verifier](skills/dayan-deck/scripts/verify_deck.py)

### `dayan-adversarial-reviewer` · public beta

Review a concrete change before merge or release through three distinct lenses:

- failure modes: malformed, repeated, partial, concurrent, interrupted, and rollback paths;
- maintainability: hidden contracts, mixed responsibilities, and regression traps;
- trust boundaries: untrusted input, authorization, files, environment, logs, and secrets;
- evidence-backed `BLOCK`, `CONCERNS`, or `CLEAN` verdicts;
- matching human-readable Markdown and machine-verifiable JSON;
- accepted and blocking fixtures plus a deterministic verdict validator.

[Read the Skill](skills/dayan-adversarial-reviewer/SKILL.md) · [Inspect the rubric](skills/dayan-adversarial-reviewer/references/rubric.md) · [Run the validator](skills/dayan-adversarial-reviewer/scripts/verify_review.py)

## Install in under a minute

Clone the repository, then install into an explicit agent home:

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills

python3 installers/install.py dayan-deck \
  --agent codex \
  --home "$HOME"
```

Replace `dayan-deck` with `dayan-adversarial-reviewer` to install the review Skill.

Claude Code packaging target:

```bash
python3 installers/install.py dayan-deck \
  --agent claude-code \
  --home "$HOME"
```

The beta installer performs new installs only and refuses to overwrite an existing Skill directory. See the [installation contract](docs/install.md).

## Try the verifier

```bash
python3 skills/dayan-deck/scripts/verify_deck.py \
  skills/dayan-deck/examples/starter.html

python3 skills/dayan-adversarial-reviewer/scripts/verify_review.py \
  skills/dayan-adversarial-reviewer/examples/block-review.json
```

Expected result:

```text
PASS: ...starter.html satisfies the structural deck contract (4 slides)
```

The verifier deliberately rejects remote runtime dependencies, multiple active slides, missing slide headings, credential-like assignments, private paths, and presenter notes inside audience-facing HTML.

## What comes next

The first 12 public candidates are organized as four product clusters:

| Create | Think | Build | Verify & Grow |
| --- | --- | --- | --- |
| Dayan Deck | Wenzhen | Agent Designer | Adversarial Reviewer |
| Huashu Design | Plan | Agent Factory | AI SEO |
| Dayan HTML | Orient | Hook Factory |  |
| Diagram |  |  |  |

`dayan-deck` and `dayan-adversarial-reviewer` are available as public betas. The other names are a public roadmap, not a production-readiness claim. See [`catalog.json`](catalog.json).

## Design principles

1. **Result before ritual.** A Skill must create a useful artifact, not merely describe a philosophy.
2. **Evidence before claims.** A passing test proves only what the test actually checks.
3. **Open by default.** General AI control and verification mechanisms should earn public names, citations, and improvements.
4. **Human authority stays explicit.** Publication, spending, credentials, consequential decisions, and high-stakes claims retain human control.
5. **Failure is part of the product.** Rejected fixtures and stop conditions matter as much as happy paths.

## Compatibility

The repository currently verifies packaging into Codex and Claude Code Skill directories in isolated temporary homes. That is not yet a claim that every product version discovers and triggers the Skill identically. Behavioral compatibility evidence will be added release by release.

See [`docs/compatibility.md`](docs/compatibility.md).

## Contributing

Issues and pull requests are welcome. A useful contribution includes:

- one repeatable user problem;
- a clear trigger and non-trigger boundary;
- one accepted fixture;
- one rejected or unsafe fixture;
- a validator or an explicit human-review contract;
- license provenance.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) or propose a Skill using the issue template.

## Security and provenance

The public beta is a clean-room package. It excludes customer material, private templates, internal infrastructure, machine-specific paths, credentials, and third-party binary assets. Read [`SANITIZATION.md`](SANITIZATION.md), [`SECURITY.md`](SECURITY.md), and the provenance records for [`dayan-deck`](skills/dayan-deck/PROVENANCE.md) and [`dayan-adversarial-reviewer`](skills/dayan-adversarial-reviewer/PROVENANCE.md).

## License

[MIT](LICENSE).

---

Built by Dayan for people who want AI to feel **controllable—not magical**.
