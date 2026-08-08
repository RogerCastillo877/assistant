from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ============================================================
# Mission
# ============================================================

@dataclass(slots=True)
class Mission:

    id: str
    name: str
    purpose: str

    version: str
    status: str

    description: Optional[str] = None

    priority: Optional[str] = None
    owner: Optional[str] = None
    domain: Optional[str] = None

    workflows: list[str] = field(default_factory=list)
    policies: list[str] = field(default_factory=list)

    requirements: list[str] = field(default_factory=list)

    success_criteria: list[str] = field(default_factory=list)

    metrics: dict = field(default_factory=dict)

    knowledge_outputs: list[str] = field(default_factory=list)

    memory: bool = True

    human_approval: bool = False

    tags: list[str] = field(default_factory=list)

    agents: list[str] = field(default_factory=list)


# ============================================================
# Policy
# ============================================================

@dataclass(slots=True)
class Policy:

    id: str
    name: str

    type: str

    version: str
    status: str

    effect: str

    scope: list[str] = field(default_factory=list)

    priority: int = 50

    rules: list[str] = field(default_factory=list)

    conditions: list[str] = field(default_factory=list)

    exceptions: list[str] = field(default_factory=list)

    requires_human_approval: bool = False

    audit: bool = True

    description: Optional[str] = None

    tags: list[str] = field(default_factory=list)


# ============================================================
# Agent
# ============================================================

@dataclass(slots=True)
class Agent:

    id: str
    name: str

    version: str
    status: str

    type: str = "assistant"

    description: Optional[str] = None

    mission: Optional[str] = None

    policies: list[str] = field(default_factory=list)

    workflows: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)

    memory: bool = True

    knowledge: bool = True

    human_approval: bool = False

    runtime: Optional[str] = None

    tags: list[str] = field(default_factory=list)


# ============================================================
# Workflow
# ============================================================

@dataclass(slots=True)
class Workflow:

    id: str
    name: str

    purpose: str

    version: str
    status: str

    description: Optional[str] = None

    mission: Optional[str] = None

    policies: list[str] = field(default_factory=list)

    agent: Optional[str] = None

    inputs: list[str] = field(default_factory=list)

    outputs: list[str] = field(default_factory=list)

    triggers: list[str] = field(default_factory=list)

    steps: list[dict] = field(default_factory=list)

    metrics: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)


# ============================================================
# Capability
# ============================================================

@dataclass(slots=True)
class Capability:

    id: str
    name: str

    description: str

    purpose: str

    version: str
    status: str

    owner: str

    inputs: list[str] = field(default_factory=list)

    outputs: list[str] = field(default_factory=list)

    preconditions: list[str] = field(default_factory=list)

    postconditions: list[str] = field(default_factory=list)

    policies: list[str] = field(default_factory=list)

    required_tools: list[str] = field(default_factory=list)

    required_resources: list[str] = field(default_factory=list)

    skills: list[str] = field(default_factory=list)

    metrics: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)


# ============================================================
# Skill
# ============================================================

@dataclass(slots=True)
class Skill:

    id: str
    name: str

    description: str

    purpose: str

    owner: str

    status: str

    inputs: list[str] = field(default_factory=list)

    outputs: list[str] = field(default_factory=list)

    tools: list[str] = field(default_factory=list)

    resources: list[str] = field(default_factory=list)

    memory: list[str] = field(default_factory=list)

    policies: list[str] = field(default_factory=list)

    constraints: list[str] = field(default_factory=list)

    preconditions: list[str] = field(default_factory=list)

    postconditions: list[str] = field(default_factory=list)

    metrics: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)


# ============================================================
# Tool
# ============================================================

@dataclass(slots=True)
class Tool:

    id: str
    name: str

    description: str

    type: str

    owner: str

    version: str
    status: str

    endpoint: Optional[str] = None

    authentication: Optional[str] = None

    inputs: list[str] = field(default_factory=list)

    outputs: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)

    resources: list[str] = field(default_factory=list)

    policies: list[str] = field(default_factory=list)


# ============================================================
# Resource
# ============================================================

@dataclass(slots=True)
class Resource:

    id: str
    name: str

    description: str

    type: str

    owner: str

    classification: str

    lifecycle: str

    version: str

    location: Optional[str] = None

    provider: Optional[str] = None

    format: Optional[str] = None

    access: dict = field(default_factory=dict)

    dependencies: list[str] = field(default_factory=list)

    used_by: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)


# ============================================================
# Memory
# ============================================================

@dataclass(slots=True)
class Memory:

    id: str
    name: str

    type: str

    scope: str

    retention: str

    purpose: str

    description: Optional[str] = None

    owner: Optional[str] = None

    storage: Optional[str] = None

    encryption: bool = False

    classification: Optional[str] = None

    policies: list[str] = field(default_factory=list)

    sources: list[str] = field(default_factory=list)

    consumers: list[str] = field(default_factory=list)


# ============================================================
# Knowledge
# ============================================================

@dataclass(slots=True)
class Knowledge:

    id: str
    name: str

    description: str

    category: str

    status: str

    source: str

    owner: str

    version: str

    tags: list[str] = field(default_factory=list)

    references: list[str] = field(default_factory=list)

    related_capabilities: list[str] = field(default_factory=list)

    related_skills: list[str] = field(default_factory=list)

    related_workflows: list[str] = field(default_factory=list)

    validation: dict = field(default_factory=dict)
