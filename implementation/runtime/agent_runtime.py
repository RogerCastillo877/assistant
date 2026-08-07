"""
OSEF Runtime

agent_runtime.py

High-level agent runtime.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.agent_context import (
    AgentContext,
)

from implementation.runtime.agent_executor import (
    AgentExecutor,
)


class AgentRuntime:

    def __init__(
        self,
        registry: RuntimeRegistry,
        agent_executor: AgentExecutor,
    ) -> None:

        self.registry = registry

        self.agent_executor = (
            agent_executor
        )

    def execute(
        self,
        agent_id: str,
        mission_id: str | None = None,
        inputs: dict | None = None,
    ) -> AgentContext:

        context = AgentContext(
            agent_id=agent_id,
            mission_id=mission_id,
            inputs=inputs or {},
        )

        self.agent_executor.execute(
            agent_id,
            context,
        )

        return context
