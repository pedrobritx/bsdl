import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("constellation", ROOT / "automation/constellation.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.config = {
            "version": 1, "project": "example/product", "governance": "polaris",
            "disciplines": {name: {"enabled": True} for name in MODULE.DISCIPLINES},
        }
        self.request = {
            "version": 1, "id": "feature-1", "objective": "Build an accessible editor",
            "context": ["README.md"], "acceptance_criteria": ["Existing documents remain readable"],
            "disciplines": list(MODULE.DISCIPLINES),
        }
        for name in ("polaris", *MODULE.DISCIPLINES):
            repo = self.workspace / name
            repo.mkdir()
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / "AGENTS.md").write_text("Repository instructions", encoding="utf-8")
            if name == "polaris":
                for path in MODULE.GOVERNANCE_CONTEXT:
                    target = repo / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text("Governance context", encoding="utf-8")
            else:
                manifest = {
                    "version": 1, "id": name, "repository": f"pedrobritx/{name}",
                    "entrypoint": "AGENTS.md", "context": ["AGENTS.md"],
                    "owns": [f"{name} reusable capability"],
                    "outputs": [f"{name} task evidence"],
                }
                (repo / "discipline.json").write_text(json.dumps(manifest), encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
            subprocess.run([
                "git", "-C", str(repo), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
                "commit", "-qm", "fixture",
            ], check=True)

    def plan(self):
        return MODULE.plan(self.config, self.request, self.workspace)

    def test_every_opt_out_combination_is_independent(self):
        for enabled in itertools.product((False, True), repeat=3):
            with self.subTest(enabled=enabled):
                self.config["disciplines"] = {
                    name: {"enabled": flag, **({} if flag else {"reason": "Project owner covers this scope"})}
                    for name, flag in zip(MODULE.DISCIPLINES, enabled)
                }
                result = self.plan()
                self.assertEqual([task["discipline"] for task in result["tasks"]],
                                 [name for name, flag in zip(MODULE.DISCIPLINES, enabled) if flag])
                self.assertEqual(len(result["coverage_gaps"]), enabled.count(False))
                self.assertEqual(result["status"], "ready" if all(enabled) else "needs-coverage")
                self.assertTrue(all(task["status"] == "planned" and task["evidence"] == [] for task in result["tasks"]))

    def test_disabled_repository_is_not_required(self):
        self.config["disciplines"]["sentinel"] = {"enabled": False, "reason": "External security reviewer"}
        self.workspace.joinpath("sentinel").rename(self.workspace / "absent")
        self.assertEqual(self.plan()["coverage_gaps"][0]["discipline"], "sentinel")

    def test_unrequested_enabled_repository_is_not_required(self):
        self.request["disciplines"] = ["meridian"]
        self.workspace.joinpath("axis").rename(self.workspace / "absent")
        result = self.plan()
        self.assertEqual([task["discipline"] for task in result["tasks"]], ["meridian"])
        self.assertEqual(result["coverage_gaps"], [])

    def test_standalone_plan_does_not_load_governance(self):
        self.config["governance"] = "none"
        self.workspace.joinpath("polaris").rename(self.workspace / "absent")
        self.assertIsNone(self.plan()["governance_context"])

    def test_governed_plan_requires_complete_constitution(self):
        (self.workspace / "polaris" / MODULE.GOVERNANCE_CONTEXT[-1]).unlink()
        with self.assertRaisesRegex(ValueError, "context.*missing"):
            self.plan()

    def test_source_revisions_and_modified_work_are_visible(self):
        result = self.plan()
        self.assertRegex(result["tasks"][0]["source"]["revision"], r"^[0-9a-f]{40}$")
        self.assertFalse(result["tasks"][0]["source"]["dirty"])
        (self.workspace / "axis/AGENTS.md").write_text("Changed locally", encoding="utf-8")
        self.assertTrue(self.plan()["tasks"][0]["source"]["dirty"])

    def test_no_discipline_is_needed_for_governance_only_work(self):
        self.request["disciplines"] = []
        self.assertEqual(self.plan()["tasks"], [])

    def test_missing_enabled_source_never_silently_disappears(self):
        (self.workspace / "axis/discipline.json").unlink()
        with self.assertRaisesRegex(ValueError, "discipline.json"):
            self.plan()

    def test_wrong_repository_manifest_is_rejected(self):
        target = self.workspace / "axis/discipline.json"
        data = json.loads(target.read_text())
        data["repository"] = "someone/meridian"
        target.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "repository"):
            self.plan()

    def test_manifest_context_cannot_escape_capability_checkout(self):
        target = self.workspace / "axis/discipline.json"
        data = json.loads(target.read_text())
        data["entrypoint"] = "../meridian/AGENTS.md"
        target.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "within"):
            self.plan()

    def test_malformed_configuration_is_rejected(self):
        for mutate in (
            lambda c: c.update(version=True),
            lambda c: c.update(governance="automatic"),
            lambda c: c.update(extra=True),
            lambda c: c["disciplines"].pop("sentinel"),
            lambda c: c["disciplines"].update(sentinell={"enabled": True}),
            lambda c: c["disciplines"]["axis"].update(enabled="false"),
            lambda c: c["disciplines"]["axis"].update(enabled=False),
            lambda c: c["disciplines"]["axis"].update(enabled=False, reason=" "),
        ):
            original = copy.deepcopy(self.config)
            mutate(self.config)
            with self.subTest(config=self.config), self.assertRaises(ValueError):
                self.plan()
            self.config = original

    def test_malformed_requests_are_rejected(self):
        for mutate in (
            lambda r: r.update(disciplines=["sentinell"]),
            lambda r: r.update(disciplines=["axis", "axis"]),
            lambda r: r.update(acceptance_criteria=[]),
            lambda r: r.update(objective=" "),
            lambda r: r.update(context="README.md"),
            lambda r: r.update(shell="run this"),
        ):
            original = copy.deepcopy(self.request)
            mutate(self.request)
            with self.subTest(request=self.request), self.assertRaises(ValueError):
                self.plan()
            self.request = original

    def test_cli_is_read_only_and_emits_json(self):
        config = self.workspace / "project.json"
        request = self.workspace / "request.json"
        config.write_text(json.dumps(self.config))
        request.write_text(json.dumps(self.request))
        command = ["python3", str(ROOT / "automation/constellation.py"), "--config", str(config),
                   "--request", str(request), "--workspace", str(self.workspace)]
        run = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)["project"], "example/product")
        config.write_text('{"version": 1, "version": 2}')
        run = subprocess.run(command, text=True, capture_output=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertEqual(run.stdout, "")
        self.assertIn("duplicate", run.stderr)


if __name__ == "__main__":
    unittest.main()
