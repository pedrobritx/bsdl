---
title: Security Policy
owner: Security Engineer
status: Active
last_updated: 2026-07-08
related: [PROJECT_RULES]
---

# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 0.1.x   | ✅        |

BSF is a documentation-and-process framework; "security updates" here means corrections to guidance in `constraints/security.md`, `recipes/`, and `playbooks/security_review.md`.

## Reporting a Vulnerability

- **Framework guidance flaws** (a recipe or constraint that would lead adopters to insecure implementations): open a GitHub issue with the `sev:2` label, or a private security advisory if disclosure would put adopters at risk.
- **Repository/automation issues** (CI workflow, `automation/validate_docs.py`): open a private security advisory via GitHub's **Security → Report a vulnerability**.

You can expect an acknowledgement within 7 days. Accepted reports are fixed following `playbooks/security_review.md` and recorded in `memory/mistakes.md`.
