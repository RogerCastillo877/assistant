"""
OSEF Runtime

artifact_hook.py
"""

from __future__ import annotations

from implementation.runtime.artifact_engine import (
    ArtifactEngine,
)

from implementation.runtime.artifact_record import (
    ArtifactRecord,
)


class ArtifactHook:

    def __init__(
        self,
        artifact_engine: ArtifactEngine,
    ) -> None:

        self.artifact_engine = (
            artifact_engine
        )

    def execute(
        self,
        payload: dict,
    ) -> None:

        workflow_id = payload[
            "workflow_id"
        ]

        artifact = ArtifactRecord(
            id=f"artifact-{workflow_id}",
            title=f"Workflow {workflow_id} Report",
            content=(
                "Workflow completed successfully"
            ),
            artifact_type="report",
            source="artifact-hook",
            tags=[
                "workflow",
                workflow_id,
            ],
        )

        self.artifact_engine.store(
            artifact
        )
