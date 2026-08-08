"""
OSEF Runtime

engine.py

Runtime bootstrap and initialization.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.hooks.knowledge_pipeline_hook import KnowledgePipelineHook
from implementation.runtime.knowledge_engine import KnowledgeEngine
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

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.artifact_engine import (
    ArtifactEngine,
)

from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)

from implementation.runtime.knowledge_builder import (
    KnowledgeBuilder,
)

from implementation.runtime.traceability_service import (
    TraceabilityService,
)

from implementation.runtime.knowledge_pipeline import (
    KnowledgePipeline,
)

from implementation.runtime.runtime_lifecycle import (
    RuntimeLifecycle,
)

from implementation.runtime.hooks.outcome_hook import (
    OutcomeHook,
)

from implementation.runtime.hooks.decision_hook import (
    DecisionHook,
)

from implementation.runtime.hooks.artifact_hook import (
    ArtifactHook,
)

from implementation.runtime.projection_engine import (
    ProjectionEngine,
)

from implementation.runtime.mission_executor import (
    MissionExecutor,
)

from implementation.runtime.mission_runtime import (
    MissionRuntime,
)

from implementation.runtime.mission_projection_engine import (
    MissionProjectionEngine,
)

from implementation.runtime.query_engine import (
    QueryEngine,
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

    artifact_engine: ArtifactEngine

    knowledge: KnowledgeEngine

    decision_engine: DecisionEngine

    memory_engine: MemoryEngine

    projection: ProjectionEngine

    knowledge_builder: KnowledgeBuilder

    traceability: TraceabilityEngine

    traceability_service: TraceabilityService

    skill_executor: SkillExecutor

    capability_executor: CapabilityExecutor

    mission_executor: MissionExecutor

    mission_runtime: MissionRuntime

    mission_projection: MissionProjectionEngine

    policy_engine: PolicyEngine

    outcome_engine: OutcomeEngine

    query: QueryEngine

    executor: WorkflowExecutor

    agent_executor: AgentExecutor

    agent_runtime: AgentRuntime

    knowledge_pipeline: KnowledgePipeline

    lifecycle: RuntimeLifecycle

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

    lifecycle = RuntimeLifecycle()

    #
    # Core Engines
    #

    memory = MemoryEngine()

    knowledge = KnowledgeEngine()

    traceability = TraceabilityEngine()

    artifact_engine = ArtifactEngine()

    decision_engine = DecisionEngine()

    outcome_engine = OutcomeEngine()

    artifact_engine = ArtifactEngine()

    #
    # Builders / Services
    #

    knowledge_builder = KnowledgeBuilder(
        memory_engine=memory,
        knowledge_engine=knowledge,
    )

    traceability_service = TraceabilityService(
        traceability_engine=traceability,
    )

    knowledge_pipeline = KnowledgePipeline(
        knowledge_builder=knowledge_builder,
        traceability_service=traceability_service,
    )

    #
    # Lifecycle Hooks
    #

    hook = KnowledgePipelineHook(
        knowledge_pipeline
    )

    lifecycle.register(
        "workflow.completed",
        hook,
    )

    outcome_hook = OutcomeHook(
        outcome_engine
    )

    lifecycle.register(
        "workflow.completed",
        outcome_hook,
    )

    decision_hook = DecisionHook(
        decision_engine=decision_engine,
    )

    lifecycle.register(
        "workflow.completed",
        decision_hook,
    )

    artifact_hook = ArtifactHook(
        artifact_engine=artifact_engine,
    )

    lifecycle.register(
        "workflow.completed",
        artifact_hook,
    )

    #
    # Runtime Executors
    #

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

    projection = ProjectionEngine(
        memory_engine=memory,
        knowledge_engine=knowledge,
        traceability_engine=traceability,
        artifact_engine=artifact_engine,
        decision_engine=decision_engine,
        outcome_engine=outcome_engine,
    )

    mission_projection = (
        MissionProjectionEngine(
            registry=registry,
            memory_engine=memory,
            knowledge_engine=knowledge,
            traceability_engine=traceability,
            artifact_engine=artifact_engine,
            decision_engine=decision_engine,
            outcome_engine=outcome_engine,
        )
    )

    query = QueryEngine(
        memory_engine=memory,
        knowledge_engine=knowledge,
        traceability_engine=traceability,
        artifact_engine=artifact_engine,
        decision_engine=decision_engine,
        outcome_engine=outcome_engine,
    )

    executor = WorkflowExecutor(
        registry=registry,
        events=events,
        capability_executor=capability_executor,
        policy_engine=policy_engine,
        memory_engine=memory,
        lifecycle=lifecycle,
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

    mission_executor = MissionExecutor(
    registry=registry,
    agent_runtime=agent_runtime,
    )

    mission_runtime = MissionRuntime(
        registry=registry,
        mission_executor=mission_executor,
    )

    #
    # Validation
    #

    if validate:

        report = resolver.validate()

        if not report.valid:

            raise ResolutionError(
                "\n".join(report.errors)
            )

    #
    # Runtime Container
    #

    return RuntimeEngine(
        project=project,
        registry=registry,
        resolver=resolver,
        events=events,
        tool_executor=tool_executor,
        artifact_engine=artifact_engine,
        knowledge=knowledge,
        decision_engine=decision_engine,
        memory_engine=memory,
        projection=projection,
        knowledge_builder=knowledge_builder,
        traceability=traceability,
        traceability_service=traceability_service,
        skill_executor=skill_executor,
        capability_executor=capability_executor,
        policy_engine=policy_engine,
        outcome_engine=outcome_engine,
        executor=executor,
        agent_executor=agent_executor,
        agent_runtime=agent_runtime,
        knowledge_pipeline=knowledge_pipeline,
        lifecycle=lifecycle,
        mission_executor=mission_executor,
        mission_runtime=mission_runtime,
        mission_projection=mission_projection,
        query=query,
    )
