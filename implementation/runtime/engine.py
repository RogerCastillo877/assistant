"""
OSEF Runtime

engine.py

Runtime bootstrap and initialization.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.loader import load_project
from implementation.runtime.project import Project
from implementation.runtime.registry import RuntimeRegistry
from implementation.runtime.resolver import RuntimeResolver
from implementation.runtime.errors import ResolutionError

from implementation.runtime.events import (
    EventStore,
)

from implementation.runtime.executor import (
    WorkflowExecutor,
)

from implementation.runtime.tool_executor import (
    ToolExecutor,
)

from implementation.runtime.skill_executor import (
    SkillExecutor,
)

from implementation.runtime.capability_executor import (
    CapabilityExecutor,
)

from implementation.runtime.policy_engine import (
    PolicyEngine,
)

from implementation.runtime.agent_executor import (
    AgentExecutor,
)

from implementation.runtime.agent_runtime import (
    AgentRuntime,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
)

@dataclass(slots=True)
class RuntimeEngine:
    """
    Main runtime container.
    """

    project: Project

    registry: RuntimeRegistry

    resolver: RuntimeResolver

    events: EventStore

    tool_executor: ToolExecutor

    memory_engine: MemoryEngine

    skill_executor: SkillExecutor

    capability_executor: CapabilityExecutor

    policy_engine: PolicyEngine

    executor: WorkflowExecutor

    agent_executor: AgentExecutor

    agent_runtime: AgentRuntime

def bootstrap(
    validate: bool = True,
) -> RuntimeEngine:
    """
    Bootstraps the OSEF runtime.
    """

    project = load_project()

    registry = RuntimeRegistry.build(project)

    resolver = RuntimeResolver(registry)

    events = EventStore()

    memory = MemoryEngine()

    tool_executor = ToolExecutor(
        registry=registry,
    )

    skill_executor = SkillExecutor(
        registry=registry,
        tool_executor=tool_executor,
    )

    capability_executor = CapabilityExecutor(
        registry=registry,
        skill_executor=skill_executor,
    )

    policy_engine = PolicyEngine(
        registry=registry,
    )

    executor = WorkflowExecutor(
        registry=registry,
        events=events,
        capability_executor=capability_executor,
        policy_engine=policy_engine,
        memory_engine=memory,
    )

    agent_executor = AgentExecutor(
        registry=registry,
        workflow_executor=executor,
    )

    agent_runtime = AgentRuntime(
        registry=registry,
        agent_executor=agent_executor,
        memory_engine=memory,
    )

    return RuntimeEngine(
        project=project,
        registry=registry,
        resolver=resolver,
        events=events,
        memory_engine=memory,
        tool_executor=tool_executor,
        skill_executor=skill_executor,
        capability_executor=capability_executor,
        policy_engine=policy_engine,
        agent_executor=agent_executor,
        agent_runtime=agent_runtime,
        executor=executor,
    )
