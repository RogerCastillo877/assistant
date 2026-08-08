"""
OSEF Runtime

context.py

Execution context passed through the runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from implementation.runtime.state import (
    WorkflowState,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
)

@dataclass(slots=True)
class ExecutionContext:

    mission_id: str | None = None

    workflow_id: str | None = None

    state: WorkflowState | None = None

    memory: MemoryEngine | None = None

    inputs: dict[str, Any] = field(
        default_factory=dict
    )

    outputs: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def set_output(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.outputs[key] = value

    def get_input(
        self,
        key: str,
        default: Any = None,
    ) -> Any:

        return self.inputs.get(key, default)
