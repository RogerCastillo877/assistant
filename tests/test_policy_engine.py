from implementation.runtime.engine import (
    bootstrap,
)


def test_policy_validation():

    engine = bootstrap()

    workflow = engine.registry.get_workflow(
        "learning-workflow"
    )

    result = engine.policy_engine.enforce_workflow(
        workflow,
        None,
    )

    assert result is True
