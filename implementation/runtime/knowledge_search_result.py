"""
OSEF Runtime

knowledge_search_result.py
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from implementation.runtime.knowledge_engine import (
    KnowledgeRecord,
)


@dataclass(slots=True)
class KnowledgeSearchResult:

    query: str

    results: list[KnowledgeRecord] = field(
        default_factory=list
    )

    total_results: int = 0

    def add(
        self,
        record: KnowledgeRecord,
    ) -> None:

        self.results.append(
            record
        )

        self.total_results = len(
            self.results
        )

    @property
    def empty(
        self,
    ) -> bool:

        return (
            self.total_results == 0
        )

    def top(
        self,
        limit: int = 5,
    ) -> list[KnowledgeRecord]:

        return self.results[
            :limit
        ]
