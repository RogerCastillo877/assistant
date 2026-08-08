"""
OSEF Runtime

dashboard.py

Runtime dashboard builder.
"""

from __future__ import annotations

from implementation.runtime.dashboard_projection import (
    DashboardProjection,
)

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
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


class RuntimeDashboard:

    def __init__(
        self,
        registry: RuntimeRegistry,
        memory_engine: MemoryEngine,
        knowledge_engine: KnowledgeEngine,
        traceability_engine: TraceabilityEngine,
        artifact_engine: ArtifactEngine,
        decision_engine: DecisionEngine,
        outcome_engine: OutcomeEngine,
    ) -> None:

        self.registry = registry

        self.memory_engine = memory_engine

        self.knowledge_engine = knowledge_engine

        self.traceability_engine = (
            traceability_engine
        )

        self.artifact_engine = (
            artifact_engine
        )

        self.decision_engine = (
            decision_engine
        )

        self.outcome_engine = (
            outcome_engine
        )

    def build(
        self,
    ) -> DashboardProjection:

        return DashboardProjection(
            missions=len(
                self.registry.missions
            ),
            agents=len(
                self.registry.agents
            ),
            workflows=len(
                self.registry.workflows
            ),
            capabilities=len(
                self.registry.capabilities
            ),
            skills=len(
                self.registry.skills
            ),
            tools=len(
                self.registry.tools
            ),
            memories=self.memory_engine.count(),
            knowledge=self.knowledge_engine.count(),
            traces=self.traceability_engine.count(),
            artifacts=self.artifact_engine.count(),
            decisions=self.decision_engine.count(),
            outcomes=self.outcome_engine.count(),
        )
