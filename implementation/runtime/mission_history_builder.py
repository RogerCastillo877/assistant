"""
OSEF Runtime

mission_history_builder.py
"""

from __future__ import annotations

from implementation.runtime.mission_history_projection import (
    MissionHistoryProjection,
)

from implementation.runtime.mission_run_engine import (
    MissionRunEngine,
)


class MissionHistoryBuilder:

    def __init__(
        self,
        mission_run_engine: MissionRunEngine,
    ) -> None:

        self.mission_run_engine = (
            mission_run_engine
        )

    def build(
        self,
        mission_id: str,
    ) -> MissionHistoryProjection:

        runs = (
            self.mission_run_engine
            .by_mission(
                mission_id
            )
        )

        completed_runs = len(
            [
                run
                for run in runs
                if run.status
                == "completed"
            ]
        )

        failed_runs = len(
            [
                run
                for run in runs
                if run.status
                == "failed"
            ]
        )

        return (
            MissionHistoryProjection(
                mission_id=mission_id,
                runs=runs,
                total_runs=len(
                    runs
                ),
                completed_runs=(
                    completed_runs
                ),
                failed_runs=(
                    failed_runs
                ),
            )
        )
