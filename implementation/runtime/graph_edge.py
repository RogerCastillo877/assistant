"""
OSEF Runtime

graph_edge.py

Knowledge graph edge.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class GraphEdge:

    source_id: str

    target_id: str

    relationship: str

    metadata: dict = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
