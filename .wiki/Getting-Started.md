> Current migration note: Polaris owns governance; Axis engineering/project templates, Meridian design and Sentinel security guidance are independently usable. Current operating rules permit reversible work within approved scope; Draft policies grant no authority. Historical Axis descriptions below are interpreted through [current operating rules](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/PROJECT_RULES.md).

*From zero to a scaffolded, governed project.* — [[Home]]

## Adopt the capability deliberately

Start from [Axis](https://github.com/pedrobritx/axis) and select its engineering templates. The template button and an external scaffold skill are not verified distribution channels. Use the documented repository files rather than assuming a published generator or a fixed file count.

Full Polaris governance is a separate explicit adoption. Axis, Meridian and Sentinel retain their own essential quality and safety requirements when used independently.

## The post-scaffold interview

The skeleton is generic on purpose. Before the first feature, make it *yours*:

1. **Fill the product docs** — `docs/product/VISION.md` (why this exists) and `docs/product/PRODUCT.md` (what it does, for whom). Everything downstream depends on these.
2. **Confirm delegation defaults** — agents may complete reversible work within approved scope; unresolved consequential decisions require human review. Record the selected policy in `PROJECT_RULES.md` and per-policy in `decisions/decision-engine/`.
3. **Seed your deviations** — the Decision Engine ships with opinionated defaults (e.g. Supabase Auth, pgvector). Where your stack differs, edit the policy files now so the AI never applies a default you don't want.

## Your first session

Point your AI tool at [`START_HERE.md`](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/START_HERE.md). It walks the mandatory onboarding sequence — constitution, vision, product, architecture, roadmap, status, handoff — then has the AI identify its role, pick a playbook, check the Decision Engine and memory, and respect constraints. Sessions end by updating `HANDOFF.md` and `STATUS.md`: *a session that doesn't hand off didn't happen.*

Then set up your work boards: [[Project Boards]].

---

**→ In the repository**
- [START_HERE.md](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/START_HERE.md) — the onboarding sequence
- [PROJECT_RULES.md](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/PROJECT_RULES.md) — delegation defaults live here
- [docs/product/VISION.md](https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/product/VISION.md) · [docs/product/PRODUCT.md](https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/product/PRODUCT.md)
- [decisions/decision-engine/](https://github.com/pedrobritx/axis/tree/2cb53bfc96824c71d8b57c5e5340f29f1c41ccb5/decisions/decision-engine)

See also: [[Core Principles]] · [[Governance and Delegation]] · [[Project Boards]]
