"""
OSEF Runtime

graph_builder.py

Builds dependency graph from registry.
"""

from __future__ import annotations

from implementation.runtime.graph import RuntimeGraph
from implementation.runtime.registry import RuntimeRegistry


class RuntimeGraphBuilder:

    def __init__(
        self,
        registry: RuntimeRegistry,
    ) -> None:

        self.registry = registry

    def build(self) -> RuntimeGraph:

        graph = RuntimeGraph()

        # -------------------------------------------------
        # Register nodes
        # -------------------------------------------------

        collections = [
            self.registry.missions,
            self.registry.agents,
            self.registry.workflows,
            self.registry.capabilities,
            self.registry.skills,
            self.registry.tools,
            self.registry.resources,
            self.registry.memory,
            self.registry.knowledge,
        ]

        for collection in collections:

            for entity in collection.values():

                graph.add_node(
                    entity.id,
                    entity,
                )

        # -------------------------------------------------
        # Mission -> Workflow
        # -------------------------------------------------

        for mission in self.registry.missions.values():

            for workflow_id in mission.workflows:

                graph.add_edge(
                    mission.id,
                    workflow_id,
                )

        # -------------------------------------------------
        # Agent -> Workflow
        # -------------------------------------------------

        for agent in self.registry.agents.values():

            for workflow_id in agent.workflows:

                graph.add_edge(
                    agent.id,
                    workflow_id,
                )

            for capability_id in agent.capabilities:

                graph.add_edge(
                    agent.id,
                    capability_id,
                )

        # -------------------------------------------------
        # Workflow -> Capability
        # -------------------------------------------------

        for workflow in self.registry.workflows.values():

            for step in workflow.steps:

                capability_id = step.get(
                    "capability"
                )

                if capability_id:

                    graph.add_edge(
                        workflow.id,
                        capability_id,
                    )

        # -------------------------------------------------
        # Capability -> Skill
        # -------------------------------------------------

        for capability in self.registry.capabilities.values():

            for skill_id in capability.skills:

                graph.add_edge(
                    capability.id,
                    skill_id,
                )

        # -------------------------------------------------
        # Skill -> Tool
        # -------------------------------------------------

        for skill in self.registry.skills.values():

            for tool_id in skill.tools:

                graph.add_edge(
                    skill.id,
                    tool_id,
                )

            for resource_id in skill.resources:

                graph.add_edge(
                    skill.id,
                    resource_id,
                )

        return graph
