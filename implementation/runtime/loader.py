"""
OSEF Runtime

loader.py

Loads an OSEF project into memory using a minimal viable metamodel.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from implementation.runtime.common import (
    find_yaml_files,
    get_project_root,
    load_yaml,
)


@dataclass
class ProjectModel:

    config: dict[str, Any] = field(default_factory=dict)

    missions: list[dict[str, Any]] = field(default_factory=list)

    policies: list[dict[str, Any]] = field(default_factory=list)

    agents: list[dict[str, Any]] = field(default_factory=list)

    workflows: list[dict[str, Any]] = field(default_factory=list)

    capabilities: list[dict[str, Any]] = field(default_factory=list)

    skills: list[dict[str, Any]] = field(default_factory=list)

    tools: list[dict[str, Any]] = field(default_factory=list)

    resources: list[dict[str, Any]] = field(default_factory=list)

    memory: list[dict[str, Any]] = field(default_factory=list)

    knowledge: list[dict[str, Any]] = field(default_factory=list)

    documents: list[dict[str, Any]] = field(default_factory=list)

    releases: list[dict[str, Any]] = field(default_factory=list)

    decisions: list[dict[str, Any]] = field(default_factory=list)

    traceability: list[dict[str, Any]] = field(default_factory=list)


def _add_collection(target: list[dict[str, Any]], payload: dict[str, Any]) -> None:
    if isinstance(payload, dict):
        target.append(payload)


def load_project() -> ProjectModel:
    """
    Load the core OSEF entities from the repository's runtime examples.

    This implementation intentionally supports only the initial, minimal
    metamodel required for the first runtime iteration.
    """

    project = ProjectModel()
    root = get_project_root()

    manifest_path = root / "specification" / "300-runtime" / "config" / "osef.yaml"
    if manifest_path.exists():
        project.config = load_yaml(manifest_path)

    example_root = root / "specification" / "300-runtime" / "examples"
    if not example_root.exists():
        return project

    collection_map = {
        "missions": project.missions,
        "policies": project.policies,
        "agents": project.agents,
        "workflows": project.workflows,
        "capabilities": project.capabilities,
        "skills": project.skills,
        "tools": project.tools,
        "resources": project.resources,
        "memory": project.memory,
        "knowledge": project.knowledge,
    }

    for path in find_yaml_files(example_root):
        payload = load_yaml(path)
        if not isinstance(payload, dict):
            continue

        parent_name = path.parent.name
        if parent_name in collection_map:
            _add_collection(collection_map[parent_name], payload)
            continue

        if isinstance(payload.get("kind"), str):
            kind = payload["kind"].lower()
            if kind in collection_map:
                _add_collection(collection_map[kind], payload)

    return project
