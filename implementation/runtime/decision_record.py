"""
OSEF Runtime

decision_record.py

Decision model.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class DecisionRecord:

    id: str

    title: str

    decision: str

    rationale: str

    decision_type: str

    source: str | None = None

    tags: list[str] = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
