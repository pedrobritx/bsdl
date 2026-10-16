#!/usr/bin/env python3
"""Reject retired product identities in current tracked paths and text."""

from pathlib import Path
import re
import subprocess

RETIRED = tuple(bytes.fromhex(value).decode() for value in ("6273646c", "6264736c", "627366"))
BRANDING = re.compile(r"(?<![a-z0-9])(?:" + "|".join(RETIRED) + r")(?![a-z0-9])", re.I)


def violations(path, data):
    errors = []
    if BRANDING.search(path):
        errors.append(f"{path}: retired identity in path")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return errors
    for number, line in enumerate(text.splitlines(), 1):
        if BRANDING.search(line):
            errors.append(f"{path}:{number}: retired product identity")
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    errors = []
    for name in filter(None, paths):
        path = root / name
        if path.is_file():
            errors.extend(violations(name, path.read_bytes()))
    if errors:
        print("\n".join(errors))
        return 1
    print("Current tracked paths and text use canonical product identities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
