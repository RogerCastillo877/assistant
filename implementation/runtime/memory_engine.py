"""
OSEF Runtime

memory_engine.py

Runtime memory management.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class MemoryRecord:

    id: str

    title: str

    content: str

    memory_type: str

    tags: list[str] = field(
        default_factory=list
    )

    source: str | None = None

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


class MemoryEngine:

    def __init__(self) -> None:

        self._records: dict[
            str,
            MemoryRecord,
        ] = {}

    def store(
        self,
        record: MemoryRecord,
    ) -> None:

        self._records[
            record.id
        ] = record

    def get(
        self,
        record_id: str,
    ) -> MemoryRecord | None:

        return self._records.get(
            record_id
        )

    def all(
        self,
    ) -> list[MemoryRecord]:

        return list(
            self._records.values()
        )

    def search_by_tag(
        self,
        tag: str,
    ) -> list[MemoryRecord]:

        return [
            record
            for record in self._records.values()
            if tag in record.tags
        ]

    def search_by_type(
        self,
        memory_type: str,
    ) -> list[MemoryRecord]:

        return [
            record
            for record in self._records.values()
            if record.memory_type
            == memory_type
        ]

    def count(self) -> int:

        return len(
            self._records
        )

    def clear(self) -> None:

        self._records.clear()
