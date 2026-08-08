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

from implementation.runtime.events import (
    EventStore,
)

from implementation.runtime.capability_executor import (
    CapabilityExecutor,
)

from implementation.runtime.policy_engine import (
    PolicyEngine,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
)

from implementation.runtime.runtime_lifecycle import (
    RuntimeLifecycle,
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
        events: EventStore,
        policy_engine: PolicyEngine,
        capability_executor: CapabilityExecutor,
        memory_engine: MemoryEngine,
        lifecycle: RuntimeLifecycle,
    ) -> None:

        self.registry = registry
        self.events = events
        self.policy_engine = policy_engine
        self.capability_executor = capability_executor
        self.memory_engine = memory_engine
        self.lifecycle = lifecycle
    def execute(
        self,
        workflow_id: str,
        context: ExecutionContext | None = None,
    ) -> ExecutionResult:

        workflow = self.registry.get_workflow(
            workflow_id
        )

        if workflow is None:

            raise RuntimeError(
                f"Workflow '{workflow_id}' not found."
            )

        if context is None:

            context = ExecutionContext(
                workflow_id=workflow.id,
                memory=self.memory_engine,
            )

        if context.memory is None:

            context.memory = self.memory_engine

        self.policy_engine.enforce_workflow(
            workflow,
            context,
        )

        if context.state is None:

            context.state = WorkflowState(
                workflow_id=workflow.id
            )

        self.events.emit(
            "workflow.started",
            {
                "workflow_id": workflow.id,
            },
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

            step_id = step["id"]

            capability_id = step.get(
                "capability"
            )

            self.events.emit(
                "workflow.step.started",
                {
                    "workflow_id": workflow.id,
                    "step_id": step_id,
                },
            )

            name = step.get(
                "name",
                step_id,
            )

            print(
                f"[{index}/{total}] {name}"
            )

            if capability_id:

                self.capability_executor.execute(
                    capability_id,
                    context,
                )

            context.state.mark_step_completed(
                step_id
            )

            completed += 1

            self.events.emit(
                "workflow.step.completed",
                {
                    "workflow_id": workflow.id,
                    "step_id": step_id,
                },
            )

        context.state.mark_completed()

        self.events.emit(
            "workflow.completed",
            {
                "workflow_id": workflow.id,
                "completed_steps": completed,
            },
        )

        self.lifecycle.emit(
            "workflow.completed",
            {
                "workflow_id": workflow.id,
                "completed_steps": completed,
                "context": context,
            },
        )

        return ExecutionResult(
            workflow_id=workflow.id,
            completed_steps=completed,
            success=True,
        )

    def execute_with_context(
        self,
        workflow_id: str,
        mission_id: str | None = None,
        inputs: dict | None = None,
    ) -> ExecutionContext:

        context = ExecutionContext(
            workflow_id=workflow_id,
            mission_id=mission_id,
            inputs=inputs or {},
            memory=self.memory_engine,
        )

        self.execute(
            workflow_id=workflow_id,
            context=context,
        )

        return context
