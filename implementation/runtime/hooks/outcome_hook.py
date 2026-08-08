"""
OSEF Runtime

outcome_hook.py

Creates outcomes from workflow completion.
"""

from __future__ import annotations

from implementation.runtime.outcome_record import (
    OutcomeRecord,
)

from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)


class OutcomeHook:

    def __init__(
        self,
        outcome_engine: OutcomeEngine,
    ) -> None:

        self.outcome_engine = (
            outcome_engine
        )

    def execute(
        self,
        payload: dict,
    ) -> None:

        workflow_id = payload.get(
            "workflow_id"
        )

        if workflow_id is None:
            return

        outcome = OutcomeRecord(
            id=f"outcome-{workflow_id}",
            title=f"Workflow {workflow_id}",
            description=(
                "Workflow completed successfully"
            ),
            outcome_type="workflow",
            status="completed",
            source="outcome-hook",
        )

        self.outcome_engine.store(
            outcome
        )

        print(
            "[HOOK] outcome.created"
        )
