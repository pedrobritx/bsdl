---
title: "Constraint: Security"
owner: Engineering
status: Active
last_updated: 2026-10-15
---

# Constraint: Security

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (Level 0).

## Non-negotiables
- No secrets in code, logs, or prompts — ever
- Validate untrusted inputs at system boundaries using the adopted platform's appropriate validation mechanism.
- Auth required by default; public endpoints are explicit allow-list
- Dependencies audited before adding; no unmaintained packages
- RLS enabled on all Supabase tables

## Verification
Required evidence is project-specific and must be recorded: boundary rejection cases, access-control allow/deny cases, and dependency review. This document is a policy; it does not prove those checks have been implemented or passed.
