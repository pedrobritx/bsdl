---
title: "Constraint: Coding Standards"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Constraint: Coding Standards

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (L0).

## Language & typing
- TypeScript everywhere, `strict: true`. No `any` without an inline justification comment.
- **Zod** validates every external boundary: API inputs, env vars, webhooks, LLM outputs.

## React / Next.js
- **Server Components by default**; `"use client"` only when interaction demands it.
- Prefer **Server Actions** for mutations.
- Shared client state: **Zustand**. **Never Context API for app state** (fine for true dependency injection like themes).
- Tailwind for styling; design tokens from `DESIGN_SYSTEM.md` — no magic values.

## Libraries
- Dates: `date-fns` or Temporal. **Never `moment.js`.**
- Before adding any dependency: Decision Engine check + license check + "can the platform do this natively?"

## Structure
- No hardcoded user-facing strings (LOCALIZATION).
- Errors follow the taxonomy in `ERROR_HANDLING.md` — no naked `throw new Error("oops")` reaching users.
- Idempotent scripts; versioned config; small pure functions over clever abstractions.

## Verification
- ESLint + typecheck in CI (`WORKFLOWS.md`); reviewer checks this list in every PR.
