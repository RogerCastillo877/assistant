"""
OSEF Runtime

mission_history_projection.py
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.mission_run import (
    MissionRun,
)


@dataclass(slots=True)
class MissionHistoryProjection:

    mission_id: str

    runs: list[MissionRun]

    total_runs: int

    completed_runs: int

    failed_runs: int
