"""
OSEF Runtime

mission_run.py

Mission execution record.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class MissionRun:

    id: str

    mission_id: str

    workflow_id: str

    status: str

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
