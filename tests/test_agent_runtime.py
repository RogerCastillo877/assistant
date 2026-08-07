from implementation.runtime.engine import (
    bootstrap,
)


def test_agent_runtime():

    engine = bootstrap()

    context = (
        engine.agent_runtime.execute(
            agent_id="planner",
            mission_id="learning",
            inputs={
                "learning-goal":
                "Learn Kubernetes"
            },
        )
    )

    assert (
        context.agent_id
        == "planner"
    )

    assert (
        context.execution_context
        is not None
    )

    assert (
        context.execution_context.state.completed
        is True
    )
