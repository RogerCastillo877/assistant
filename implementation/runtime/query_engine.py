"""
OSEF Runtime

query_engine.py

Unified query layer.
"""

from __future__ import annotations

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


class QueryEngine:

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

    # -------------------------
    # Memory
    # -------------------------

    def memories(
        self,
        tag: str | None = None,
    ) -> list:

        records = (
            self.memory_engine.all()
        )

        if tag is None:
            return records

        return [
            record
            for record in records
            if tag in record.tags
        ]

    # -------------------------
    # Knowledge
    # -------------------------

    def knowledge(
        self,
        knowledge_type: str | None = None,
    ) -> list:

        records = (
            self.knowledge_engine.all()
        )

        if knowledge_type is None:
            return records

        return [
            record
            for record in records
            if (
                record.knowledge_type
                == knowledge_type
            )
        ]

    # -------------------------
    # Artifacts
    # -------------------------

    def artifacts(
        self,
        artifact_type: str | None = None,
    ) -> list:

        records = (
            self.artifact_engine.all()
        )

        if artifact_type is None:
            return records

        return [
            record
            for record in records
            if (
                record.artifact_type
                == artifact_type
            )
        ]

    # -------------------------
    # Decisions
    # -------------------------

    def decisions(
        self,
        decision_type: str | None = None,
    ) -> list:

        records = (
            self.decision_engine.all()
        )

        if decision_type is None:
            return records

        return [
            record
            for record in records
            if (
                record.decision_type
                == decision_type
            )
        ]

    # -------------------------
    # Outcomes
    # -------------------------

    def outcomes(
        self,
        status: str | None = None,
    ) -> list:

        records = (
            self.outcome_engine.all()
        )

        if status is None:
            return records

        return [
            record
            for record in records
            if record.status == status
        ]

    # -------------------------
    # Traceability
    # -------------------------

    def descendants(
        self,
        source_id: str,
    ) -> list[str]:

        return (
            self.traceability_engine
            .descendants(source_id)
        )
