"""
OSEF Runtime

mission_report_builder.py

Builds mission reports from mission projections.
"""

from __future__ import annotations

from implementation.runtime.mission_projection_engine import (
    MissionProjectionEngine,
)

from implementation.runtime.mission_report import (
    MissionReport,
)


class MissionReportBuilder:

    def __init__(
        self,
        mission_projection: MissionProjectionEngine,
    ) -> None:

        self.mission_projection = (
            mission_projection
        )

    def build(
        self,
        mission_id: str,
    ) -> MissionReport:

        projection = (
            self.mission_projection.build(
                mission_id
            )
        )

        memories = len(
            projection.memories
        )

        knowledge = len(
            projection.knowledge
        )

        traces = len(
            projection.traces
        )

        artifacts = len(
            projection.artifacts
        )

        decisions = len(
            projection.decisions
        )

        outcomes = len(
            projection.outcomes
        )

        content = "\n".join(
            [
                (
                    f"Mission Report: "
                    f"{projection.mission.name}"
                ),
                "",
                "## Knowledge",
                "",
                f"Memories: {memories}",
                f"Knowledge: {knowledge}",
                f"Traces: {traces}",
                "",
                "## Execution",
                "",
                f"Artifacts: {artifacts}",
                f"Decisions: {decisions}",
                f"Outcomes: {outcomes}",
            ]
        )

        return MissionReport(
            mission_id=mission_id,
            memories=memories,
            knowledge=knowledge,
            traces=traces,
            artifacts=artifacts,
            decisions=decisions,
            outcomes=outcomes,
            content=content,
        )
