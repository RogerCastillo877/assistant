from implementation.runtime.engine import bootstrap
from implementation.runtime.graph_builder import (
    RuntimeGraphBuilder,
)


def test_graph_build():

    engine = bootstrap()

    graph = RuntimeGraphBuilder(
        engine.registry
    ).build()

    assert graph.node_count() > 0

    assert graph.contains("learning")

    assert graph.contains("planning")

    assert graph.contains("search")


def test_mission_descendants():

    engine = bootstrap()

    graph = RuntimeGraphBuilder(
        engine.registry
    ).build()

    descendants = graph.descendants(
        "learning"
    )

    assert "learning-workflow" in descendants

    assert "planning" in descendants

    assert "search" in descendants
