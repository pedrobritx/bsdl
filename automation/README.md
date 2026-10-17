---
title: Polaris local validation
owner: Maintainer
status: Active
last_updated: 2026-10-16
---

# Local validation

Run `python3 automation/validate_docs.py` and `python3 -m unittest discover -s tests -v` from this checkout. These check documentation/tooling, not a consuming application's quality. The validator is a deliberately local adapter so this repository can be checked without sibling repositories, network access or Polaris governance. Its identical copies are not separate constitutional authority.

Polaris also supplies the read-only `automation/constellation.py` planner. Read [its composition contract](../integration/README.md) before use. The optional integration example requires only the enabled/requested sibling checkouts; the local unit suite uses isolated fixtures.

## Experimental A0 routing

`python3 automation/a0.py route --config <project-config> --intake <host-inspected-intake> --workspace <checkout-parent> --product-root <adopter-checkout>` recommends relevant discipline coverage and a permissible orchestration mode, while reusing the existing v1 planner. `python3 automation/a0.py check-result --result <reported-result>` validates a self-reported result structure **without attesting to performed checks**. See [A0 contract](../integration/a0.md) and [Codex skill](../.agents/skills/constellation-a0/SKILL.md). These commands are read-only, not an agent runtime.
