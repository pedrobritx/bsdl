---
title: Capability extraction and rollback
owner: Maintainer
status: Active
last_updated: 2026-10-15
---

# Capability extraction and rollback

The source snapshot is Polaris commit 4881ea912345079efeaee5fbd0d287680fd5a06e. The owner authorised moves and commits after the forensic audit. See migration/provenance.json for exact original and destination file hashes.

Destination additions must be reviewed before merging Polaris removals. Current entry points link to capability review commits/branches, so source discovery remains possible before all default branches converge. Full Polaris governance is opt-in; the standalone capability checks do not clone sibling repositories.

## Rollback
Before merge, close the coordinated PRs or retain their branches for revision. After merge, revert the affected commits through review in reverse dependency order and restore the source files from the recorded original snapshot. Never force-push or erase original history. The migration creates no runtime/database transition, package release or provider configuration.

## Remaining boundaries
Licensing and public distribution remain separate. Philosophical protective-intervention wording remains Proposed. Runtime/Figma/accessibility claims are not inferred from documentation checks.
