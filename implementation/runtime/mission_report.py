"""
OSEF Runtime

mission_report.py

Mission execution report.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MissionReport:

    mission_id: str

    memories: int

    knowledge: int

    traces: int

    artifacts: int

    decisions: int

    outcomes: int

    content: str
