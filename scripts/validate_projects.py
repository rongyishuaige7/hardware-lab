#!/usr/bin/env python3
"""Validate the Hardware Lab index against live public GitHub facts."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_FILE = ROOT / "projects.yml"
README_FILE = ROOT / "README.md"
EXPECTED_PROJECT_COUNT = 9
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REPO_RE = re.compile(r"^https://github\.com/([^/]+)/([^/]+)$")
RUN_RE = re.compile(
    r"^https://github\.com/([^/]+)/([^/]+)/actions/runs/([0-9]+)$"
)
ALLOWED_RETEST = {"not_retested", "historical_evidence_only", "reverified"}
REQUIRED_KEYS = {
    "name",
    "repo",
    "default_branch",
    "head_sha",
    "platform",
    "summary",
    "build",
    "hardware_retest",
    "media_scope",
    "known_boundaries",
}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def get_json(url: str) -> dict[str, Any]:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "rongyi-hardware-lab-validator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        fail(f"{url} returned HTTP {error.code}")
    except urllib.error.URLError as error:
        fail(f"{url} could not be reached: {error.reason}")


def require_nonempty_string(project: dict[str, Any], key: str, name: str) -> str:
    value = project.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{name}: {key} must be a non-empty string")
    return value


def validate_local(data: dict[str, Any]) -> list[dict[str, Any]]:
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(data.get("status_date", ""))):
        fail("status_date must use YYYY-MM-DD")

    projects = data.get("projects")
    if not isinstance(projects, list) or not projects:
        fail("projects must be a non-empty array")
    if len(projects) != EXPECTED_PROJECT_COUNT:
        fail(
            f"projects must contain the {EXPECTED_PROJECT_COUNT} currently "
            "published Hardware Lab entries"
        )

    repos: set[str] = set()
    for index, project in enumerate(projects, start=1):
        if not isinstance(project, dict):
            fail(f"project #{index} must be an object")
        missing = REQUIRED_KEYS - project.keys()
        if missing:
            fail(f"project #{index} is missing: {', '.join(sorted(missing))}")

        name = require_nonempty_string(project, "name", f"project #{index}")
        if not re.search(r"[\u4e00-\u9fff]", name):
            fail(f"{name}: Hardware Lab project names must contain Chinese text")
        repo = require_nonempty_string(project, "repo", name).rstrip("/")
        project["repo"] = repo
        if not REPO_RE.fullmatch(repo):
            fail(f"{name}: repo must be a canonical GitHub repository URL")
        if repo in repos:
            fail(f"{name}: duplicate repository URL")
        repos.add(repo)

        branch = require_nonempty_string(project, "default_branch", name)
        if branch != "main":
            fail(f"{name}: this first index requires default_branch=main")
        if not SHA_RE.fullmatch(str(project.get("head_sha", ""))):
            fail(f"{name}: head_sha must be a full lowercase Git SHA")

        for key in ("platform", "summary", "media_scope"):
            require_nonempty_string(project, key, name)

        build = project.get("build")
        if not isinstance(build, dict) or build.get("status") != "passed":
            fail(f"{name}: build.status must be passed")
        if not SHA_RE.fullmatch(str(build.get("head_sha", ""))):
            fail(f"{name}: build.head_sha must be a full lowercase Git SHA")
        if build["head_sha"] != project["head_sha"]:
            fail(f"{name}: build evidence must match the indexed default-branch HEAD")
        if not RUN_RE.fullmatch(str(build.get("run_url", ""))):
            fail(f"{name}: build.run_url must be a fixed GitHub Actions run URL")
        if build.get("artifact_retention_days") != 14:
            fail(f"{name}: artifact retention must stay explicit at 14 days")

        retest = project.get("hardware_retest")
        if not isinstance(retest, dict) or retest.get("status") not in ALLOWED_RETEST:
            fail(f"{name}: invalid hardware_retest.status")
        require_nonempty_string(retest, "note", f"{name} hardware_retest")
        if retest["status"] == "not_retested" and retest.get("date") is not None:
            fail(f"{name}: not_retested must not have a date")
        if retest["status"] != "not_retested" and not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", str(retest.get("date", ""))
        ):
            fail(f"{name}: dated evidence must use YYYY-MM-DD")

        boundaries = project.get("known_boundaries")
        if not isinstance(boundaries, list) or not boundaries:
            fail(f"{name}: known_boundaries must be a non-empty array")
        if not all(isinstance(item, str) and item.strip() for item in boundaries):
            fail(f"{name}: known_boundaries entries must be non-empty strings")

    return projects


def validate_live(projects: list[dict[str, Any]]) -> None:
    for project in projects:
        name = project["name"]
        repo_match = REPO_RE.fullmatch(project["repo"])
        assert repo_match
        owner, repo = repo_match.groups()
        api_base = f"https://api.github.com/repos/{owner}/{repo}"

        metadata = get_json(api_base)
        if metadata.get("private") is not False:
            fail(f"{name}: indexed repository is not public")
        if metadata.get("default_branch") != project["default_branch"]:
            fail(f"{name}: default branch drifted")

        commit = get_json(f"{api_base}/commits/{project['default_branch']}")
        if commit.get("sha") != project["head_sha"]:
            fail(f"{name}: indexed HEAD drifted from the live default branch")

        run_match = RUN_RE.fullmatch(project["build"]["run_url"])
        assert run_match
        run_owner, run_repo, run_id = run_match.groups()
        if (run_owner, run_repo) != (owner, repo):
            fail(f"{name}: workflow run belongs to a different repository")
        run = get_json(
            f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}"
        )
        if run.get("status") != "completed" or run.get("conclusion") != "success":
            fail(f"{name}: workflow run is not a completed success")
        if run.get("head_sha") != project["head_sha"]:
            fail(f"{name}: workflow run does not match the indexed HEAD")
        print(f"PASS {name}: {project['head_sha'][:12]} · Actions {run_id}")


def validate_readme(projects: list[dict[str, Any]]) -> None:
    readme = README_FILE.read_text(encoding="utf-8")
    if "SYSTEM ONLINE" in readme.upper():
        fail("README must not claim SYSTEM ONLINE")
    if f"当前收录 {len(projects)} 个公开项目" not in readme:
        fail("README project count is not synchronized with projects.yml")
    for project in projects:
        heading = f"### [{project['name']}]({project['repo']})"
        if heading not in readme:
            fail(f"README must use the indexed Chinese project name: {project['name']}")
        for value in (
            project["repo"],
            project["build"]["run_url"],
            project["head_sha"][:12],
        ):
            if value not in readme:
                fail(f"README is not synchronized with {project['name']}: {value}")


def main() -> None:
    try:
        data = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot parse projects.yml as JSON-compatible YAML: {error}")
    projects = validate_local(data)
    validate_readme(projects)
    validate_live(projects)
    print(f"Hardware Lab validation: PASS ({len(projects)} projects)")


if __name__ == "__main__":
    main()
