---
title: ADR-004 capability extraction with source provenance
owner: Maintainer
status: Accepted
last_updated: 2026-10-15
---

# Capability extraction

## Decision and authorisation
The owner explicitly instructed on 2026-10-15 to move files to Polaris, Axis, Meridian and Sentinel and commit. Apply the reviewed operational directions while preserving the canonical philosophical text, historical decisions, existing Meridian implementation and workflows.

## Boundaries
Polaris retains constitutional/governance authority and registry. Axis maintains engineering roles, recipes, playbooks, project templates and optional web profiles. Meridian receives designer guidance. Sentinel receives the security role and security-review method. Project security documents and general incident management remain adopter-template slots in Axis; Sentinel supplies requirements/evidence guidance. Local validation and essential policy templates are derived adapters, not duplicated constitutional authority.

## History
Use snapshot extraction with exact original commit/blob provenance and destination content hashes. The complete original lineage remains in Polaris. No filtered history, force-push or squash-policy exception is needed. This is an explicit choice for reviewability; it does not preserve native per-file blame in the new repositories.

## Commit and merge order
Initialise empty Axis/Sentinel with an empty review baseline. Commit and review Sentinel, Meridian and Axis additions before accepting Polaris removals. Cross-repository migration cannot be atomic; immutable destination references and the ledger support coordination and rollback. No automatic merge, release, licence selection, provider configuration or deployment.

## Evidence
Run standalone documentation/tooling tests for Polaris, Axis and Sentinel, verify all moves against the source ledger and resolve local document references. Run Meridian's existing tests/build for its contributor-guidance change. The migration ledger and verification report record exact results and remaining gaps.
