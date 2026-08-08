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
        registry=engine.registry,
        events=engine.events,
        policy_engine=engine.policy_engine,
        capability_executor=engine.capability_executor,
        memory_engine=engine.memory_engine,
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
