"""
OSEF Runtime

artifact_record.py

Artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime


@dataclass(slots=True)
class ArtifactRecord:

    id: str

    title: str

    content: str

    artifact_type: str

    tags: list[str] = field(
        default_factory=list
    )

    source: str | None = None

    version: str = "1.0.0"

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
