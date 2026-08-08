"""
OSEF Runtime

test_runtime_state_graph_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)

from implementation.runtime.runtime_state_graph_builder import (
    RuntimeStateGraphBuilder,
)


def test_graph_builder():

    engine = bootstrap()

    graph = RuntimeStateGraphBuilder(
        engine.registry
    ).build()

    assert (
        graph.node_count() > 0
    )

    assert graph.contains(
        "learning"
    )

    assert graph.contains(
        "learning-workflow"
    )

    descendants = graph.descendants(
        "learning"
    )

    assert (
        "learning-workflow"
        in descendants
    )
