#!/usr/bin/env python3
"""A0 read-only contextual routing and reported-result contract.

This module does not call an LLM, run project commands, edit files, grant
permissions, or verify the truth of reported external observations.
An authorised coding host supplies the context and executes actual work.
"""

import argparse
import json
from pathlib import Path
import re
import sys

from constellation import plan, read_json, source, nonempty, object_keys, text_list, version_one

SIGNALS = (
    "implementation", "architecture", "interface", "security",
    "independent_workstreams", "shared_interfaces", "consequential",
)
EXECUTION = ("not_started", "running", "partial", "blocked", "completed")
VERIFICATION = ("not_run", "partial", "failed", "passed")
APPROVAL = ("not_requested", "pending", "approved", "rejected")


def local_project_file(root, name):
    nonempty(name, "project context path")
    if Path(name).is_absolute():
        raise ValueError("Project context must be relative to the product checkout")
    root = root.resolve()
    candidate = (root / name).resolve()
    if not candidate.is_relative_to(root) or not candidate.is_file():
        raise ValueError("Project context missing or outside product checkout")
    return name


def intake_record(data, product_root):
    """Validate explicit, inspectable signals; no natural-language inference."""
    object_keys(data, (
        "version", "id", "objective", "context", "acceptance_criteria",
        "signals", "host",
    ), "A0 intake")
    version_one(data["version"], "A0 intake")
    nonempty(data["id"], "intake.id")
    nonempty(data["objective"], "intake.objective")
    for key in ("context", "acceptance_criteria"):
        text_list(data[key], key)
    for path in data["context"]:
        local_project_file(product_root, path)
    object_keys(data["signals"], SIGNALS, "intake.signals")
    for k, v in data["signals"].items():
        if type(v) is not bool:
            raise ValueError("Signal " + k + " must be a boolean")
    object_keys(data["host"], ("name", "subagents", "isolated_worktrees"), "intake.host")
    if data["host"]["name"] != "codex":
        raise ValueError("A0 supports the codex host contract only; other hosts need review")
    if type(data["host"]["subagents"]) is not bool or type(data["host"]["isolated_worktrees"]) is not bool:
        raise ValueError("Host capabilities must be explicit booleans")
    if data["host"]["isolated_worktrees"] and not data["host"]["subagents"]:
        raise ValueError("Isolated parallel subagents cannot be available without subagents")
    if data["signals"]["independent_workstreams"] and data["signals"]["shared_interfaces"]:
        raise ValueError("Workstreams marked independent cannot simultaneously share mutable interfaces")
    return data


def route_request(config, intake, workspace, product_root):
    """Return deterministic recommendation plus current v1 composition plan."""
    product_root = product_root.resolve()
    if not product_root.is_dir():
        raise ValueError("Adopting product checkout is missing")
    intake = intake_record(intake, product_root)
    if not isinstance(config.get("project"), str):
        raise ValueError("Project configuration is missing an owner/repo name")
    project = config["project"]
    if product_root.name != project.split("/")[-1]:
        raise ValueError("Product checkout name does not match configuration")
    current = source(product_root, project)
    signals = intake["signals"]
    chosen = []
    if signals["implementation"] or signals["architecture"]:
        chosen.append("axis")
    if signals["interface"]:
        chosen.append("meridian")
    if signals["security"]:
        chosen.append("sentinel")

    # Source relevance is separate from selecting extra executing AI agents.
    host = intake["host"]
    mode = "unified"
    explanation = "One coding agent applies selected disciplines; least orchestration overhead"
    if len(chosen) > 1 and host["subagents"]:
        if (signals["independent_workstreams"] and host["isolated_worktrees"]
                and not signals["shared_interfaces"]):
            mode = "parallel"
            explanation = "Independent tasks and isolated worktrees are reported available"
        elif signals["shared_interfaces"]:
            mode = "coordinated"
            explanation = "Interdependent contracts benefit from reviewed sequential handoffs"
    elif len(chosen) > 1:
        explanation = "Unified fallback: separate native subagents were not declared available"

    req = {
        "version": 1, "id": intake["id"], "objective": intake["objective"],
        "context": intake["context"], "acceptance_criteria": intake["acceptance_criteria"],
        "disciplines": chosen,
    }
    composition = plan(config, req, workspace)
    return {
        "version": 1, "routing": {
            "disciplines": chosen, "mode": mode, "reason": explanation,
            "human_approval_required_for_consequential_action": signals["consequential"],
            "host_capabilities_are_reported_not_attested": True,
        },
        "product_source": current,
        "preflight_status": composition["status"],
        "composition": composition,
        "authority": "Read-only recommendation; execution, approval, review and release not granted",
    }


def validate_result(data):
    """Validate reported evidence shape without claiming independent assurance."""
    object_keys(data, (
        "version", "request_id", "project", "source_revision", "execution",
        "verification", "approval", "checks", "artifacts",
        "documentation", "coverage_gaps", "unresolved_findings",
    ), "A0 result")
    version_one(data["version"], "A0 result")
    for key in ("request_id", "project"):
        nonempty(data[key], key)
    if not isinstance(data["source_revision"], str) or not re.fullmatch(r"[0-9a-f]{40}", data["source_revision"]):
        raise ValueError("source_revision must be an immutable 40-digit Git SHA")
    for key, options in (("execution", EXECUTION), ("verification", VERIFICATION), ("approval", APPROVAL)):
        if data[key] not in options:
            raise ValueError("Invalid " + key + " state")
    for key in ("checks", "artifacts", "documentation", "coverage_gaps", "unresolved_findings"):
        if not isinstance(data[key], list):
            raise ValueError(key + " must be a list")
    for check in data["checks"]:
        object_keys(check, ("command", "exit_code", "source_revision", "evidence_ref"), "check")
        nonempty(check["command"], "check.command")
        nonempty(check["evidence_ref"], "check.evidence_ref")
        if type(check["exit_code"]) is not int:
            raise ValueError("Check must record a real integer exit status")
        if check["source_revision"] != data["source_revision"]:
            raise ValueError("Stale check revision")
    for key in ("artifacts", "documentation", "coverage_gaps"):
        for value in data[key]:
            nonempty(value, key)
    for finding in data["unresolved_findings"]:
        object_keys(finding, ("severity", "description"), "finding")
        if finding["severity"] not in ("critical", "high", "medium", "low", "info"):
            raise ValueError("Invalid finding severity")
        nonempty(finding["description"], "finding.description")

    if data["verification"] == "passed":
        if data["execution"] != "completed":
            raise ValueError("Verification cannot pass unfinished execution")
        if not data["checks"] or any(check["exit_code"] != 0 for check in data["checks"]):
            raise ValueError("Passing verification needs reported successful actual checks")
        if data["coverage_gaps"]:
            raise ValueError("Unverified coverage prevents a passing result")
        if any(x["severity"] in ("critical", "high") for x in data["unresolved_findings"]):
            raise ValueError("Unresolved critical/high risk prevents a passing result")
    if data["execution"] in ("not_started", "running", "blocked") and data["verification"] == "passed":
        raise ValueError("Work cannot be verified before completion")
    return {"status": "schema-valid", "assurance": "self-reported, not independently observed",
            "request_id": data["request_id"], "execution": data["execution"],
            "verification": data["verification"], "approval": data["approval"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    route = sub.add_parser("route", help="Read-only routing from explicitly inspected host context")
    route.add_argument("--config", type=Path, required=True)
    route.add_argument("--intake", type=Path, required=True)
    route.add_argument("--workspace", type=Path, required=True)
    route.add_argument("--product-root", type=Path, required=True)
    result = sub.add_parser("check-result", help="Validate self-reported result shape, not external truth")
    result.add_argument("--result", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "route":
            data = route_request(read_json(args.config), read_json(args.intake),
                                 args.workspace, args.product_root)
        else:
            data = validate_result(read_json(args.result))
    except (ValueError, OSError) as error:
        print("A0 validation failed: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
