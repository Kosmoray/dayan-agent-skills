# Sanitization record

Date: 2026-08-12

## Scope

`skills/dayan-wenzhen/` was written as a generic, public task-framing package.

## Checks

- Checked for private machine paths, credentials, private keys, customer identifiers, and internal control markers with `scripts/scan_public_redlines.py`.
- Checked fixture consistency and high-risk action boundaries with `scripts/verify_contract.py`.
- Used fictional, non-commercial examples only.

## Result

No private material, customer material, credentials, or proprietary workflow details are intended to be included. The rejected fixture deliberately contains an unsafe authorization pattern so the validator has a negative case; it contains no sensitive material.

