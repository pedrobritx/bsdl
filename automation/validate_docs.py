#!/usr/bin/env python3
"""BSF doc validator: front matter presence + relative-link integrity.
Run from repo root: python3 automation/validate_docs.py
Exit 0 = healthy; exit 1 = violations found. Wire into CI (see .github/workflows).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ("title:", "owner:", "status:", "last_updated:")
errors = []

md_files = []
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if not d.startswith(".") or d == ".github"]
    if "node_modules" in dirpath: continue
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(dirpath, f))

for path in md_files:
    rel = os.path.relpath(path, ROOT)
    text = open(path, encoding="utf-8").read()
    # front matter (root README is the public face; .github files follow GitHub's own format)
    if rel != "README.md" and not rel.startswith(".github"):
        if not text.startswith("---"):
            errors.append(f"{rel}: missing front matter")
        else:
            fm = text.split("---", 2)[1]
            for key in REQUIRED:
                if key not in fm:
                    errors.append(f"{rel}: front matter missing '{key.rstrip(':')}'")
    # relative markdown links
    for m in re.finditer(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)", text):
        target = m.group(1).split("#")[0]
        if not target: continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            errors.append(f"{rel}: broken link -> {m.group(1)}")

if errors:
    print(f"✗ {len(errors)} violation(s):")
    for e in errors: print("  " + e)
    sys.exit(1)
print(f"✓ {len(md_files)} documents validated. Front matter and links healthy.")
