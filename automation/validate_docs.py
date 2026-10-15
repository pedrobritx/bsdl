#!/usr/bin/env python3
"""Check required front matter and the existing relative Markdown link scope.

Run from any directory: python3 automation/validate_docs.py
Use --root PATH to validate a different repository without copying this script.
Required metadata must use top-level, nonempty, single-line scalar values.
This is a bounded metadata check, not a YAML or full Markdown parser.
"""

import argparse
import os
from pathlib import Path
import re
import sys


REQUIRED = ("title", "owner", "status", "last_updated")
DELIMITER = re.compile(r"---[ \t]*")
RELATIVE_LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
EMPTY_VALUES = {"", "''", '""', "~", "null", "[]", "{}"}


def markdown_files(root):
    """Keep the existing traversal scope, including its node_modules rule."""
    documents = []
    for directory, directories, files in os.walk(root):
        directories[:] = sorted(
            name for name in directories
            if not name.startswith(".") or name == ".github"
        )
        if "node_modules" in directory:
            continue
        documents.extend(
            Path(directory) / name for name in sorted(files)
            if name.endswith(".md")
        )
    return documents


def has_nonempty_scalar(value):
    """Recognise the simple scalar metadata format used by this repository."""
    value = value.strip()
    if value.startswith(("'", '"')):
        quote = value[0]
        closing_quote = value.rfind(quote)
        if closing_quote == 0:
            return False
        content = value[1:closing_quote]
        remainder = value[closing_quote + 1:].strip()
        return bool(content.strip()) and (not remainder or remainder.startswith("#"))
    value = re.split(r"(?:^|[ \t]+)#", value, maxsplit=1)[0].strip()
    if value.lower() in EMPTY_VALUES or value.startswith(("[", "{")):
        return False
    # Block scalars require a YAML parser; required metadata stays single-line.
    return not re.fullmatch(r"[|>][+\-1-9]*", value)


def front_matter_errors(text, relative_path):
    if relative_path == Path("README.md") or relative_path.parts[0] == ".github":
        return []
    lines = text.splitlines()
    if not lines or not DELIMITER.fullmatch(lines[0]):
        return [f"{relative_path}: missing front matter opening delimiter"]
    closing = next(
        (index for index, line in enumerate(lines[1:], 1)
         if DELIMITER.fullmatch(line)),
        None,
    )
    if closing is None:
        return [f"{relative_path}: missing front matter closing delimiter"]
    front_matter = "\n".join(lines[1:closing])
    errors = []
    for key in REQUIRED:
        values = re.findall(rf"^{key}:[ \t]*(.*)$", front_matter, re.MULTILINE)
        if not values:
            errors.append(f"{relative_path}: front matter missing '{key}'")
        elif not all(has_nonempty_scalar(value) for value in values):
            errors.append(f"{relative_path}: front matter '{key}' needs a nonempty scalar value")
    return errors


def relative_link_errors(text, path, relative_path):
    errors = []
    for match in RELATIVE_LINK.finditer(text):
        target = match.group(1).split("#")[0]
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(path.parent, target))
        if not os.path.exists(resolved):
            errors.append(f"{relative_path}: broken link -> {match.group(1)}")
    return errors


def validate_documents(root):
    documents = markdown_files(root)
    errors = []
    for path in documents:
        relative_path = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{relative_path}: cannot read document: {error}")
            continue
        errors.extend(front_matter_errors(text, relative_path))
        errors.extend(relative_link_errors(text, path, relative_path))
    return len(documents), errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1],
        help="repository root (default: the parent of this script's directory)",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"repository root is not a directory: {root}")
    count, errors = validate_documents(root)
    if errors:
        print(f"✗ {len(errors)} violation(s):")
        for error in errors:
            print("  " + error)
        return 1
    print(f"✓ {count} documents validated. Front matter and links healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
