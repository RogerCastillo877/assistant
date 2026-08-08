"""
OSEF Runtime

query_result.py

Search result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class QueryResult:

    source_type: str

    source_id: str

    title: str

    content: str

    score: float
