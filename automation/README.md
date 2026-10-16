---
title: Automation
owner: DevOps Engineer
status: Active
last_updated: 2026-10-15
---

# Automation

Scripts that keep the framework honest (Automation Over Repetition).

| Script | Does |
|---|---|
| `validate_docs.py` | Checks required front matter + existing relative-link scope. Runs in CI on every PR. |

## Documentation validation

Run `python3 automation/validate_docs.py` from any directory. The repository root defaults to the parent of the script directory. Use `--root PATH` to validate another checkout. Exit codes are 0 for success, 1 for documentation violations, and 2 for invalid CLI arguments or roots.

Required metadata is `title`, `owner`, `status`, and `last_updated`, each on its own top-level line with a nonempty, single-line scalar value between standalone `---` delimiters. Empty values, quoted whitespace, null markers, unquoted flow collections (empty or populated), and block scalar markers do not satisfy a required field. Quoted collection-looking text is accepted as a scalar. This bounded check does not parse or validate full YAML, field types, duplicate keys, dates, status vocabulary, `depends_on`, or `related`.

The root `README.md` and files under `.github/` are exempt from front matter checks; their relative links are still checked. Hidden directories other than `.github/`, including `.wiki/`, are skipped. The existing `node_modules` path substring exclusion is retained.

Relative links retain the original expression and file-existence check. HTTP(S), `mailto:`, and fragment-only links are skipped. Link anchors, network availability, reference-style links, HTML links, complex Markdown destinations, and wiki navigation are outside this check. A green run is not a general documentation or migration-readiness verdict.

Run the [CLI regression tests](../tests/test_validate_docs.py) with `python3 -m unittest discover -s tests -v`.

## Planned
- Dependency-graph builder from front matter (`depends_on`/`related` → visual graph)
- Stale-doc detector (`last_updated` vs git history of owned code)
- HANDOFF/STATUS freshness check at PR time
