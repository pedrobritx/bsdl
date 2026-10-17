#!/usr/bin/env python3
"""Audit *locally captured* A0 check receipts against their files and Git HEAD.

This never runs commands, calls a provider, changes repository files or proves
that an external agent actually ran the claimed command. It verifies integrity
and consistency of local records for subsequent human/CI review.
"""

import argparse
import hashlib
import json
from pathlib import Path
import sys

from a0 import validate_result
from constellation import read_json, source, object_keys, nonempty, version_one

RECEIPT_KEYS = (
    "version", "request_id", "project", "source_revision", "command",
    "exit_code", "stdout_path", "stdout_sha256", "stderr_path", "stderr_sha256",
)
MAX_LOG_BYTES = 10 * 1024 * 1024


def contained_file(root: Path, relative: str):
    nonempty(relative, "local evidence file")
    if Path(relative).is_absolute():
        raise ValueError("Evidence file must use a relative path")
    base = root.resolve()
    path = (base / relative).resolve()
    if not path.is_relative_to(base) or not path.is_file():
        raise ValueError("Evidence file missing or escapes the permitted evidence directory")
    return path


def hash_file(path: Path):
    if path.stat().st_size > MAX_LOG_BYTES:
        raise ValueError("Evidence log exceeds the configured 10 MiB integrity limit")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_result(result, product_root: Path, evidence_root: Path):
    """Validate shape, current checkout revision and local receipt integrity."""
    validate_result(result)
    product_root = product_root.resolve()
    evidence_root = evidence_root.resolve()
    actual = source(product_root, result["project"])
    if actual["revision"] != result["source_revision"]:
        raise ValueError("Product HEAD differs from the recorded result revision")
    if actual["dirty"]:
        raise ValueError("Product checkout has uncommitted changes; record a reviewed revision")

    confirmed = []
    for index, check in enumerate(result["checks"]):
        receipt_path = contained_file(evidence_root, check["evidence_ref"])
        receipt = read_json(receipt_path)
        object_keys(receipt, RECEIPT_KEYS, f"receipt[{index}]")
        version_one(receipt["version"], f"receipt[{index}]")
        for key in ("request_id", "project", "source_revision"):
            if receipt[key] != result[key]:
                raise ValueError(f"Receipt {key} does not match the result")
        for key in ("command", "exit_code"):
            if receipt[key] != check[key]:
                raise ValueError(f"Receipt {key} does not match the reported check")
        for stem in ("stdout", "stderr"):
            path = contained_file(evidence_root, receipt[f"{stem}_path"])
            expected = receipt[f"{stem}_sha256"]
            if not isinstance(expected, str) or len(expected) != 64:
                raise ValueError(f"Invalid {stem} digest")
            if hash_file(path) != expected:
                raise ValueError(f"{stem} evidence digest mismatch")
        confirmed.append(check["evidence_ref"])

    return {
        "status": "local-receipts-consistent",
        "source_revision": actual["revision"],
        "verified_local_receipts": confirmed,
        "assurance": (
            "Local file integrity and Git consistency only; command execution, "
            "subagent claims, accessibility/security and CI origin still require review"
        ),
        "approval": result["approval"],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--product-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = audit_result(read_json(args.result), args.product_root, args.evidence_root)
    except (OSError, ValueError) as error:
        print("A0 evidence audit failed: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
