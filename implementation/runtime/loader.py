"""
OSEF Runtime

loader.py

Loads OSEF YAML artifacts and converts them into
typed runtime objects.
"""

from __future__ import annotations

from pathlib import Path

from implementation.runtime.common import (
    find_yaml_files,
    get_project_root,
    load_yaml,
)

from implementation.runtime.model import (
    Mission,
    Agent,
    Workflow,
    Capability,
    Skill,
    Tool,
    Resource,
    Memory,
    Knowledge,
)

from implementation.runtime.project import Project


# ============================================================
# Entity Builders
# ============================================================


def _build_mission(data: dict) -> Mission:

    return Mission(
        id=data["id"],
        name=data["name"],
        purpose=data["purpose"],
        version=data["version"],
        status=data["status"],
        description=data.get("description"),
        workflows=data.get("workflows", []),
        policies=data.get("policies", []),
        tags=data.get("tags", []),
    )


def _build_agent(data: dict) -> Agent:

    return Agent(
        id=data["id"],
        name=data["name"],
        version=data["version"],
        status=data["status"],
        mission=data.get("mission"),
        workflows=data.get("workflows", []),
        capabilities=data.get("capabilities", []),
        tags=data.get("tags", []),
    )


def _build_workflow(data: dict) -> Workflow:

    return Workflow(
        id=data["id"],
        name=data["name"],
        purpose=data["purpose"],
        version=data["version"],
        status=data["status"],
        mission=data.get("mission"),
        steps=data.get("steps", []),
    )


def _build_capability(data: dict) -> Capability:

    cap = data["capability"]

    return Capability(
        id=cap["id"],
        name=cap["name"],
        purpose=cap["purpose"],
        version=cap["version"],
        status=cap["status"],
        skills=cap.get("skills", []),
    )


def _build_skill(data: dict) -> Skill:

    skill = data["skill"]

    return Skill(
        id=skill["id"],
        name=skill["name"],
        purpose=skill["purpose"],
        owner=skill["owner"],
        status=skill["status"],
        tools=skill.get("tools", []),
        resources=skill.get("resources", []),
    )


def _build_tool(data: dict) -> Tool:

    tool = data["tool"]

    return Tool(
        id=tool["id"],
        name=tool["name"],
        type=tool["type"],
        version=tool["version"],
        status=tool["status"],
    )


def _build_resource(data: dict) -> Resource:

    resource = data["resource"]

    return Resource(
        id=resource["id"],
        name=resource["name"],
        type=resource["type"],
        lifecycle=resource["lifecycle"],
        version=resource["version"],
    )


def _build_memory(data: dict) -> Memory:

    memory = data["memory"]

    return Memory(
        id=memory["id"],
        name=memory["name"],
        type=memory["type"],
        scope=memory["scope"],
        retention=memory["retention"],
    )


def _build_knowledge(data: dict) -> Knowledge:

    knowledge = data["knowledge"]

    return Knowledge(
        id=knowledge["id"],
        name=knowledge["name"],
        category=knowledge["category"],
        version=knowledge["version"],
        status=knowledge["status"],
    )


# ============================================================
# Loader
# ============================================================


def load_project() -> Project:

    root = get_project_root()

    project = Project()

    examples_root = (
        root
        / "specification"
        / "300-runtime"
        / "examples"
    )

    if not examples_root.exists():
        return project

    for path in find_yaml_files(examples_root):

        payload = load_yaml(path)

        if not isinstance(payload, dict):
            continue

        parent = path.parent.name

        if parent == "missions":
            project.missions.append(
                _build_mission(payload)
            )

        elif parent == "agents":
            project.agents.append(
                _build_agent(payload)
            )

        elif parent == "workflows":
            project.workflows.append(
                _build_workflow(payload)
            )

        elif parent == "capabilities":
            project.capabilities.append(
                _build_capability(payload)
            )

        elif parent == "skills":
            project.skills.append(
                _build_skill(payload)
            )

        elif parent == "tools":
            project.tools.append(
                _build_tool(payload)
            )

        elif parent == "resources":
            project.resources.append(
                _build_resource(payload)
            )

        elif parent == "memory":
            project.memory.append(
                _build_memory(payload)
            )

        elif parent == "knowledge":
            project.knowledge.append(
                _build_knowledge(payload)
            )

    return project
