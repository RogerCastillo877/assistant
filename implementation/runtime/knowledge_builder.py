"""
OSEF Runtime

knowledge_builder.py

Builds reusable knowledge from memory.
"""

from __future__ import annotations

from implementation.runtime.memory_engine import (
    MemoryEngine,
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
    KnowledgeRecord,
)


class KnowledgeBuilder:

    def __init__(
        self,
        knowledge_engine: KnowledgeEngine,
        memory_engine: MemoryEngine | None = None,
    ) -> None:

        # memory_engine is optional: callers may build from an in-memory
        # MemoryRecord (via `build_from_memory`) or promote by id (via
        # `promote_memory`) when a MemoryEngine is available.
        self.memory_engine = memory_engine

        self.knowledge_engine = knowledge_engine

    def promote_memory(
        self,
        memory_id: str,
        knowledge_type: str = "pattern",
    ) -> KnowledgeRecord:

        if self.memory_engine is None:
            raise ValueError(
                "memory_engine is required for promote_memory"
            )

        memory = self.memory_engine.get(memory_id)

        if memory is None:

            raise ValueError(
                f"Memory '{memory_id}' not found."
            )

        return self.build_from_memory(memory, knowledge_type=knowledge_type)

    def build_from_memory(
        self,
        memory: MemoryRecord,
        knowledge_type: str = "pattern",
        knowledge_engine: KnowledgeEngine | None = None,
    ) -> KnowledgeRecord:

        knowledge = KnowledgeRecord(
            id=f"knowledge-{memory.id}",
            title=memory.title,
            content=memory.content,
            knowledge_type=knowledge_type,
            tags=list(memory.tags),
            source=memory.source,
        )

        engine = knowledge_engine or self.knowledge_engine

        engine.store(knowledge)

        return knowledge
