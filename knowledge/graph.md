---
title: Knowledge Graph
owner: All
status: Active
last_updated: 2026-07-01
---

# Knowledge Graph

The repository is a **graph, not a tree**. Each document owns one subject and links to the rest.

## Dependency chain (product → data)
```
VISION → PRODUCT → USER_STORIES → UX_FLOWS → SCREENS
  → DESIGN_SYSTEM components → API → SCHEMA → DATA_DICTIONARY
```

## Hubs
- `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/ARCHITECTURE.md` — technical hub. Names every system; links to owners.
- `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/product/PRODUCT.md` — product hub.
- `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/README.md` — global index.

## Rules
1. One source of truth — information lives in exactly one document.
2. Reference, don't duplicate — link to the owning document.
3. Every document declares `depends_on` and `related` in front matter.
4. `automation/validate_docs.py` checks links and front matter in CI.
