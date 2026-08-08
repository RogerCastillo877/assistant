"""
OSEF Runtime

test_mission_runtime.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_mission_runtime():

    engine = bootstrap()

    context = (
        engine.mission_runtime.execute(
            mission_id="learning",
            inputs={
                "learning-goal":
                "Learn Kubernetes"
            },
        )
    )

    assert (
        context.mission_id
        ==
        "learning"
    )

    assert (
        context.execution_result
        is not None
    )
