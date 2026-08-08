from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)

from implementation.runtime.hooks.outcome_hook import (
    OutcomeHook,
)


def test_outcome_hook():

    outcome_engine = (
        OutcomeEngine()
    )

    hook = OutcomeHook(
        outcome_engine
    )

    hook.execute(
        {
            "workflow_id":
            "learning-workflow"
        }
    )

    assert (
        outcome_engine.count()
        == 1
    )

    outcome = (
        outcome_engine.all()[0]
    )

    assert (
        outcome.id
        == "outcome-learning-workflow"
    )

    assert (
        outcome.status
        == "completed"
    )
