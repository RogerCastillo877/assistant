"""
OSEF Runtime

test_dashboard.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_dashboard():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="learning",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        },
    )

    dashboard = (
        engine.dashboard.build()
    )

    assert (
        dashboard.missions
        >= 1
    )

    assert (
        dashboard.agents
        >= 1
    )

    assert (
        dashboard.workflows
        >= 1
    )

    assert (
        dashboard.memories
        >= 1
    )

    assert (
        dashboard.knowledge
        >= 1
    )

    assert (
        dashboard.traces
        >= 1
    )

    assert (
        dashboard.artifacts
        >= 1
    )

    assert (
        dashboard.decisions
        >= 1
    )

    assert (
        dashboard.outcomes
        >= 1
    )
