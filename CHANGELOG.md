# Changelog

## 1.3.0-beta.1 — 2026-08-13

- Added `docs/core-knowledge.md`, a public-safe map of method candidates and publication boundaries for the broader Dayan knowledge layer.
- Added `docs/tooling.md`, a catalog of 14 local repository tools with commands, proof boundaries, and non-claims.
- Added `scripts/verify_tooling.py` and tests, then wired tooling verification into release validation.
- Linked core knowledge and tooling from README, Chinese README, quickstart, methods, skills, and contributing docs.

## 1.2.0-beta.1 — 2026-08-13

- Expanded `docs/fixtures/` from 5 to 9 copyable artifact fixtures, adding visual deck brief, architecture decision record, agent package manifest, and responsive UI acceptance plan.
- Added `docs/good-first-issues.md`, an actionable contribution board with eight bounded tasks.
- Added `scripts/verify_good_first_issues.py` and tests, then wired good-first-issue verification into release validation.
- Updated README, quickstart, chooser, and contributing docs so external contributors can start from a small verified change.

## 1.1.0-beta.1 — 2026-08-13

- Added `docs/fixtures/`, a public artifact gallery with five copyable output fixtures for `dayan-orient`, `dayan-agent-designer`, `dayan-hook-factory`, `dayan-api-design-reviewer`, and `dayan-ai-seo`.
- Added `scripts/verify_fixtures.py` and tests to keep artifact fixtures complete, linked, and sanitized.
- Added a GitHub issue template for artifact fixture contributions.
- Wired fixture verification into release validation and public docs.

## 1.0.0-beta.1 — 2026-08-13

- Added `scripts/runtime_smoke.py`, an offline lifecycle harness for clean temporary homes.
- Added marker-guarded `installers/install.py --update`; updates replace only matching Dayan-owned Skill directories.
- Added `docs/runtime-smoke.md` and `docs/runtime-smoke.json`, covering discovery, trigger routing, declared example commands, non-trigger rejection, and safe update across 56 Skills x 2 targets.
- Updated release validation to require the runtime smoke matrix and rerun all-Skill lifecycle smoke.

## 0.9.0-beta.1 — 2026-08-13

- Extended `scripts/compatibility_smoke.py` with `--all-skills` and `--json-output`.
- Added `docs/compatibility-matrix.json`, a machine-readable 56-Skill x 2-target clean install matrix.
- Updated release validation to require the matrix and rerun all-Skill package smoke.
- Expanded compatibility-smoke tests to cover all-Skill JSON output, conflict handling, and the default report.

## 0.8.0-beta.1 — 2026-08-13

- Added `scripts/compatibility_smoke.py`, a clean temporary-home smoke harness that installs selected Skills into Codex-style and Claude Code-style directories and prints a paste-ready Markdown report.
- Added compatibility-smoke tests and wired the smoke harness into release validation.
- Updated README, README.zh-CN, quickstart, compatibility docs, and the compatibility issue template so external users can report packaging evidence without touching their live agent configuration.

## 0.7.0-beta.1 — 2026-08-13

- Expanded sanitized example runs from 3 to 11 across repository orientation, agent design, hooks, API review, accessibility, database performance, AI visibility, and launch content boundaries.
- Added `scripts/verify_examples.py` to keep public example runs complete, linked from the index, and free of configured redlines.
- Wired example verification into release validation and updated README, README.zh-CN, roadmap, and llms entry points around the larger example surface.

## 0.6.0-beta.1 — 2026-08-12

- Added public playbooks for control-layer design, conversation-to-Skill extraction, and release review loops.
- Added sanitized example runs for Wenzhen, Deck, and Adversarial Reviewer so visitors can copy a realistic trial path.
- Connected playbooks and example runs from README, README.zh-CN, methods, contributing, roadmap, and llms.txt.
- Raised the package release to the first v0.6 beta without changing individual Skill behavior claims.

## 0.5.2-beta.1 — 2026-08-12

- Added a 60-second quickstart that installs into a temporary home instead of a live agent configuration.
- Added a Skill chooser and FAQ so visitors can start from a concrete failure mode instead of browsing 56 folders.
- Expanded compatibility evidence into a clear matrix and added GitHub issue templates for compatibility reports and bugs.
- Recorded the first external publication runbook with Hacker News and V2EX live links, X status, and Reddit account boundary.
- Tightened README and Chinese README conversion paths around quick trial, evidence, and compatibility reports.

## 0.5.1-beta.1 — 2026-08-12

- Rebuilt the GitHub Pages front door around the full 56-Skill library instead of a generic repository overview.
- Added three 60-second proof demos for Wenzhen, Deck, and Code Reviewer.
- Added a channel-ready launch kit with factual claims, copy variants, and ethical distribution boundaries.
- Added an automated public-site verifier and wired it into release validation.

## 0.5.0-beta.1 — 2026-08-12

- Expanded the single repository from 12 to 56 installable public beta Skills.
- Added 44 clean-room Skill bundles across engineering quality, research and decisions, agent systems, content and design, and product architecture.
- Published 12 concise Dayan method cards covering complexity, evidence, authority, verification, completion, project harnesses, delivery assets, and audience-clean artifacts.
- Added deterministic generation, public indexes, provenance, sanitization records, starter contracts, and isolated install smoke coverage for all 56 Skills.
- Kept customer material, private operating data, personalized finance workflows, logged-in integrations, and unresolved third-party assets outside the public package.

## 0.4.0-beta.1 — 2026-08-12

- Completed the first public 12-Skill collection inside one repository.
- Added Orient, Plan, Agent Designer, Agent Factory, Hook Factory, HTML, Huashu Design, Diagram, and AI SEO.
- Added nine clean-room starter contracts, provenance records, sanitization records, and a shared deterministic bundle validator.
- Expanded isolated Codex and Claude Code installer smoke coverage to all 12 Skills.
- Reorganized discovery around Create, Think, Build, and Verify & Grow instead of a flat release list.

## 0.3.0-beta.1 — 2026-08-12

- Released `dayan-wenzhen` as the third public beta Skill.
- Added a falsifiable problem-hypothesis and minimal task-contract workflow.
- Added a JSON contract schema, safe starter fixture, rejected unsafe fixture, and deterministic validator.
- Added tests for a real defer-or-shrink option, high-risk release boundaries, and private-path rejection.

## 0.2.0-beta.1 — 2026-07-29

- Released `dayan-adversarial-reviewer` as the second public beta Skill.
- Added a public severity rubric and separate failure-mode, maintainability, and trust-boundary lenses.
- Added human-readable plus machine-readable verdict contracts.
- Added accepted and blocking fixtures with a deterministic JSON validator.
- Extended isolated installer smoke coverage to both public beta Skills.

## 0.1.0-beta.1 — 2026-07-29

- Published the Dayan Agent Skills mothership.
- Released `dayan-deck` as the first public beta.
- Added a four-slide HTML starter and deterministic structural verifier.
- Added isolated Codex and Claude Code packaging targets.
- Published the 12-Skill roadmap, catalog, tests, CI, safety model, and clean-room records.
