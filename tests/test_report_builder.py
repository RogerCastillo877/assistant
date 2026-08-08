"""
OSEF Runtime

test_report_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)

from implementation.runtime.report_builder import (
    ReportBuilder,
)


def test_report_builder():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="learning",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        },
    )

    report = ReportBuilder(
        engine.dashboard
    ).build()

    assert (
        report.missions
        >= 1
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
        report.artifacts
        >= 1
    )

    assert (
        report.outcomes
        >= 1
    )

    assert (
        "Runtime Summary"
        in report.content
    )
