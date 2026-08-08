"""
OSEF Runtime

test_mission_projection.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_mission_projection():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="learning",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        },
    )

    projection = (
        engine.mission_projection.build(
            "learning"
        )
    )

    assert (
        projection.mission.id
        ==
        "learning"
    )

    assert (
        len(
            projection.memories
        )
        >= 1
    )

    assert (
        len(
            projection.knowledge
        )
        >= 1
    )

    assert (
        len(
            projection.outcomes
        )
        >= 1
    )
