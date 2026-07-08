---
title: "Constraint: Cost"
owner: CEO
status: Active
last_updated: 2026-07-01
---

# Constraint: Cost

> Prevents AI from suggesting overengineered solutions. Immutable during execution.

## Non-negotiables
- **Any new recurring cost is L0.** No exceptions, no trials that auto-convert.
- Prefer free tiers and services already in the stack before adding vendors.

## Never introduce without explicit L0 approval
- AWS (any service)
- Kubernetes
- Redis clusters / managed Redis (introduce caching only when measured need exists)
- Dedicated vector DB (Pinecone etc.) — **pgvector on Supabase is the default** for embeddings/semantic search
- Any per-seat SaaS

## Default-stack bias
- Storage: Supabase Storage first; Cloudflare R2 only for heavy file egress.
- Background jobs: none until needed; then Trigger.dev or Inngest per Decision Engine.
- Feature flags: PostHog (already present) before any flags vendor.
- Secrets: platform env vars (e.g. Vercel) before a secrets manager.

## Verification
- PR reviewer checks new dependencies/services against this list.
- `STATUS.md` risk section flags any cost-bearing proposal awaiting L0.
