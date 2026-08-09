"""
OSEF Runtime

knowledge_search.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class KnowledgeSearchResult:

    source_type: str

    source_id: str

    title: str

    content: str

    score: float
