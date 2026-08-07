"""
OSEF Runtime

executor.py

Workflow execution engine.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.registry import RuntimeRegistry
from implementation.runtime.errors import RuntimeError
from implementation.runtime.context import (
    ExecutionContext,
)
from implementation.runtime.state import (
    WorkflowState,
)

@dataclass(slots=True)
class ExecutionResult:

    workflow_id: str

    completed_steps: int

    success: bool


class WorkflowExecutor:

    def __init__(
        self,
        registry: RuntimeRegistry,
    ) -> None:

        self.registry = registry

    def execute(
        self,
        workflow_id: str,
        context: ExecutionContext | None = None,
    ) -> ExecutionResult:

        workflow = self.registry.get_workflow(
            workflow_id
        )

        if workflow is None:

            context = ExecutionContext(
                workflow_id=workflow_id
            )

            raise RuntimeError(
                f"Workflow '{workflow_id}' not found."
            )

        if context.state is None:

            context.state = WorkflowState(
                workflow_id=workflow.id
            )

        completed = 0

        total = len(workflow.steps)

        print(
            f"Executing workflow: "
            f"{workflow.name}"
        )

        print(
            f"Inputs: "
            f"{context.inputs}"
        )

        for index, step in enumerate(
            workflow.steps,
            start=1,
        ):

            context.state.mark_step_completed(
                step["id"]
            )

            name = step.get(
                "name",
                step.get("id", "unknown"),
            )

            print(
                f"[{index}/{total}] {name}"
            )

            completed += 1

            context.state.mark_completed()

        return ExecutionResult(
            workflow_id=workflow.id,
            completed_steps=completed,
            success=True,
        )
