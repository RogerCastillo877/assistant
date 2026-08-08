"""
OSEF Runtime

search_service.py

Unified runtime search service.
"""

from __future__ import annotations

from implementation.runtime.query_engine import (
    QueryEngine,
)

from implementation.runtime.query_result import (
    QueryResult,
)


class SearchService:

    def __init__(
        self,
        query_engine: QueryEngine,
    ) -> None:

        self.query_engine = (
            query_engine
        )

    def search(
        self,
        query: str,
    ) -> list[QueryResult]:

        query_lower = (
            query.lower()
        )

        results: list[
            QueryResult
        ] = []

        #
        # Memories
        #

        for memory in (
            self.query_engine.memories()
        ):

            searchable = " ".join(
                [
                    memory.title,
                    memory.content,
                ]
            ).lower()

            if (
                query_lower
                not in searchable
            ):
                continue

            results.append(
                QueryResult(
                    source_type="memory",
                    source_id=memory.id,
                    title=memory.title,
                    content=memory.content,
                    score=1.0,
                )
            )

        #
        # Knowledge
        #

        for knowledge in (
            self.query_engine.knowledge()
        ):

            searchable = " ".join(
                [
                    knowledge.title,
                    knowledge.content,
                ]
            ).lower()

            if (
                query_lower
                not in searchable
            ):
                continue

            results.append(
                QueryResult(
                    source_type="knowledge",
                    source_id=knowledge.id,
                    title=knowledge.title,
                    content=knowledge.content,
                    score=1.0,
                )
            )

        results.sort(
            key=lambda r: r.score,
            reverse=True,
        )

        return results
