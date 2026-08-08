"""
OSEF Runtime

decision_engine.py

Decision management.
"""

from __future__ import annotations

from implementation.runtime.decision_record import (
    DecisionRecord,
)


class DecisionEngine:

    def __init__(self) -> None:

        self._records: dict[
            str,
            DecisionRecord,
        ] = {}

    def record(
        self,
        decision: DecisionRecord,
    ) -> None:

        self._records[
            decision.id
        ] = decision

    def get(
        self,
        decision_id: str,
    ) -> DecisionRecord | None:

        return self._records.get(
            decision_id
        )

    def all(
        self,
    ) -> list[DecisionRecord]:

        return list(
            self._records.values()
        )

    def count(self) -> int:

        return len(
            self._records
        )

    def clear(self) -> None:

        self._records.clear()
