"""
OSEF Runtime

runtime_state_graph_builder.py
"""

from __future__ import annotations

from implementation.runtime.graph_edge import (
    GraphEdge,
)

from implementation.runtime.knowledge_graph import (
    KnowledgeGraph,
)


class RuntimeStateGraphBuilder:

    def __init__(
        self,
        registry,
    ) -> None:

        self.registry = registry

    def build(
        self,
    ) -> KnowledgeGraph:

        graph = KnowledgeGraph()

        #
        # Missions
        #

        for mission in (
            self.registry.missions.values()
        ):

            graph.add_node(
                mission.id,
                mission,
            )

            for workflow_id in (
                mission.workflows
            ):

                graph.add_edge(
                    GraphEdge(
                        source_id=mission.id,
                        target_id=workflow_id,
                        relationship="uses",
                    )
                )

        #
        # Workflows
        #

        for workflow in (
            self.registry.workflows.values()
        ):

            graph.add_node(
                workflow.id,
                workflow,
            )

            #
            # workflow.steps
            #

            if hasattr(
                workflow,
                "steps",
            ):

                for step in workflow.steps:

                    capability_id = (
                        step.get(
                            "capability"
                        )
                    )

                    if capability_id:

                        graph.add_edge(
                            GraphEdge(
                                source_id=workflow.id,
                                target_id=capability_id,
                                relationship="uses",
                            )
                        )

            #
            # workflow.capabilities
            #

            elif hasattr(
                workflow,
                "capabilities",
            ):

                for capability_id in (
                    workflow.capabilities
                ):

                    graph.add_edge(
                        GraphEdge(
                            source_id=workflow.id,
                            target_id=capability_id,
                            relationship="uses",
                        )
                    )

        #
        # Capabilities
        #

        for capability in (
            self.registry.capabilities.values()
        ):

            graph.add_node(
                capability.id,
                capability,
            )

            for skill_id in (
                capability.skills
            ):

                graph.add_edge(
                    GraphEdge(
                        source_id=capability.id,
                        target_id=skill_id,
                        relationship="uses",
                    )
                )

        #
        # Skills
        #

        for skill in (
            self.registry.skills.values()
        ):

            graph.add_node(
                skill.id,
                skill,
            )

            for tool_id in (
                skill.tools
            ):

                graph.add_edge(
                    GraphEdge(
                        source_id=skill.id,
                        target_id=tool_id,
                        relationship="uses",
                    )
                )

        #
        # Tools
        #

        for tool in (
            self.registry.tools.values()
        ):

            graph.add_node(
                tool.id,
                tool,
            )

        return graph
