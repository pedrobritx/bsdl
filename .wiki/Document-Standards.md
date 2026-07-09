*How every document in the repository is shaped — and why uniformity is the point.* — [[Home]]

## The universal layout

Every document follows `templates/DOCUMENT_TEMPLATE.md`: YAML front matter plus six sections. Humans and AI always know where to look.

**Front matter fields:**

- `title` — the document's name.
- `owner` — the responsible role (`Product | Design | Engineering | Business | All`). Everything has an owner.
- `status` — `Draft | Active | Deprecated`. Deprecated docs keep their history and point to a successor.
- `last_updated` — `YYYY-MM-DD`.
- `depends_on` — documents you must read to understand this one.
- `related` — documents that reference this one. Together these two make the [[Memory and Knowledge]] graph machine-readable.

**The six sections:** *Purpose* (one sentence — a doc with more than one Purpose sentence probably owns too much and should split), *Scope* (what belongs here and what does NOT, naming the owning doc), *Related Documents*, *Contents* (the actual material — reference, don't duplicate), *Decisions* (links to ADRs, never restated), *Open Questions* (each with an owner).

## The ownership principle

Information lives in exactly one owning document; every other doc links. The ownership table in [`docs/README.md`](https://github.com/pedrobritx/bsf/blob/main/docs/README.md) names the owner of every subject — VISION owns *why*, PRODUCT owns *what*, API owns endpoints, SCHEMA owns database structure, and so on. The canonical example: *"JWT expiration is defined in `SECURITY.md`"* — a link, never a copy.

## Enforcement in CI

[`automation/validate_docs.py`](https://github.com/pedrobritx/bsf/blob/main/automation/validate_docs.py) runs on every push and PR (`.github/workflows/docs-validate.yml`). It fails the build if any Markdown file is missing front matter (or the `title/owner/status/last_updated` keys), or if any relative link points to a file that doesn't exist. Structure isn't a style guide here — it's a passing check. *Documentation Is Code.*

---

**→ In the repository**
- [templates/DOCUMENT_TEMPLATE.md](https://github.com/pedrobritx/bsf/blob/main/templates/DOCUMENT_TEMPLATE.md) — the template itself
- [docs/README.md](https://github.com/pedrobritx/bsf/blob/main/docs/README.md) — index + ownership table
- [automation/validate_docs.py](https://github.com/pedrobritx/bsf/blob/main/automation/validate_docs.py) — the validator

See also: [[Core Principles]]
