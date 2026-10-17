"""A0 routing and evidence-contract tests; no LLM/provider calls or writes to GitHub."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation"))
import a0
import constellation


class A0Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.workspace = self.root / "workspace"
        self.workspace.mkdir()
        self.product = self.root / "product"
        self.product.mkdir()
        for repo in ("polaris", "axis", "meridian", "sentinel"):
            location = self.workspace / repo
            location.mkdir()
            (location / "AGENTS.md").write_text("Repository instructions", encoding="utf-8")
            if repo == "polaris":
                for name in constellation.GOVERNANCE_CONTEXT:
                    target = location / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text("Governance guidance", encoding="utf-8")
            else:
                manifest = {
                    "version": 1, "id": repo, "repository": f"pedrobritx/{repo}",
                    "entrypoint": "AGENTS.md", "context": ["AGENTS.md"],
                    "owns": ["methods"], "outputs": ["reviewed results"],
                }
                (location / "discipline.json").write_text(json.dumps(manifest))
            self.commit(location)
        (self.product / "README.md").write_text("Adopter context", encoding="utf-8")
        self.commit(self.product)
        self.config = {
            "version": 1, "project": "example/product", "governance": "polaris",
            "disciplines": {k: {"enabled": True} for k in ("axis", "meridian", "sentinel")},
        }
        self.intake = {
            "version": 1, "id": "feature-001", "objective": "Add an accessible editor",
            "context": ["README.md"], "acceptance_criteria": ["Existing documents remain readable"],
            "signals": {k: False for k in a0.SIGNALS},
            "host": {"name": "codex", "subagents": False, "isolated_worktrees": False},
        }
        self.result = {
            "version": 1, "request_id": "feature-001", "project": "example/product",
            "source_revision": "a" * 40, "execution": "completed",
            "verification": "passed", "approval": "pending",
            "checks": [{"command": "python -m unittest", "exit_code": 0,
                        "source_revision": "a" * 40, "evidence_ref": "logs/ci-run-123"}],
            "artifacts": ["src/editor.py"], "documentation": ["docs/editor.md"],
            "coverage_gaps": [], "unresolved_findings": [],
        }

    def commit(self, location):
        subprocess.run(["git", "init", "-q", str(location)], check=True)
        subprocess.run(["git", "-C", str(location), "add", "."], check=True)
        subprocess.run(["git", "-C", str(location), "-c", "user.name=Test",
                        "-c", "user.email=test@example.com", "commit", "-qm", "fixture"], check=True)

    def route(self):
        return a0.route_request(self.config, self.intake, self.workspace, self.product)

    def test_unified_default_and_provenance(self):
        self.intake["signals"]["implementation"] = True
        result = self.route()
        self.assertEqual(result["routing"]["mode"], "unified")
        self.assertEqual(result["routing"]["disciplines"], ["axis"])
        self.assertEqual(len(result["product_source"]["revision"]), 40)
        self.assertEqual(result["preflight_status"], "ready")
        self.assertEqual(result["composition"]["tasks"][0]["status"], "planned")
        self.assertEqual(result["composition"]["tasks"][0]["evidence"], [])

    def test_parallel_only_for_independent_isolated_work(self):
        self.intake["signals"].update(implementation=True, interface=True, independent_workstreams=True)
        self.intake["host"].update(subagents=True, isolated_worktrees=True)
        self.assertEqual(self.route()["routing"]["mode"], "parallel")
        self.intake["host"]["isolated_worktrees"] = False
        self.assertEqual(self.route()["routing"]["mode"], "unified")

    def test_coordinated_shared_interfaces(self):
        self.intake["signals"].update(architecture=True, interface=True, shared_interfaces=True)
        self.intake["host"]["subagents"] = True
        result = self.route()
        self.assertEqual(result["routing"]["mode"], "coordinated")

    def test_optout_does_not_claim_coverage(self):
        self.intake["signals"]["security"] = True
        self.config["disciplines"]["sentinel"] = {"enabled": False, "reason": "External reviewer required"}
        result = self.route()
        self.assertEqual(result["preflight_status"], "needs-coverage")
        self.assertEqual(result["composition"]["coverage_gaps"][0]["discipline"], "sentinel")

    def test_disabled_unrequested_capability_is_not_loaded(self):
        self.config["disciplines"]["meridian"] = {"enabled": False, "reason": "Different design"}
        self.intake["signals"]["implementation"] = True
        (self.workspace / "meridian").rename(self.workspace / "not-installed")
        self.assertEqual(self.route()["preflight_status"], "ready")

    def test_invalid_host_and_signal_rejected(self):
        self.intake["signals"]["security"] = "yes"
        with self.assertRaisesRegex(ValueError, "boolean"):
            self.route()
        self.intake["signals"]["security"] = False
        self.intake["host"]["name"] = "arbitrary-provider"
        with self.assertRaisesRegex(ValueError, "codex"):
            self.route()

    def test_path_traversal_and_missing_context_rejected(self):
        self.intake["context"] = ["../private.txt"]
        with self.assertRaisesRegex(ValueError, "outside|missing"):
            self.route()
        self.intake["context"] = ["missing-file.md"]
        with self.assertRaisesRegex(ValueError, "outside|missing"):
            self.route()

    def test_governance_none_is_supported(self):
        self.config["governance"] = "none"
        (self.workspace / "polaris").rename(self.workspace / "polaris-unused")
        result = self.route()
        self.assertIsNone(result["composition"]["governance_context"])

    def test_duplicate_signals_and_inconsistent_host(self):
        del self.intake["signals"]["security"]
        with self.assertRaisesRegex(ValueError, "expected exactly"):
            self.route()
        self.intake["signals"]["security"] = False
        self.intake["host"].update(subagents=False, isolated_worktrees=True)
        with self.assertRaisesRegex(ValueError, "cannot be available"):
            self.route()

    def test_result_is_only_reported_evidence(self):
        valid = a0.validate_result(self.result)
        self.assertEqual(valid["status"], "schema-valid")
        self.assertIn("not independently", valid["assurance"])

    def test_passing_result_requires_actual_reported_check(self):
        for new in ([], [{**self.result["checks"][0], "exit_code": 1}]):
            result = copy.deepcopy(self.result)
            result["checks"] = new
            with self.assertRaises(ValueError):
                a0.validate_result(result)

    def test_stale_or_missing_evidence_fails(self):
        result = copy.deepcopy(self.result)
        result["checks"][0]["source_revision"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "Stale"):
            a0.validate_result(result)
        result["checks"][0]["source_revision"] = "a" * 40
        result["checks"][0]["evidence_ref"] = ""
        with self.assertRaises(ValueError):
            a0.validate_result(result)

    def test_open_critical_risk_and_gap_prevent_pass(self):
        for name, payload in (
            ("coverage_gaps", ["No security review"]),
            ("unresolved_findings", [{"severity": "high", "description": "Missing authorization"}]),
        ):
            result = copy.deepcopy(self.result)
            result[name] = payload
            with self.assertRaises(ValueError):
                a0.validate_result(result)

    def test_blocked_execution_never_passes(self):
        self.result["execution"] = "blocked"
        with self.assertRaises(ValueError):
            a0.validate_result(self.result)

    def test_cli_reports_no_false_execution(self):
        self.intake["signals"]["implementation"] = True
        path_config, path_intake = self.root / "config.json", self.root / "intake.json"
        path_config.write_text(json.dumps(self.config))
        path_intake.write_text(json.dumps(self.intake))
        cmd = [sys.executable, str(ROOT / "automation/a0.py"), "route",
               "--config", str(path_config), "--intake", str(path_intake),
               "--workspace", str(self.workspace), "--product-root", str(self.product)]
        out = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(json.loads(out.stdout)["routing"]["disciplines"], ["axis"])
        self.assertEqual(json.loads(out.stdout)["composition"]["tasks"][0]["status"], "planned")


if __name__ == "__main__":
    unittest.main()
