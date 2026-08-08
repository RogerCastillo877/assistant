"""
OSEF Runtime

knowledge_graph.py

Runtime knowledge graph.
"""

from __future__ import annotations

from implementation.runtime.graph_edge import (
    GraphEdge,
)


class KnowledgeGraph:

    def __init__(self) -> None:

        self._nodes: dict[str, object] = {}

        self._edges: list[
            GraphEdge
        ] = []

    def add_node(
        self,
        node_id: str,
        node: object,
    ) -> None:

        self._nodes[node_id] = node

    def add_edge(
        self,
        edge: GraphEdge,
    ) -> None:

        self._edges.append(edge)

    def get_node(
        self,
        node_id: str,
    ) -> object | None:

        return self._nodes.get(
            node_id
        )

    def nodes(
        self,
    ) -> dict[str, object]:

        return dict(
            self._nodes
        )

    def edges(
        self,
    ) -> list[GraphEdge]:

        return list(
            self._edges
        )

    def neighbors(
        self,
        node_id: str,
    ) -> list[str]:

        return [
            edge.target_id
            for edge in self._edges
            if edge.source_id
            == node_id
        ]

    def descendants(
        self,
        node_id: str,
    ) -> list[str]:

        visited: set[str] = set()

        stack = [node_id]

        while stack:

            current = stack.pop()

            for edge in self._edges:

                if (
                    edge.source_id
                    != current
                ):
                    continue

                target = (
                    edge.target_id
                )

                if target in visited:
                    continue

                visited.add(
                    target
                )

                stack.append(
                    target
                )

        return list(
            visited
        )

    def node_count(
        self,
    ) -> int:

        return len(
            self._nodes
        )

    def edge_count(
        self,
    ) -> int:

        return len(
            self._edges
        )

    def clear(
        self,
    ) -> None:

        self._nodes.clear()

        self._edges.clear()

    def contains(
        self,
        node_id: str,
    ) -> bool:

        return (
            node_id
            in self._nodes
    )
