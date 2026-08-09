"""
OSEF Runtime

knowledge_catalog.py
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.knowledge_engine import (KnowledgeRecord)


@dataclass(slots=True)
class KnowledgeCatalog:

    total_items: int

    items: list[KnowledgeRecord]

    content: str
