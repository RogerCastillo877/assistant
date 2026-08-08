"""
OSEF Runtime

runtime_report.py

Human-readable runtime report.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeReport:

    title: str

    missions: int

    agents: int

    workflows: int

    memories: int

    knowledge: int

    traces: int

    artifacts: int

    decisions: int

    outcomes: int

    content: str
