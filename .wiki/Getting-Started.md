> Current migration note: Polaris owns governance; Axis engineering/project templates, Meridian design and Sentinel security guidance are independently usable. Current operating rules permit reversible work within approved scope; Draft policies grant no authority. Historical BSF descriptions below are interpreted through [current operating rules](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/PROJECT_RULES.md).

*From zero to a scaffolded, governed project.* — [[Home]]

## Three ways to adopt BSF

1. **Use this template** — click the green **Use this template** button on [the repository](https://github.com/pedrobritx/bsf) to start a new repo with the full 119-file skeleton.
2. **CLI** — `gh repo create myapp --template pedrobritx/bsf --private --clone`
3. **Claude skill** — if the `britx-software-framework` skill is installed, its `scaffold.py` generates the skeleton into any directory.

All three produce the same thing: the framework's directory tree with every core document, agent, playbook, recipe, constraint, and the CI validator already wired.

## The post-scaffold interview

The skeleton is generic on purpose. Before the first feature, make it *yours*:

1. **Fill the product docs** — `docs/product/VISION.md` (why this exists) and `docs/product/PRODUCT.md` (what it does, for whom). Everything downstream depends on these.
2. **Confirm delegation defaults** — the project default is **L2** (AI recommends, human confirms). If you want more or less autonomy per decision class, set it in `PROJECT_RULES.md` and per-policy in `decisions/decision-engine/`.
3. **Seed your deviations** — the Decision Engine ships with opinionated defaults (e.g. Supabase Auth, pgvector). Where your stack differs, edit the policy files now so the AI never applies a default you don't want.

## Your first session

Point your AI tool at [`START_HERE.md`](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/START_HERE.md). It walks the mandatory onboarding sequence — constitution, vision, product, architecture, roadmap, status, handoff — then has the AI identify its role, pick a playbook, check the Decision Engine and memory, and respect constraints. Sessions end by updating `HANDOFF.md` and `STATUS.md`: *a session that doesn't hand off didn't happen.*

Then set up your work boards: [[Project Boards]].

---

**→ In the repository**
- [START_HERE.md](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/START_HERE.md) — the onboarding sequence
- [PROJECT_RULES.md](https://github.com/pedrobritx/polaris/blob/refactor/polaris-capability-extraction/PROJECT_RULES.md) — delegation defaults live here
- [docs/product/VISION.md](https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/product/VISION.md) · [docs/product/PRODUCT.md](https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/product/PRODUCT.md)
- [decisions/decision-engine/](https://github.com/pedrobritx/bsf/tree/main/decisions/decision-engine)

See also: [[Core Principles]] · [[Governance and Delegation]] · [[Project Boards]]
