"""
OSEF Runtime

test_mission_report_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)

from implementation.runtime.mission_report_builder import (
    MissionReportBuilder,
)


def test_mission_report_builder():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="learning",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        },
    )

    report = (
        MissionReportBuilder(
            engine.mission_projection
        ).build(
            "learning"
        )
    )

    assert (
        report.mission_id
        == "learning"
    )

    assert (
        report.memories
        >= 1
    )

    assert (
        report.knowledge
        >= 1
    )

    assert (
        report.traces
        >= 1
    )

    assert (
        report.artifacts
        >= 1
    )

    assert (
        report.decisions
        >= 1
    )

    assert (
        report.outcomes
        >= 1
    )

    assert (
        "Mission Report"
        in report.content
    )
