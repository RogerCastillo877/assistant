"""
OSEF Runtime

state.py

Workflow execution state.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WorkflowState:

    workflow_id: str

    current_step: int = 0

    completed_steps: list[str] = field(
        default_factory=list
    )

    failed: bool = False

    completed: bool = False

    def mark_step_completed(
        self,
        step_id: str,
    ) -> None:

        self.completed_steps.append(
            step_id
        )

        self.current_step += 1

    def mark_completed(self) -> None:

        self.completed = True

    def mark_failed(self) -> None:

        self.failed = True
