"""
OSEF Runtime

test_mission_run_engine.py
"""

from implementation.runtime.mission_run import (
    MissionRun,
)

from implementation.runtime.mission_run_engine import (
    MissionRunEngine,
)


def test_mission_run_engine():

    engine = MissionRunEngine()

    engine.store(
        MissionRun(
            id="run-001",
            mission_id="learning",
            workflow_id="learning-workflow",
            status="completed",
        )
    )

    assert (
        engine.count()
        == 1
    )

    assert (
        len(
            engine.by_mission(
                "learning"
            )
        )
        == 1
    )
