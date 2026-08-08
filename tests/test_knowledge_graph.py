"""
OSEF Runtime

test_knowledge_graph.py
"""

from implementation.runtime.graph_edge import (
    GraphEdge,
)

from implementation.runtime.knowledge_graph import (
    KnowledgeGraph,
)


def test_knowledge_graph():

    graph = KnowledgeGraph()

    graph.add_node(
        "memory-001",
        {"type": "memory"},
    )

    graph.add_node(
        "knowledge-001",
        {"type": "knowledge"},
    )

    graph.add_edge(
        GraphEdge(
            source_id="memory-001",
            target_id="knowledge-001",
            relationship="promoted_to",
        )
    )

    assert (
        graph.node_count()
        == 2
    )

    assert (
        graph.edge_count()
        == 1
    )

    assert (
        graph.neighbors(
            "memory-001"
        )
        ==
        ["knowledge-001"]
    )

    assert (
        graph.descendants(
            "memory-001"
        )
        ==
        ["knowledge-001"]
    )
