"""
OSEF Runtime

tool_executor.py

Tool execution layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)

from implementation.runtime.context import (
    ExecutionContext,
)


class ToolExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
    ) -> None:

        self.registry = registry

    def execute(
        self,
        tool_id: str,
        context: ExecutionContext,
    ) -> dict:

        tool = self.registry.get_tool(
            tool_id
        )

        if tool is None:
            raise ValueError(
                f"Tool '{tool_id}' not found."
            )

        print(
            f"Executing tool: "
            f"{tool.name}"
        )

        result = {
            "tool": tool.id,
            "status": "success",
            "results": [],
        }

        context.outputs[
            f"tool:{tool.id}"
        ] = result

        return result
