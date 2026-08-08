"""
OSEF Runtime

mission_run_hook.py
"""

from __future__ import annotations

from uuid import uuid4

from implementation.runtime.mission_run import (
    MissionRun,
)

from implementation.runtime.mission_run_engine import (
    MissionRunEngine,
)


class MissionRunHook:

    def __init__(
        self,
        mission_run_engine: MissionRunEngine,
    ) -> None:

        self.mission_run_engine = (
            mission_run_engine
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

        context = payload.get("context")

        if context is None:
            return

        mission_id = context.mission_id

        if mission_id is None:
            return

        self.mission_run_engine.store(
            MissionRun(
                id=str(uuid4()),
                mission_id=mission_id,
                workflow_id=workflow_id,
                status="completed",
            )
        )
