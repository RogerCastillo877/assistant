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
        web_search_service=None,
    ) -> None:

        self.registry = registry
        self.web_search_service = web_search_service

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

        if tool.id == "web-search":

            query = (
                context.inputs.get(
                    "topic",
                    ""
                )
            )

            results = (
                self.web_search_service.search(
                    query
                )
            )

            result = {
                "tool": tool.id,
                "status": "success",
                "results": results,
            }

            context.outputs[
                f"tool:{tool.id}"
            ] = result

            return result
