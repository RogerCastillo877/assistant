"""
OSEF Runtime

agent_context.py

Agent execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from implementation.runtime.context import (
    ExecutionContext,
)


@dataclass(slots=True)
class AgentContext:

    agent_id: str

    mission_id: str | None = None

    workflow_id: str | None = None

    inputs: dict[str, Any] = field(
        default_factory=dict
    )

    execution_context: ExecutionContext | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )
