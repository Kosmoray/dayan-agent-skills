<p align="center"><img src="assets/dayan-mark.svg" width="104" alt="Dayan"></p>

<h1 align="center">DAYAN AGENT SKILLS</h1>

<p align="center"><strong>Pick the mess. Install the fix.</strong></p>

<p align="center">One public library of 56 AI-agent Skills for turning vague work into a clear contract, a clear deck, a safer release, a mapped repository, or a bounded agent.</p>

<p align="center">
  <a href="https://kosmoray.github.io/dayan-agent-skills/"><strong>PICK A PROBLEM</strong></a>
  ·
  <a href="docs/quickstart.md"><strong>INSTALL IN 60 SECONDS</strong></a>
  ·
  <a href="docs/demos/control-library.html">SEE THE PROOF</a>
  ·
  <a href="README.zh-CN.md">中文</a>
  ·
  <a href="https://github.com/Kosmoray/dayan-agent-skills"><strong>★ STAR IF IT SAVED YOU A REBUILD</strong></a>
</p>

<p align="center"><a href="https://kosmoray.github.io/dayan-agent-skills/"><img src="assets/hero.svg" alt="Pick a common AI-agent problem and install the matching Dayan Skill"></a></p>

## Pick your problem. Take the fix.

| You need to... | Click this Skill | You get |
| --- | --- | --- |
| turn a fuzzy request into work that can be checked | [`dayan-wenzhen`](skills/dayan-wenzhen/SKILL.md) | a falsifiable task contract with authority, evidence, and a stop signal |
| make an AI-generated deck obvious instead of crowded | [`dayan-deck`](skills/dayan-deck/SKILL.md) | one narrative job per slide plus a structural verifier |
| catch a release failure before it ships | [`dayan-adversarial-reviewer`](skills/dayan-adversarial-reviewer/SKILL.md) | a `BLOCK`, `CONCERNS`, or `CLEAN` verdict with evidence |
| understand an unfamiliar codebase before changing it | [`dayan-orient`](skills/dayan-orient/SKILL.md) | a repository map and a safe first-change route |
| define what an agent may do, use, remember, and refuse | [`dayan-agent-designer`](skills/dayan-agent-designer/SKILL.md) | a bounded agent specification with evaluation hooks |

The live [problem picker](https://kosmoray.github.io/dayan-agent-skills/) gives each route a one-click install command and a visual proof. The library stays in one package: one clone, one source of truth, 56 installable public-beta Skills.

### Run one route

Clone once, then install only the Skill you need into a temporary home:

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills
DAYAN_TEST_HOME="$(mktemp -d)"

python3 installers/install.py dayan-wenzhen \
  --agent codex \
  --home "$DAYAN_TEST_HOME"

python3 skills/dayan-wenzhen/scripts/verify_contract.py \
  skills/dayan-wenzhen/examples/starter-contract.json
```

Replace `dayan-wenzhen` with the Skill above that matches your problem. [Quickstart](docs/quickstart.md) · [All 56 Skills](docs/skills.md) · [Compatibility evidence](docs/compatibility.md) · [What the checks do—and do not—prove](docs/control-layer-vs-prompt-collection.md) · [Share kit](docs/share-kit.md)

## Copy-paste examples and fixtures

Try one sanitized run before integrating anything:

The repository now includes [11 sanitized example runs](examples/runs/README.md), including:

- [Wenzhen fuzzy request](examples/runs/wenzhen-fuzzy-request.md): turn a vague AI-support idea into a falsifiable task contract.
- [Deck from outline](examples/runs/deck-from-outline.md): turn a practical outline into a verifier-ready presentation request.
- [Adversarial review verdict](examples/runs/adversarial-review-verdict.md): turn a release description into a concrete BLOCK/CONCERNS/CLEAN review.
- [API pagination contract review](examples/runs/api-review-pagination-contract.md): block an unbounded endpoint before clients depend on it.
- [AI visibility for open-source docs](examples/runs/ai-seo-open-source-docs.md): make claims easier for AI assistants to cite accurately.

It also includes [12 artifact fixtures](docs/fixtures/README.md) that show copyable output shapes for repository orientation, agent design, guardrail hooks, API review, AI visibility audits, visual deck briefs, architecture decisions, agent packages, responsive UI acceptance, verifier planning, false-positive review, and authority ledgers.

Then use the public [playbooks](docs/playbooks/README.md) to decide whether your repeated workflow should become a checklist, Skill, verifier, hook, or agent. If you want a bounded contribution, start with [Good first issues](docs/good-first-issues.md).

For the system behind the Skills, read the [core knowledge map](docs/core-knowledge.md). For the small local tools that verify the repository, read [Public tooling](docs/tooling.md).

## Choose your route

| Create | Think | Build | Verify & Grow |
| --- | --- | --- | --- |
| [Deck](skills/dayan-deck/SKILL.md) | [Wenzhen](skills/dayan-wenzhen/SKILL.md) | [Agent Designer](skills/dayan-agent-designer/SKILL.md) | [Adversarial Reviewer](skills/dayan-adversarial-reviewer/SKILL.md) |
| [Huashu Design](skills/dayan-huashu-design/SKILL.md) | [Plan](skills/dayan-plan/SKILL.md) | [Agent Factory](skills/dayan-agent-factory/SKILL.md) | [AI SEO](skills/dayan-ai-seo/SKILL.md) |
| [HTML](skills/dayan-html/SKILL.md) | [Orient](skills/dayan-orient/SKILL.md) | [Hook Factory](skills/dayan-hook-factory/SKILL.md) |  |
| [Diagram](skills/dayan-diagram/SKILL.md) |  |  |  |

All 56 are installable public betas. Featured Skills have dedicated validators; the Core Library uses a shared strict public bundle contract, package-install matrix, and offline lifecycle smoke.

## Featured Skills

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

### `dayan-wenzhen` · public beta

Turn a vague, risky, or solution-shaped request into a decision-ready task contract before the agent starts generating a polished answer:

- triage the work type, risk level, currently allowed action, release authority, and minimum evidence;
- state a falsifiable best-current problem hypothesis rather than pretending certainty;
- ask only questions whose answers can change the route;
- compare the current route, alternatives, a reframed third route, and a genuine defer-or-shrink option;
- end with the smallest reversible bet, pause signal, checkpoint, and evidence needed to continue;
- return human-readable Markdown plus a machine-verifiable JSON contract.

[Read the Skill](skills/dayan-wenzhen/SKILL.md) · [Inspect the schema](skills/dayan-wenzhen/references/contract-schema.md) · [Run the validator](skills/dayan-wenzhen/scripts/verify_contract.py)

## Install in under a minute

Clone the repository, then install into an explicit agent home. Use a temporary home for first inspection:

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills
DAYAN_TEST_HOME="$(mktemp -d)"

python3 installers/install.py dayan-deck \
  --agent codex \
  --home "$DAYAN_TEST_HOME"
```

Replace `dayan-deck` with any name in the route table to install another public beta Skill.

Claude Code packaging target:

```bash
python3 installers/install.py dayan-deck \
  --agent claude-code \
  --home "$DAYAN_TEST_HOME"
```

The beta installer performs new installs only and refuses to overwrite an existing Skill directory. See the [installation contract](docs/install.md).

## Try the verifier

```bash
python3 skills/dayan-deck/scripts/verify_deck.py \
  skills/dayan-deck/examples/starter.html

python3 skills/dayan-adversarial-reviewer/scripts/verify_review.py \
  skills/dayan-adversarial-reviewer/examples/block-review.json

python3 skills/dayan-wenzhen/scripts/verify_contract.py \
  skills/dayan-wenzhen/examples/starter-contract.json
```

Expected result:

```text
PASS: ...starter.html satisfies the structural deck contract (4 slides)
```

The verifier deliberately rejects remote runtime dependencies, multiple active slides, missing slide headings, credential-like assignments, private paths, and presenter notes inside audience-facing HTML.

## Verify any new bundle

```bash
python3 scripts/validate_public_skill.py dayan-orient

python3 scripts/verify_fixtures.py

python3 scripts/verify_methods.py

python3 scripts/verify_positioning.py

python3 scripts/verify_control_demo.py

python3 scripts/verify_share_kit.py

python3 scripts/verify_good_first_issues.py

python3 scripts/verify_tooling.py
```

See [`catalog.json`](catalog.json) for readiness evidence and unresolved host-version evidence for every Skill.

## Design principles

1. **Result before ritual.** A Skill must create a useful artifact, not merely describe a philosophy.
2. **Evidence before claims.** A passing test proves only what the test actually checks.
3. **Open by default.** General AI control and verification mechanisms should earn public names, citations, and improvements.
4. **Human authority stays explicit.** Publication, spending, credentials, consequential decisions, and high-stakes claims retain human control.
5. **Failure is part of the product.** Rejected fixtures and stop conditions matter as much as happy paths.

## Compatibility

The repository verifies packaging into Codex and Claude Code Skill directories in isolated temporary homes, then runs an offline lifecycle smoke that discovers installed Skills, routes catalog trigger text, executes declared example commands, and tests marker-guarded update. That is still not a claim that every product version loads the Skill UI or that every model routes identically.

See [`docs/compatibility.md`](docs/compatibility.md) and [`docs/runtime-smoke.md`](docs/runtime-smoke.md).

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

The public beta is a clean-room package. It excludes customer material, private templates, internal infrastructure, machine-specific paths, credentials, and third-party binary assets. Read [`SANITIZATION.md`](SANITIZATION.md), [`SECURITY.md`](SECURITY.md), and each Skill's local provenance and sanitization record.

## License

[MIT](LICENSE).

---

Built by Dayan for people who want AI to feel **controllable—not magical**.
