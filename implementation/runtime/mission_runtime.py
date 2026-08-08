"""
OSEF Runtime

mission_runtime.py

High-level mission runtime.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.mission_context import (
    MissionContext,
)

from implementation.runtime.mission_executor import (
    MissionExecutor,
)


class MissionRuntime:

    def __init__(
        self,
        registry: RuntimeRegistry,
        mission_executor: MissionExecutor,
    ) -> None:

        self.registry = registry

        self.mission_executor = (
            mission_executor
        )

    def execute(
        self,
        mission_id: str,
        inputs: dict | None = None,
    ) -> MissionContext:

        context = MissionContext(
            mission_id=mission_id,
            inputs=inputs or {},
        )

        self.mission_executor.execute(
            mission_id,
            context,
        )

        return context
