"""
OSEF Runtime

artifact_engine.py

Artifact management.
"""

from __future__ import annotations

from implementation.runtime.artifact_record import (
    ArtifactRecord,
)


class ArtifactEngine:

    def __init__(self) -> None:

        self._artifacts: dict[
            str,
            ArtifactRecord,
        ] = {}

    def store(
        self,
        artifact: ArtifactRecord,
    ) -> None:

        self._artifacts[
            artifact.id
        ] = artifact

    def get(
        self,
        artifact_id: str,
    ) -> ArtifactRecord | None:

        return self._artifacts.get(
            artifact_id
        )

    def all(
        self,
    ) -> list[ArtifactRecord]:

        return list(
            self._artifacts.values()
        )

    def count(
        self,
    ) -> int:

        return len(
            self._artifacts
        )

    def clear(
        self,
    ) -> None:

        self._artifacts.clear()

    def search_by_tag(
        self,
        tag: str,
    ) -> list[ArtifactRecord]:

        return [
            artifact
            for artifact in self._artifacts.values()
            if tag in artifact.tags
        ]

    def search_by_type(
        self,
        artifact_type: str,
    ) -> list[ArtifactRecord]:

        return [
            artifact
            for artifact in self._artifacts.values()
            if artifact.artifact_type
            == artifact_type
        ]
