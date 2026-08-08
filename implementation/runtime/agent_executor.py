"""
OSEF Runtime

agent_executor.py

Agent execution layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.executor import (
    WorkflowExecutor,
)

from implementation.runtime.agent_context import (
    AgentContext,
)


class AgentExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
        workflow_executor: WorkflowExecutor,
    ) -> None:

        self.registry = registry

        self.workflow_executor = (
            workflow_executor
        )

    def execute(
        self,
        agent_id: str,
        context: AgentContext,
    ) -> None:

        agent = self.registry.get_agent(
            agent_id
        )

        if agent is None:

            raise ValueError(
                f"Agent '{agent_id}' not found."
            )

        print(
            f"Executing agent: "
            f"{agent.name}"
        )

        for workflow_id in agent.workflows:

            workflow_context = (
                self.workflow_executor
                .execute_with_context(
                    workflow_id=workflow_id,
                    inputs=context.inputs,
                )
            )

            context.execution_context = (
                workflow_context
            )

        return None
