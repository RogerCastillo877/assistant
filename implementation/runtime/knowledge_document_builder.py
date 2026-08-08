"""
OSEF Runtime

knowledge_document_builder.py

Builds human-readable knowledge documents.
"""

from __future__ import annotations

from implementation.runtime.knowledge_document import (
    KnowledgeDocument,
)

from implementation.runtime.mission_projection_engine import (
    MissionProjectionEngine,
)


class KnowledgeDocumentBuilder:

    def __init__(
        self,
        mission_projection,
    ) -> None:

        self.mission_projection = (
            mission_projection
        )

    def build(
        self,
        mission_id: str,
    ) -> KnowledgeDocument:

        projection = (
            self.mission_projection.build(
                mission_id
            )
        )

        mission = projection.mission

        content = f"""
# {mission.name}

## Mission

Purpose:
{mission.purpose}

Description:
{mission.description}

## Knowledge Summary

Memories:
{len(projection.memories)}

Knowledge:
{len(projection.knowledge)}

Traces:
{len(projection.traces)}

## Execution Summary

Artifacts:
{len(projection.artifacts)}

Decisions:
{len(projection.decisions)}

Outcomes:
{len(projection.outcomes)}

## Knowledge Items
"""

        for item in projection.knowledge:

            content += f"""

### {item.title}

{item.content}
"""

        return KnowledgeDocument(
            mission_id=mission.id,
            title=mission.name,
            content=content.strip(),
        )
