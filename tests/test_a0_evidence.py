"""A0 local evidence integrity tests: no external providers and no real user data."""

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation"))
import a0_evidence


class EvidenceAuditTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.product = self.root / "product"
        self.product.mkdir()
        self.evidence = self.root / "evidence"
        self.evidence.mkdir()
        subprocess.run(["git", "init", "-q", str(self.product)], check=True)
        (self.product / "README.md").write_text("Synthetic project\n", encoding="utf-8")
        self.commit()
        self.rev = subprocess.check_output(
            ["git", "-C", str(self.product), "rev-parse", "HEAD"], text=True
        ).strip()
        (self.evidence / "stdout.log").write_text("2 tests passed\n", encoding="utf-8")
        (self.evidence / "stderr.log").write_text("", encoding="utf-8")
        self.receipt = {
            "version": 1, "request_id": "fixture-001",
            "project": "example/product", "source_revision": self.rev,
            "command": "python -m unittest discover", "exit_code": 0,
            "stdout_path": "stdout.log",
            "stdout_sha256": hashlib.sha256((self.evidence / "stdout.log").read_bytes()).hexdigest(),
            "stderr_path": "stderr.log",
            "stderr_sha256": hashlib.sha256((self.evidence / "stderr.log").read_bytes()).hexdigest(),
        }
        self.write_receipt()
        self.report = {
            "version": 1, "request_id": "fixture-001", "project": "example/product",
            "source_revision": self.rev, "execution": "completed",
            "verification": "passed", "approval": "pending",
            "checks": [{
                "command": self.receipt["command"], "exit_code": 0,
                "source_revision": self.rev, "evidence_ref": "receipt.json",
            }],
            "artifacts": ["README.md"], "documentation": ["README.md"],
            "coverage_gaps": [], "unresolved_findings": [],
        }

    def commit(self):
        subprocess.run(["git", "-C", str(self.product), "add", "."], check=True)
        subprocess.run(
            ["git", "-C", str(self.product), "-c", "user.name=Fixture",
             "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Fixture"],
            check=True,
        )

    def write_receipt(self):
        (self.evidence / "receipt.json").write_text(
            json.dumps(self.receipt), encoding="utf-8",
        )

    def audit(self):
        return a0_evidence.audit_result(self.report, self.product, self.evidence)

    def test_valid_receipt_is_consistent_but_not_attested(self):
        result = self.audit()
        self.assertEqual(result["status"], "local-receipts-consistent")
        self.assertEqual(result["source_revision"], self.rev)
        self.assertEqual(result["verified_local_receipts"], ["receipt.json"])
        self.assertEqual(result["approval"], "pending")
        self.assertIn("still require review", result["assurance"])

    def test_changed_log_detected(self):
        (self.evidence / "stdout.log").write_text("different\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            self.audit()

    def test_missing_or_escaping_receipt_rejected(self):
        self.report["checks"][0]["evidence_ref"] = "../outside.json"
        with self.assertRaisesRegex(ValueError, "missing or escapes"):
            self.audit()
        self.report["checks"][0]["evidence_ref"] = "missing.json"
        with self.assertRaisesRegex(ValueError, "missing or escapes"):
            self.audit()

    def test_receipt_mismatch_rejected(self):
        self.receipt["exit_code"] = 1
        self.write_receipt()
        with self.assertRaisesRegex(ValueError, "exit_code"):
            self.audit()

    def test_dirty_checkout_rejected(self):
        (self.product / "README.md").write_text("Uncommitted changes\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "uncommitted"):
            self.audit()

    def test_moved_head_is_stale(self):
        (self.product / "new.md").write_text("New commit\n", encoding="utf-8")
        self.commit()
        with self.assertRaisesRegex(ValueError, "HEAD differs"):
            self.audit()

    def test_invalid_pass_claim_is_rejected_by_existing_schema(self):
        self.report["checks"][0]["exit_code"] = 1
        with self.assertRaises(ValueError):
            self.audit()

    def test_missing_log_rejected(self):
        (self.evidence / "stderr.log").unlink()
        with self.assertRaisesRegex(ValueError, "missing or escapes"):
            self.audit()

    def test_oversized_log_rejected(self):
        with (self.evidence / "stdout.log").open("wb") as f:
            f.truncate(a0_evidence.MAX_LOG_BYTES + 1)
        self.receipt["stdout_sha256"] = hashlib.sha256(b"arbitrary").hexdigest()
        self.write_receipt()
        with self.assertRaisesRegex(ValueError, "exceeds"):
            self.audit()

    def test_cli_audit_reads_receipt_and_returns_json(self):
        file = self.root / "result.json"
        file.write_text(json.dumps(self.report), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(ROOT / "automation/a0_evidence.py"),
             "--result", str(file), "--product-root", str(self.product),
             "--evidence-root", str(self.evidence)],
            capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(
            json.loads(proc.stdout)["status"], "local-receipts-consistent",
        )


if __name__ == "__main__":
    unittest.main()
