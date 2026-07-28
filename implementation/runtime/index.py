"""
OSEF Runtime

index.py

Builds searchable indexes for an OSEF project.

This module DOES NOT validate anything.

Responsibilities

- Build indexes
- Resolve identifiers
- Provide fast lookups

Validation belongs to the validators.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from implementation.runtime.loader import ProjectModel


# ---------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------


@dataclass
class ProjectIndex:
    """
    Search indexes for an OSEF project.
    """

    by_id: dict[str, dict] = field(default_factory=dict)

    by_type: dict[str, list[dict]] = field(default_factory=dict)

    relationships: list[dict] = field(default_factory=list)


# ---------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------


class IndexBuilder:

    def __init__(self, project: ProjectModel):

        self.project = project

        self.index = ProjectIndex()

    # -------------------------------------------------------------

    def build(self) -> ProjectIndex:

        self._index_collection(
            "missions",
            self.project.missions,
        )

        self._index_collection(
            "policies",
            self.project.policies,
        )

        self._index_collection(
            "agents",
            self.project.agents,
        )

        self._index_collection(
            "workflows",
            self.project.workflows,
        )

        self._index_collection(
            "capabilities",
            self.project.capabilities,
        )

        self._index_collection(
            "skills",
            self.project.skills,
        )

        self._index_collection(
            "tools",
            self.project.tools,
        )

        self._index_collection(
            "resources",
            self.project.resources,
        )

        self._index_collection(
            "memory",
            self.project.memory,
        )

        self._index_collection(
            "knowledge",
            self.project.knowledge,
        )

        self._index_collection(
            "documents",
            self.project.documents,
        )

        self._index_collection(
            "decisions",
            self.project.decisions,
        )

        self._index_collection(
            "releases",
            self.project.releases,
        )

        self.index.relationships = self.project.traceability

        return self.index

    # -------------------------------------------------------------

    def _index_collection(
        self,
        collection_name: str,
        collection: list[dict],
    ) -> None:

        self.index.by_type[collection_name] = collection

        for item in collection:

            item_id = item.get("id")

            if item_id:

                self.index.by_id[item_id] = item


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------


def build_index(project: ProjectModel) -> ProjectIndex:
    """
    Convenience helper.
    """
    return IndexBuilder(project).build()


def exists(
    index: ProjectIndex,
    identifier: str,
) -> bool:

    return identifier in index.by_id


def get(
    index: ProjectIndex,
    identifier: str,
) -> dict[str, Any] | None:

    return index.by_id.get(identifier)


def get_by_type(
    index: ProjectIndex,
    artifact_type: str,
) -> list[dict]:

    return index.by_type.get(
        artifact_type,
        [],
    )
