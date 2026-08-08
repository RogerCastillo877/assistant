"""
OSEF Runtime

test_mission_history_builder.py
"""

from implementation.runtime.mission_run import (
    MissionRun,
)

from implementation.runtime.mission_run_engine import (
    MissionRunEngine,
)

from implementation.runtime.mission_history_builder import (
    MissionHistoryBuilder,
)


def test_mission_history_builder():

    engine = (
        MissionRunEngine()
    )

    engine.store(
        MissionRun(
            id="run-001",
            mission_id="learning",
            workflow_id=(
                "learning-workflow"
            ),
            status="completed",
        )
    )

    engine.store(
        MissionRun(
            id="run-002",
            mission_id="learning",
            workflow_id=(
                "learning-workflow"
            ),
            status="completed",
        )
    )

    engine.store(
        MissionRun(
            id="run-003",
            mission_id="learning",
            workflow_id=(
                "learning-workflow"
            ),
            status="failed",
        )
    )

    builder = (
        MissionHistoryBuilder(
            engine
        )
    )

    projection = (
        builder.build(
            "learning"
        )
    )

    assert (
        projection.mission_id
        == "learning"
    )

    assert (
        projection.total_runs
        == 3
    )

    assert (
        projection.completed_runs
        == 2
    )

    assert (
        projection.failed_runs
        == 1
    )

    assert (
        len(
            projection.runs
        )
        == 3
    )
