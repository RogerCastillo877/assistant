"""
OSEF Runtime

projection_engine.py

Runtime projection builder.
"""

from __future__ import annotations

from implementation.runtime.runtime_projection import (
    RuntimeProjection,
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


class ProjectionEngine:

    def __init__(
        self,
        memory_engine: MemoryEngine,
        knowledge_engine: KnowledgeEngine,
        traceability_engine: TraceabilityEngine,
        artifact_engine: ArtifactEngine,
        decision_engine: DecisionEngine,
        outcome_engine: OutcomeEngine,
    ) -> None:

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
        workflow_id: str,
    ) -> RuntimeProjection:

        return RuntimeProjection(
            workflow_id=workflow_id,
            memories=self.memory_engine.all(),
            knowledge=self.knowledge_engine.all(),
            traces=self.traceability_engine.all(),
            artifacts=self.artifact_engine.all(),
            decisions=self.decision_engine.all(),
            outcomes=self.outcome_engine.all(),
        )
