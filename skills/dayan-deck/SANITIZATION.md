# Sanitization record

Date: 2026-07-29
Scope: `skills/dayan-deck/`, `installers/install.py`, and `docs/install.md`

## Result

No credential value, private user path, customer identity, private key, internal strategy, or binary vendor asset is present in the candidate.

The standard text scan has two intentional classes of matches:

- the verifier contains a pattern identifier for detecting credential-like assignments;
- the installation guide names the public configuration directory used by a supported packaging target.

Neither match contains a credential or private location. They remain visible so reviewers can audit the detector and installer behavior.

## Excluded from the candidate

- all vendor reference directories;
- all private templates and brand assets;
- all customer or organization-specific workflow rules;
- all binary audio, image, font, and presentation assets;
- all source scripts with machine-specific dependency paths.

The beta is published under MIT. Behavioral compatibility, safe lifecycle support, and broader cross-environment visual evidence remain explicitly unverified and are tracked as roadmap items.
