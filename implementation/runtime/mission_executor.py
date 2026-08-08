"""
OSEF Runtime

mission_executor.py

Mission execution layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.agent_runtime import (
    AgentRuntime,
)

from implementation.runtime.mission_context import (
    MissionContext,
)


class MissionExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
        agent_runtime: AgentRuntime,
    ) -> None:

        self.registry = registry

        self.agent_runtime = (
            agent_runtime
        )

    def execute(
        self,
        mission_id: str,
        context: MissionContext,
    ) -> None:

        mission = self.registry.get_mission(
            mission_id
        )

        if mission is None:

            raise ValueError(
                f"Mission '{mission_id}' not found."
            )

        print(
            f"Executing mission: "
            f"{mission.name}"
        )

        last_result = None
        print("MISSION AGENTS:", mission.agents)
        for agent_id in mission.agents:
            print(
                "EXECUTING AGENT:",
                agent_id
            )
            last_result = (
                self.agent_runtime.execute(
                    agent_id=agent_id,
                    mission_id=mission.id,
                    inputs=context.inputs,
                )
            )

        context.execution_result = (
            last_result
        )
