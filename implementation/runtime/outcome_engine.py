"""
OSEF Runtime

outcome_engine.py

Outcome management.
"""

from __future__ import annotations

from implementation.runtime.outcome_record import (
    OutcomeRecord,
)


class OutcomeEngine:

    def __init__(self) -> None:

        self._records: dict[
            str,
            OutcomeRecord,
        ] = {}

    def store(
        self,
        outcome: OutcomeRecord,
    ) -> None:

        self._records[
            outcome.id
        ] = outcome

    def get(
        self,
        outcome_id: str,
    ) -> OutcomeRecord | None:

        return self._records.get(
            outcome_id
        )

    def all(
        self,
    ) -> list[OutcomeRecord]:

        return list(
            self._records.values()
        )

    def count(self) -> int:

        return len(
            self._records
        )

    def clear(self) -> None:

        self._records.clear()
