"""
OSEF Runtime

knowledge_pipeline.py

Transforms memories into knowledge assets.
"""

from __future__ import annotations
from implementation.runtime.knowledge_engine import KnowledgeEngine

from implementation.runtime.memory_engine import (
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeRecord,
)

from implementation.runtime.knowledge_builder import (
    KnowledgeBuilder,
)

from implementation.runtime.traceability_service import (
    TraceabilityService,
)


class KnowledgePipeline:

    def __init__(
        self,
        knowledge_builder: KnowledgeBuilder,
        traceability_service: TraceabilityService,
    ) -> None:

        self.knowledge_builder = (
            knowledge_builder
        )

        self.traceability_service = (
            traceability_service
        )

    def process(
        self,
        memory: MemoryRecord,
        knowledge_engine: KnowledgeEngine | None = None,
    ) -> KnowledgeRecord:

        knowledge = self.knowledge_builder.build_from_memory(
            memory,
            knowledge_engine=knowledge_engine,
        )

        self.traceability_service.track_memory_knowledge(
            memory_id=memory.id,
            knowledge_id=knowledge.id,
        )

        return knowledge
