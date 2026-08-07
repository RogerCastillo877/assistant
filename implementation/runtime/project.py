"""
OSEF Runtime

project.py

Canonical in-memory representation of an OSEF project.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from implementation.runtime.model import (
    Agent,
    Capability,
    Knowledge,
    Memory,
    Mission,
    Policy,
    Resource,
    Skill,
    Tool,
    Workflow,
)


@dataclass(slots=True)
class Project:
    """
    Root aggregate loaded by the OSEF Runtime.
    """

    # ---------------------------------------------------------
    # Raw project manifest
    # ---------------------------------------------------------

    config: dict[str, Any] = field(default_factory=dict)

    # ---------------------------------------------------------
    # Core entities
    # ---------------------------------------------------------

    missions: list[Mission] = field(default_factory=list)

    policies: list[Policy] = field(default_factory=list)

    agents: list[Agent] = field(default_factory=list)

    workflows: list[Workflow] = field(default_factory=list)

    capabilities: list[Capability] = field(default_factory=list)

    skills: list[Skill] = field(default_factory=list)

    tools: list[Tool] = field(default_factory=list)

    resources: list[Resource] = field(default_factory=list)

    memory: list[Memory] = field(default_factory=list)

    knowledge: list[Knowledge] = field(default_factory=list)

    # ---------------------------------------------------------
    # Future runtime entities
    # ---------------------------------------------------------

    documents: list[dict[str, Any]] = field(default_factory=list)

    specifications: list[dict[str, Any]] = field(default_factory=list)

    artifacts: list[dict[str, Any]] = field(default_factory=list)

    decisions: list[dict[str, Any]] = field(default_factory=list)

    releases: list[dict[str, Any]] = field(default_factory=list)

    validations: list[dict[str, Any]] = field(default_factory=list)

    traceability: list[dict[str, Any]] = field(default_factory=list)

    # ---------------------------------------------------------
    # Runtime metadata
    # ---------------------------------------------------------

    root_path: str | None = None

    loaded: bool = False

    runtime_version: str = "0.1.0"

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def entity_count(self) -> int:
        return (
            len(self.missions)
            + len(self.policies)
            + len(self.agents)
            + len(self.workflows)
            + len(self.capabilities)
            + len(self.skills)
            + len(self.tools)
            + len(self.resources)
            + len(self.memory)
            + len(self.knowledge)
        )

    @property
    def is_empty(self) -> bool:
        return self.entity_count == 0
