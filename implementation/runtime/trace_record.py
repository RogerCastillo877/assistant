"""
OSEF Runtime

trace_record.py

Traceability record.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class TraceRecord:

    source_id: str

    target_id: str

    relationship: str

    metadata: dict = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
