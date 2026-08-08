"""
OSEF Runtime

mission_run_engine.py

Stores mission executions.
"""

from __future__ import annotations

from implementation.runtime.mission_run import (
    MissionRun,
)


class MissionRunEngine:

    def __init__(self) -> None:

        self._runs: list[
            MissionRun
        ] = []

    def store(
        self,
        run: MissionRun,
    ) -> None:

        self._runs.append(run)

    def all(
        self,
    ) -> list[MissionRun]:

        return list(
            self._runs
        )

    def by_mission(
        self,
        mission_id: str,
    ) -> list[MissionRun]:

        return [
            run
            for run in self._runs
            if (
                run.mission_id
                == mission_id
            )
        ]

    def count(
        self,
    ) -> int:

        return len(
            self._runs
        )
