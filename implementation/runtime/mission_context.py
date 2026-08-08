"""
OSEF Runtime

mission_context.py

Mission execution context.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from typing import Any


@dataclass(slots=True)
class MissionContext:

    mission_id: str

    inputs: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    execution_result: Any | None = None
