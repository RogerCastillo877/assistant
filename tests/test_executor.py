from implementation.runtime.engine import bootstrap

from implementation.runtime.executor import (
    WorkflowExecutor,
)

from implementation.runtime.context import (
    ExecutionContext,
)


def test_execute_learning_workflow():

    engine = bootstrap()

    executor = WorkflowExecutor(
        engine.registry,
        engine.events,
    )

    context = ExecutionContext(
        workflow_id="learning-workflow",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        }
    )

    result = executor.execute(
        "learning-workflow",
        context,
    )

    assert result.success is True

    assert result.completed_steps == 4

    assert (
        result.workflow_id
        == "learning-workflow"
    )
