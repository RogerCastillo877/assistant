"""
OSEF Runtime

graph.py

Runtime dependency graph.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from implementation.runtime.registry import RuntimeRegistry


@dataclass(slots=True)
class RuntimeGraph:

    nodes: dict[str, object] = field(
        default_factory=dict
    )

    edges: dict[str, set[str]] = field(
        default_factory=dict
    )

    # ---------------------------------------------------------
    # Nodes
    # ---------------------------------------------------------

    def add_node(
        self,
        node_id: str,
        obj: object,
    ) -> None:

        self.nodes[node_id] = obj

        self.edges.setdefault(
            node_id,
            set(),
        )

    # ---------------------------------------------------------
    # Edges
    # ---------------------------------------------------------

    def add_edge(
        self,
        source: str,
        target: str,
    ) -> None:

        self.edges.setdefault(
            source,
            set(),
        ).add(target)

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def neighbors(
        self,
        node_id: str,
    ) -> list[str]:

        return sorted(
            self.edges.get(
                node_id,
                set(),
            )
        )

    def contains(
        self,
        node_id: str,
    ) -> bool:

        return node_id in self.nodes

    def node_count(self) -> int:

        return len(self.nodes)

    def edge_count(self) -> int:

        return sum(
            len(v)
            for v in self.edges.values()
        )

    # ---------------------------------------------------------
    # Traversal
    # ---------------------------------------------------------

    def descendants(
        self,
        node_id: str,
    ) -> set[str]:

        visited = set()

        stack = [node_id]

        while stack:

            current = stack.pop()

            for child in self.edges.get(
                current,
                set(),
            ):

                if child not in visited:

                    visited.add(child)

                    stack.append(child)

        return visited
