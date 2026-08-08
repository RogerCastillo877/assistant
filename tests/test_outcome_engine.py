from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)

from implementation.runtime.outcome_record import (
    OutcomeRecord,
)


def test_outcome_engine():

    engine = OutcomeEngine()

    engine.store(
        OutcomeRecord(
            id="out-001",
            title="Learning Completed",
            description=(
                "Kubernetes learning workflow finished."
            ),
            outcome_type="learning",
            source="planner",
        )
    )

    assert (
        engine.count()
        == 1
    )

    outcome = engine.get(
        "out-001"
    )

    assert outcome is not None

    assert (
        outcome.outcome_type
        == "learning"
    )
