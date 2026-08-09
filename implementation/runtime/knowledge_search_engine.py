"""
OSEF Runtime

knowledge_search_engine.py
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

from implementation.runtime.knowledge_search import (
    KnowledgeSearchResult,
)


class KnowledgeSearchEngine:

    def __init__(
        self,
        memory_engine: MemoryEngine,
        knowledge_engine: KnowledgeEngine,
        traceability_engine: TraceabilityEngine,
    ) -> None:

        self.memory_engine = (
            memory_engine
        )

        self.knowledge_engine = (
            knowledge_engine
        )

        self.traceability_engine = (
            traceability_engine
        )

    def search(
        self,
        query: str,
    ) -> list[KnowledgeSearchResult]:

        query = query.lower()

        results: list[
            KnowledgeSearchResult
        ] = []

        #
        # Memories
        #

        for memory in (
            self.memory_engine.all()
        ):

            score = 0.0

            if (
                query
                in memory.title.lower()
            ):
                score += 2.0

            if (
                query
                in memory.content.lower()
            ):
                score += 1.0

            if score > 0:

                results.append(
                    KnowledgeSearchResult(
                        source_type="memory",
                        source_id=memory.id,
                        title=memory.title,
                        content=memory.content,
                        score=score,
                    )
                )

        #
        # Knowledge
        #

        for knowledge in (
            self.knowledge_engine.all()
        ):

            score = 0.0

            if (
                query
                in knowledge.title.lower()
            ):
                score += 2.0

            if (
                query
                in knowledge.content.lower()
            ):
                score += 1.0

            if score > 0:

                results.append(
                    KnowledgeSearchResult(
                        source_type="knowledge",
                        source_id=knowledge.id,
                        title=knowledge.title,
                        content=knowledge.content,
                        score=score,
                    )
                )

        results.sort(
            key=lambda result: (
                result.score
            ),
            reverse=True,
        )

        return results
