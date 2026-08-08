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
        registry=engine.registry,
        events=engine.events,
        policy_engine=engine.policy_engine,
        capability_executor=engine.capability_executor,
        memory_engine=engine.memory_engine,
        lifecycle=engine.lifecycle,
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
