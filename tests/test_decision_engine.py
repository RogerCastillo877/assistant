from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.decision_record import (
    DecisionRecord,
)


def test_decision_engine():

    engine = DecisionEngine()

    engine.record(
        DecisionRecord(
            id="dec-001",
            title="Use Search",
            decision="search",
            rationale=(
                "Information is missing."
            ),
            decision_type="runtime",
            source="planner",
        )
    )

    assert (
        engine.count()
        == 1
    )

    decision = engine.get(
        "dec-001"
    )

    assert decision is not None

    assert (
        decision.decision
        == "search"
    )
