"""
OSEF Runtime

test_tool_executor_web_search.py
"""

from implementation.runtime.engine import (bootstrap)
from implementation.runtime.context import (ExecutionContext)
from implementation.runtime.state import (WorkflowState)

def test_tool_executor_web_search():

    engine = bootstrap()

    context = ExecutionContext(
        mission_id="test",
        workflow_id="test",
        state=WorkflowState(
            workflow_id="test"
        ),
        memory=engine.memory_engine,
        inputs={
            "topic":
            "strength training"
        },
    )

    result = (
        engine.tool_executor.execute(
            tool_id="web-search",
            context=context,
        )
    )

    assert (
        result["status"]
        == "success"
    )

    assert (
        len(
            result["results"]
        )
        >= 1
    )
