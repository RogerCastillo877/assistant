from implementation.runtime.engine import bootstrap

from implementation.runtime.executor import (
    WorkflowExecutor,
)

from implementation.runtime.context import (
    ExecutionContext,
)


def test_workflow_state():

    engine = bootstrap()

    executor = WorkflowExecutor(
        engine.registry,
        engine.events,
        engine.capability_executor,
        engine.policy_engine,
    )

    context = ExecutionContext(
        workflow_id="learning-workflow",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        }
    )

    executor.execute(
        "learning-workflow",
        context,
    )

    state = context.state

    assert state.completed is True

    assert state.failed is False

    assert state.current_step == 4

    assert len(
        state.completed_steps
    ) == 4

    assert state.completed_steps == [
        "planning",
        "search",
        "validate",
        "generate",
    ]
