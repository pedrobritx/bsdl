#!/usr/bin/env python3
"""Build a read-only handoff plan from explicitly selected local capabilities.

This does not infer disciplines, execute agents, fetch repositories or approve work.
The coordinating human/agent reads project context and selects the request scope.
"""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


DISCIPLINES = ("axis", "meridian", "sentinel")
GOVERNANCE_CONTEXT = (
    "AGENTS.md", "START_HERE.md", "PROJECT_RULES.md", "integration/README.md",
    "polaris/constitution/README.md",
    "polaris/constitution/preamble.md", "polaris/constitution/foundations.md",
    "polaris/constitution/principles.md", "polaris/constitution/engineering-laws.md",
    "polaris/constitution/derived-frameworks.md", "polaris/constitution/reference-implementations.md",
)


def object_keys(value, required, label):
    if not isinstance(value, dict) or set(value) != set(required):
        raise ValueError(f"{label}: expected exactly {', '.join(required)}")


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: expected nonempty text")


def text_list(value, label, allow_empty=False):
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValueError(f"{label}: expected a list of text values")
    for item in value:
        nonempty(item, label)
    if len(set(value)) != len(value):
        raise ValueError(f"{label}: duplicate values")


def version_one(value, label):
    if type(value) is not int or value != 1:
        raise ValueError(f"{label}: only version 1 is supported")


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("JSON contains a duplicate key")
        result[key] = value
    return result


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot read valid JSON from {path.name}") from error


def local_document(root, name):
    nonempty(name, "context path")
    target = (root / name).resolve()
    if Path(name).is_absolute() or not target.is_relative_to(root.resolve()):
        raise ValueError("context path must stay within its capability checkout")
    if not target.is_file():
        raise ValueError(f"{root.name}: context document missing: {name}")
    return name


def source(root, repository):
    def git(*args):
        return subprocess.check_output(
            ["git", "--no-optional-locks", "-C", str(root), *args],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()

    try:
        if Path(git("rev-parse", "--show-toplevel")).resolve() != root.resolve():
            raise ValueError(f"{root.name}: expected a separate capability checkout")
        revision = git("rev-parse", "HEAD")
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError(f"{root.name}: expected an immutable Git revision")
        dirty = bool(git("status", "--porcelain", "--untracked-files=normal"))
    except (OSError, subprocess.CalledProcessError) as error:
        raise ValueError(f"{root.name}: a committed Git checkout is required") from error
    return {"repository": repository, "revision": revision, "dirty": dirty}


def capability(root, name):
    data = read_json(root / "discipline.json")
    object_keys(data, ("version", "id", "repository", "entrypoint", "context", "owns", "outputs"),
                f"{name} manifest")
    version_one(data["version"], f"{name} manifest")
    if data["id"] != name or data["repository"] != f"pedrobritx/{name}":
        raise ValueError(f"{name}: manifest id/repository does not match the selected discipline")
    local_document(root, data["entrypoint"])
    for key in ("context", "owns", "outputs"):
        text_list(data[key], f"{name}.{key}")
    for path in data["context"]:
        local_document(root, path)
    return data


def plan(config, request, workspace):
    object_keys(config, ("version", "project", "governance", "disciplines"), "project configuration")
    version_one(config["version"], "project configuration")
    if not isinstance(config["project"], str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", config["project"]):
        raise ValueError("project: expected owner/repository")
    if config["governance"] not in ("polaris", "none"):
        raise ValueError("governance: select polaris or none explicitly")
    object_keys(config["disciplines"], DISCIPLINES, "disciplines")
    for name, selection in config["disciplines"].items():
        if not isinstance(selection, dict) or type(selection.get("enabled")) is not bool:
            raise ValueError(f"{name}.enabled: expected a boolean")
        object_keys(selection, ("enabled",) if selection["enabled"] else ("enabled", "reason"), name)
        if not selection["enabled"]:
            nonempty(selection["reason"], f"{name}.reason")

    object_keys(request, ("version", "id", "objective", "context", "acceptance_criteria", "disciplines"), "request")
    version_one(request["version"], "request")
    for key in ("id", "objective"):
        nonempty(request[key], f"request.{key}")
    for key in ("context", "acceptance_criteria", "disciplines"):
        text_list(request[key], f"request.{key}", allow_empty=key == "disciplines")
    if set(request["disciplines"]) - set(DISCIPLINES):
        raise ValueError("request.disciplines: unknown discipline")

    workspace = workspace.resolve()
    governance = None
    if config["governance"] == "polaris":
        root = workspace / "polaris"
        governance = {
            "source": source(root, "pedrobritx/polaris"),
            "required_reading": [local_document(root, path) for path in GOVERNANCE_CONTEXT],
        }
    tasks, gaps = [], []
    for name in request["disciplines"]:
        selection = config["disciplines"][name]
        if not selection["enabled"]:
            gaps.append({"discipline": name, "reason": selection["reason"], "status": "unverified",
                         "required_action": "Record an alternative owner and task-specific evidence before claiming coverage"})
            continue
        root = workspace / name
        manifest = capability(root, name)
        tasks.append({
            "discipline": name, "source": source(root, manifest["repository"]),
            "entrypoint": manifest["entrypoint"], "required_reading": manifest["context"],
            "capability_owns": manifest["owns"], "expected_outputs": manifest["outputs"],
            "implementation_repository": config["project"], "status": "planned", "evidence": [],
        })
    return {
        "version": 1, "request": {key: value for key, value in request.items() if key != "version"},
        "project": config["project"], "governance_context": governance,
        "status": "needs-coverage" if gaps else "ready", "tasks": tasks, "coverage_gaps": gaps,
        "authority": "Planning only; no execution, approval, merge, publication or deployment is granted",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True,
                        help="directory containing the selected capability Git checkouts")
    args = parser.parse_args(argv)
    try:
        result = plan(read_json(args.config), read_json(args.request), args.workspace)
    except ValueError as error:
        print(f"Cannot plan: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
