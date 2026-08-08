"""
OSEF Runtime

test_marketing_content_mission.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_marketing_content_mission():

    engine = bootstrap()

    context = (
        engine.mission_runtime.execute(
            mission_id="marketing-content",
            inputs={
                "topic":
                "Benefits of strength training"
            },
        )
    )

    assert (
        context.execution_result
        is not None
    )

    projection = (
        engine.mission_projection.build(
            "marketing-content"
        )
    )

    assert (
        len(projection.memories)
        >= 1
    )

    assert (
        len(projection.outcomes)
        >= 1
    )

    report = (
        engine.mission_report_builder.build(
            "marketing-content"
        )
    )

    assert (
        report.outcomes
        >= 1
    )
