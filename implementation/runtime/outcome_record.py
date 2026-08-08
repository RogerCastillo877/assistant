"""
OSEF Runtime

outcome_record.py

Outcome model.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class OutcomeRecord:

    id: str

    title: str

    description: str

    outcome_type: str

    status: str = "completed"

    source: str | None = None

    tags: list[str] = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
