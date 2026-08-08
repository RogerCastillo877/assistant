"""
OSEF Runtime

dashboard_projection.py

Aggregated runtime dashboard view.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DashboardProjection:

    missions: int

    agents: int

    workflows: int

    capabilities: int

    skills: int

    tools: int

    memories: int

    knowledge: int

    traces: int

    artifacts: int

    decisions: int

    outcomes: int
