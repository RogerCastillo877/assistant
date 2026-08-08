"""
OSEF Runtime

knowledge_document.py

Human-readable knowledge document.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class KnowledgeDocument:

    mission_id: str

    title: str

    content: str
