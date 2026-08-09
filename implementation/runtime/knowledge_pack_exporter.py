"""
OSEF Runtime

knowledge_pack_exporter.py
"""

from __future__ import annotations

from pathlib import Path

from implementation.runtime.knowledge_pack import (
    KnowledgePack,
)


class KnowledgePackExporter:

    def export(
        self,
        pack: KnowledgePack,
        output_path: str,
    ) -> Path:

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            pack.content,
            encoding="utf-8",
        )

        return path
