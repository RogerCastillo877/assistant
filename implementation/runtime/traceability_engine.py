"""
OSEF Runtime

traceability_engine.py

Runtime traceability management.
"""

from __future__ import annotations

from implementation.runtime.trace_record import (
    TraceRecord,
)


class TraceabilityEngine:

    def __init__(self) -> None:

        self._records: list[
            TraceRecord
        ] = []

    def link(
        self,
        source_id: str,
        target_id: str,
        relationship: str,
        metadata: dict | None = None,
    ) -> TraceRecord:

        record = TraceRecord(
            source_id=source_id,
            target_id=target_id,
            relationship=relationship,
            metadata=metadata or {},
        )

        self._records.append(
            record
        )

        return record

    def all(
        self,
    ) -> list[TraceRecord]:

        return list(
            self._records
        )

    def count(self) -> int:

        return len(
            self._records
        )

    def clear(self) -> None:

        self._records.clear()

    def by_source(
        self,
        source_id: str,
    ) -> list[TraceRecord]:

        return [
            record
            for record in self._records
            if record.source_id
            == source_id
        ]

    def by_target(
        self,
        target_id: str,
    ) -> list[TraceRecord]:

        return [
            record
            for record in self._records
            if record.target_id
            == target_id
        ]

    def descendants(
        self,
        source_id: str,
    ) -> list[str]:

        return [
            record.target_id
            for record in self._records
            if record.source_id
            == source_id
        ]
