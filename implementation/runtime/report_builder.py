"""
OSEF Runtime

report_builder.py

Builds runtime reports.
"""

from __future__ import annotations

from implementation.runtime.dashboard import (
    RuntimeDashboard,
)

from implementation.runtime.runtime_report import (
    RuntimeReport,
)


class ReportBuilder:

    def __init__(
        self,
        dashboard: RuntimeDashboard,
    ) -> None:

        self.dashboard = dashboard

    def build(
        self,
        title: str = "OSEF Runtime Report",
    ) -> RuntimeReport:

        projection = (
            self.dashboard.build()
        )

        content = "\n".join(
            [
                f"Report: {title}",
                "",
                "Runtime Summary",
                "---------------",
                f"Missions: {projection.missions}",
                f"Agents: {projection.agents}",
                f"Workflows: {projection.workflows}",
                "",
                "Knowledge Summary",
                "-----------------",
                f"Memories: {projection.memories}",
                f"Knowledge: {projection.knowledge}",
                f"Traces: {projection.traces}",
                "",
                "Execution Summary",
                "-----------------",
                f"Artifacts: {projection.artifacts}",
                f"Decisions: {projection.decisions}",
                f"Outcomes: {projection.outcomes}",
            ]
        )

        return RuntimeReport(
            title=title,
            missions=projection.missions,
            agents=projection.agents,
            workflows=projection.workflows,
            memories=projection.memories,
            knowledge=projection.knowledge,
            traces=projection.traces,
            artifacts=projection.artifacts,
            decisions=projection.decisions,
            outcomes=projection.outcomes,
            content=content,
        )
