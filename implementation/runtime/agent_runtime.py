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

from implementation.runtime.memory_engine import (
    MemoryEngine,
    MemoryRecord,
)


class AgentRuntime:

    def __init__(
        self,
        registry: RuntimeRegistry,
        agent_executor: AgentExecutor,
        memory_engine: MemoryEngine,
    ) -> None:

        self.registry = registry

        self.agent_executor = (
            agent_executor
        )

        self.memory_engine = (
            memory_engine
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

        agent = self.registry.get_agent(
            agent_id
        )
        self.memory_engine.store(
            MemoryRecord(
                id=f"memory-{agent.id}",
                title=f"Execution of {agent.name}",
                content="Agent executed successfully",
                memory_type="execution",
                tags=[
                    "agent",
                    agent.id
                ],
                source="agent-runtime",
            )
        )

        return context
