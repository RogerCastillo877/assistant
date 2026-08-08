from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.hooks.decision_hook import (
    DecisionHook,
)


def test_decision_hook():

    engine = DecisionEngine()

    hook = DecisionHook(
        decision_engine=engine,
    )

    hook.execute(
        {
            "workflow_id":
            "learning-workflow"
        }
    )

    assert engine.count() == 1

    decision = engine.all()[0]

    assert (
        decision.id
        ==
        "decision-learning-workflow"
    )

    assert (
        decision.decision
        ==
        "approved"
    )
