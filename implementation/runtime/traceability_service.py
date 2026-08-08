"""
OSEF Runtime

traceability_service.py

High-level traceability automation.
"""

from __future__ import annotations

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.trace_record import (
    TraceRecord,
)


class TraceabilityService:

    def __init__(
        self,
        traceability_engine: TraceabilityEngine,
    ) -> None:

        self.traceability_engine = (
            traceability_engine
        )

    def track_workflow_memory(
        self,
        workflow_id: str,
        memory_id: str,
    ) -> TraceRecord:

        return self.traceability_engine.link(
            source_id=workflow_id,
            target_id=memory_id,
            relationship="generated",
        )

    def track_memory_knowledge(
        self,
        memory_id: str,
        knowledge_id: str,
    ) -> TraceRecord:

        return self.traceability_engine.link(
            source_id=memory_id,
            target_id=knowledge_id,
            relationship="promoted_to",
        )

    def track_agent_outcome(
        self,
        agent_id: str,
        outcome_id: str,
    ) -> TraceRecord:

        return self.traceability_engine.link(
            source_id=agent_id,
            target_id=outcome_id,
            relationship="generated",
        )

    def track_decision_artifact(
        self,
        decision_id: str,
        artifact_id: str,
    ) -> TraceRecord:

        return self.traceability_engine.link(
            source_id=decision_id,
            target_id=artifact_id,
            relationship="generated",
        )
