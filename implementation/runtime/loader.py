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
        priority=data.get("priority"),
        owner=data.get("owner"),
        domain=data.get("domain"),
        workflows=data.get("workflows", []),
        policies=data.get("policies", []),
        requirements=data.get("requirements", []),
        success_criteria=data.get("success_criteria", []),
        metrics=data.get("metrics", {}),
        knowledge_outputs=data.get("knowledge_outputs", []),
        memory=data.get("memory", True),
        human_approval=data.get("human_approval", False),
        tags=data.get("tags", []),
        agents=data.get("agents", []),
    )


def _build_agent(data: dict) -> Agent:

    return Agent(
        id=data["id"],
        name=data["name"],
        version=data["version"],
        status=data["status"],
        type=data.get("type", "assistant"),
        description=data.get("description"),
        mission=data.get("mission"),
        policies=data.get("policies", []),
        workflows=data.get("workflows", []),
        capabilities=data.get("capabilities", []),
        memory=data.get("memory", True),
        knowledge=data.get("knowledge", True),
        human_approval=data.get("human_approval", False),
        runtime=data.get("runtime"),
        tags=data.get("tags", []),
    )


def _build_workflow(data: dict) -> Workflow:

    return Workflow(
        id=data["id"],
        name=data["name"],
        purpose=data["purpose"],
        version=data["version"],
        status=data["status"],
        description=data.get("description"),
        mission=data.get("mission"),
        policies=data.get("policies", []),
        agent=data.get("agent"),
        inputs=data.get("inputs", []),
        outputs=data.get("outputs", []),
        triggers=data.get("triggers", []),
        steps=data.get("steps", []),
        metrics=data.get("metrics", []),
        tags=data.get("tags", []),
    )


def _build_capability(data: dict) -> Capability:

    return Capability(
        id=data["id"],
        name=data["name"],
        description=data["description"],
        purpose=data["purpose"],
        version=data["version"],
        status=data["status"],
        owner=data["owner"],
        inputs=data.get("inputs", []),
        outputs=data.get("outputs", []),
        preconditions=data.get("preconditions", []),
        postconditions=data.get("postconditions", []),
        policies=data.get("policies", []),
        required_tools=data.get("required_tools", []),
        required_resources=data.get("required_resources", []),
        skills=data.get("skills", []),
        metrics=data.get("metrics", []),
        tags=data.get("tags", []),
    )


def _build_skill(data: dict) -> Skill:

    return Skill(
        id=data["id"],
        name=data["name"],
        description=data["description"],
        purpose=data["purpose"],
        owner=data["owner"],
        status=data["status"],
        inputs=data.get("inputs", []),
        outputs=data.get("outputs", []),
        tools=data.get("tools", []),
        resources=data.get("resources", []),
        memory=data.get("memory", []),
        policies=data.get("policies", []),
        constraints=data.get("constraints", []),
        preconditions=data.get("preconditions", []),
        postconditions=data.get("postconditions", []),
        metrics=data.get("metrics", []),
        tags=data.get("tags", []),
    )


def _build_tool(data: dict) -> Tool:

    return Tool(
        id=data["id"],
        name=data["name"],
        description=data.get("description", ""),
        type=data["type"],
        owner=data["owner"],
        version=data["version"],
        status=data["status"],
        endpoint=data.get("endpoint"),
        authentication=data.get("authentication"),
        inputs=data.get("inputs", []),
        outputs=data.get("outputs", []),
    )


def _build_resource(data: dict) -> Resource:

    return Resource(
        id=data["id"],
        name=data["name"],
        description=data.get("description", ""),
        type=data["type"],
        owner=data["owner"],
        classification=data["classification"],
        lifecycle=data["lifecycle"],
        version=data["version"],
        location=data.get("location"),
        provider=data.get("provider"),
        format=data.get("format"),
        access=data.get("access", {}),
        dependencies=data.get("dependencies", []),
        used_by=data.get("used_by", []),
        tags=data.get("tags", []),
    )


def _build_memory(data: dict) -> Memory:

    return Memory(
        id=data["id"],
        name=data["name"],
        type=data["type"],
        scope=data["scope"],
        retention=data["retention"],
        purpose=data.get("purpose"),
        description=data.get("description"),
        owner=data.get("owner"),
        storage=data.get("storage"),
        encryption=data.get("encryption", False),
        classification=data.get("classification"),
        policies=data.get("policies", []),
        sources=data.get("sources", []),
        consumers=data.get("consumers", []),
    )


def _build_knowledge(data: dict) -> Knowledge:

    return Knowledge(
        id=data["id"],
        name=data["name"],
        description=data["description"],
        category=data["category"],
        status=data["status"],
        source=data["source"],
        owner=data["owner"],
        version=data["version"],
        tags=data.get("tags", []),
        references=data.get("references", []),
        related_capabilities=data.get("related_capabilities", []),
        related_skills=data.get("related_skills", []),
        related_workflows=data.get("related_workflows", []),
        validation=data.get("validation", {}),
    )


# ============================================================
# Loader
# ============================================================


def load_project() -> Project:

    root = get_project_root()

    project = Project()

    project.root_path = str(root)

    config_file = (
        root
        / "specification"
        / "300-runtime"
        / "config"
        / "osef.yaml"
    )

    if config_file.exists():
        project.config = load_yaml(config_file)

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
                _build_mission(payload.get("mission", payload))
            )

        elif parent == "agents":
            project.agents.append(
                _build_agent(payload.get("agent", payload))
            )

        elif parent == "workflows":
            project.workflows.append(
                _build_workflow(payload.get("workflow", payload))
            )

        elif parent == "capabilities":
            project.capabilities.append(
                _build_capability(payload.get("capability", payload))
            )

        elif parent == "skills":
            project.skills.append(
                _build_skill(payload.get("skill", payload))
            )

        elif parent == "tools":
            project.tools.append(
                _build_tool(payload.get("tool", payload))
            )

        elif parent == "resources":
            project.resources.append(
                _build_resource(payload.get("resource", payload))
            )

        elif parent == "memory":
            project.memory.append(
                _build_memory(payload.get("memory", payload))
            )

        elif parent == "knowledge":
            project.knowledge.append(
                _build_knowledge(payload.get("knowledge", payload))
            )

    project.loaded = True

    return project
