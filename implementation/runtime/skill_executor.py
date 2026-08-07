"""
OSEF Runtime

skill_executor.py

Skill execution layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.context import (
    ExecutionContext,
)

from implementation.runtime.tool_executor import (
    ToolExecutor,
)


class SkillExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
        tool_executor: ToolExecutor,
    ) -> None:

        self.registry = registry
        self.tool_executor = tool_executor

    def execute(
        self,
        skill_id: str,
        context: ExecutionContext,
    ) -> None:

        skill = self.registry.get_skill(
            skill_id
        )

        if skill is None:
            raise ValueError(
                f"Skill '{skill_id}' not found."
            )

        print(
            f"Executing skill: "
            f"{skill.name}"
        )

        for tool_id in skill.tools:

            self.tool_executor.execute(
                tool_id,
                context,
            )
