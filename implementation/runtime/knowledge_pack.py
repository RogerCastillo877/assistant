"""
OSEF Runtime

knowledge_pack.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class KnowledgePack:

    mission_id: str

    title: str

    memories: list

    knowledge: list

    traces: list

    artifacts: list

    decisions: list

    outcomes: list

    content: str
