"""
OSEF Runtime

runtime_projection.py

Aggregated runtime projection.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.memory_engine import (
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeRecord,
)

from implementation.runtime.trace_record import (
    TraceRecord,
)

from implementation.runtime.artifact_record import (
    ArtifactRecord,
)

from implementation.runtime.decision_record import (
    DecisionRecord,
)

from implementation.runtime.outcome_record import (
    OutcomeRecord,
)


@dataclass(slots=True)
class RuntimeProjection:

    workflow_id: str

    memories: list[MemoryRecord]

    knowledge: list[KnowledgeRecord]

    traces: list[TraceRecord]

    artifacts: list[ArtifactRecord]

    decisions: list[DecisionRecord]

    outcomes: list[OutcomeRecord]
