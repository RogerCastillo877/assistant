"""
OSEF Runtime

decision_hook.py
"""

from __future__ import annotations

from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.decision_record import (
    DecisionRecord,
)


class DecisionHook:

    def __init__(
        self,
        decision_engine: DecisionEngine,
    ) -> None:

        self.decision_engine = (
            decision_engine
        )

    def execute(
        self,
        payload: dict,
    ) -> None:

        workflow_id = payload[
            "workflow_id"
        ]

        decision = DecisionRecord(
            id=f"decision-{workflow_id}",
            title=f"Workflow {workflow_id}",
            decision="approved",
            rationale=(
                "Workflow completed successfully"
            ),
            decision_type="execution",
            source="decision-hook",
        )

        self.decision_engine.record(
            decision
        )
