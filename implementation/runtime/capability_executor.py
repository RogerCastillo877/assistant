"""
OSEF Runtime

capability_executor.py

Capability execution layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.context import (
    ExecutionContext,
)

from implementation.runtime.skill_executor import (
    SkillExecutor,
)


class CapabilityExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
        skill_executor: SkillExecutor,
    ) -> None:

        self.registry = registry
        self.skill_executor = skill_executor

    def execute(
        self,
        capability_id: str,
        context: ExecutionContext,
    ) -> None:

        capability = self.registry.get_capability(
            capability_id
        )

        if capability is None:
            raise ValueError(
                f"Capability '{capability_id}' not found."
            )

        print(
            f"Executing capability: "
            f"{capability.name}"
        )

        for skill_id in capability.skills:

            self.skill_executor.execute(
                skill_id,
                context,
            )
