"""
OSEF Runtime

knowledge_pack_builder.py
"""

from __future__ import annotations

from implementation.runtime.knowledge_pack import (
    KnowledgePack,
)

from implementation.runtime.mission_projection_engine import (
    MissionProjectionEngine,
)

from implementation.runtime.registry import (
    RuntimeRegistry,
)


class KnowledgePackBuilder:

    def __init__(
        self,
        registry: RuntimeRegistry,
        mission_projection: MissionProjectionEngine,
    ) -> None:

        self.registry = registry

        self.mission_projection = (
            mission_projection
        )

    def build(
        self,
        mission_id: str,
    ) -> KnowledgePack:

        mission = (
            self.registry.get_mission(
                mission_id
            )
        )

        if mission is None:

            raise ValueError(
                f"Mission '{mission_id}' not found."
            )

        projection = (
            self.mission_projection.build(
                mission_id
            )
        )

        memories = projection.memories
        knowledge = projection.knowledge
        traces = projection.traces
        artifacts = projection.artifacts
        decisions = projection.decisions
        outcomes = projection.outcomes

        content = (
            f"# {mission.name}\n\n"
            f"## Mission\n\n"
            f"Purpose:\n"
            f"{mission.purpose}\n\n"
            f"Description:\n"
            f"{mission.description}\n\n"
            f"## Statistics\n\n"
            f"Memories: {len(memories)}\n"
            f"Knowledge: {len(knowledge)}\n"
            f"Traces: {len(traces)}\n"
            f"Artifacts: {len(artifacts)}\n"
            f"Decisions: {len(decisions)}\n"
            f"Outcomes: {len(outcomes)}\n\n"
        )

        #
        # Memories
        #

        content += "## Memories\n\n"

        for memory in memories:

            content += (
                f"### {memory.title}\n\n"
                f"{memory.content}\n\n"
            )

        #
        # Knowledge
        #

        content += "## Knowledge\n\n"

        for item in knowledge:

            content += (
                f"### {item.title}\n\n"
                f"{item.content}\n\n"
            )

        #
        # Traceability
        #

        content += "## Traceability\n\n"

        for trace in traces:

            content += (
                f"{trace.source_id}\n"
                f"--[{trace.relationship}]-->\n"
                f"{trace.target_id}\n\n"
            )

        #
        # Artifacts
        #

        content += "## Artifacts\n\n"

        for artifact in artifacts:

            content += (
                f"### {artifact.title}\n\n"
                f"{artifact.content}\n\n"
            )

        #
        # Decisions
        #

        content += "## Decisions\n\n"

        for decision in decisions:

            content += (
                f"### {decision.title}\n\n"
                f"{decision.rationale}\n\n"
            )

        #
        # Outcomes
        #

        content += "## Outcomes\n\n"

        for outcome in outcomes:

            content += (
                f"### {outcome.title}\n\n"
                f"{outcome.description}\n\n"
            )

        return KnowledgePack(
            mission_id=mission_id,
            title=mission.name,
            memories=memories,
            knowledge=knowledge,
            traces=traces,
            artifacts=artifacts,
            decisions=decisions,
            outcomes=outcomes,
            content=content,
        )
