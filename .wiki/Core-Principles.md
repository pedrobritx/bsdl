*The ten principles and why each exists.* — [[Home]]

The canonical list lives in the repo ([README.md](https://github.com/pedrobritx/bsf/blob/main/README.md)); this page is the rationale.

**1. AI-First.** Every project must be understandable by humans *and* AI. If context lives only in someone's head or a chat scrollback, the next session — human or machine — starts blind. Structure beats tribal knowledge.

**2. Single Source of Truth.** Information exists in exactly one authoritative document; everything else links. Duplication is how docs rot: two copies drift, and nobody knows which one is real. The ownership table in `docs/README.md` names the owner of every subject.

**3. Context Before Code.** No AI begins coding before understanding the project — that's why `START_HERE.md` prescribes a mandatory reading sequence. Code written without context is confident, fast, and wrong.

**4. Documentation Is Code.** Docs update in the same PR as the code they describe, and CI (`automation/validate_docs.py`) fails the build when structure breaks. Documentation that can go stale silently, will.

**5. Decisions Are Permanent.** Significant decisions become ADRs — superseded, never deleted. Six months from now, "why are we using X?" already has an answer, including the options that lost.

**6. Everything Has an Owner.** Every document, decision, and component has clear responsibility — a named role, not "the team". Unowned things decay unnoticed.

**7. Automation Over Repetition.** Repeatable work becomes playbooks, recipes, or templates. If you've explained it twice, encode it once.

**8. Human Oversight by Default.** AI proposes, humans approve — unless a delegation level explicitly grants autonomy. Autonomy is earned per decision class, not assumed globally. See [[Governance and Delegation]].

**9. Continuous Learning.** Every project feeds back lessons, mistakes, patterns, and preferences into `memory/`, and recurring decisions get promoted into the Decision Engine. The company gets smarter with every project.

**10. Framework Over Tooling.** BSF holds the memory, standards, and decision process — not the AI tool. Replace Claude with anything else and the company keeps functioning. This is why BSF is plain Markdown in a git repo.

---

**→ In the repository**
- [README.md](https://github.com/pedrobritx/bsf/blob/main/README.md) — the canonical ten
- [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) — how the principles become rules

See also: [[Governance and Delegation]] · [[Document Standards]]
