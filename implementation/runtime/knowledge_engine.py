"""
OSEF Runtime

knowledge_engine.py

Knowledge management layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class KnowledgeRecord:

    id: str

    title: str

    content: str

    knowledge_type: str

    tags: list[str] = field(
        default_factory=list
    )

    source: str | None = None

    confidence: float = 1.0

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


class KnowledgeEngine:

    def __init__(self) -> None:

        self._records: dict[
            str,
            KnowledgeRecord,
        ] = {}

    def store(
        self,
        record: KnowledgeRecord,
    ) -> None:

        self._records[
            record.id
        ] = record

    def get(
        self,
        record_id: str,
    ) -> KnowledgeRecord | None:

        return self._records.get(
            record_id
        )

    def all(
        self,
    ) -> list[KnowledgeRecord]:

        return list(
            self._records.values()
        )

    def search_by_tag(
        self,
        tag: str,
    ) -> list[KnowledgeRecord]:

        return [
            record
            for record in self._records.values()
            if tag in record.tags
        ]

    def search_by_type(
        self,
        knowledge_type: str,
    ) -> list[KnowledgeRecord]:

        return [
            record
            for record in self._records.values()
            if record.knowledge_type
            == knowledge_type
        ]

    def count(self) -> int:

        return len(
            self._records
        )

    def clear(self) -> None:

        self._records.clear()
