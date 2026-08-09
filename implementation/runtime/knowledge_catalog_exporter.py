"""
OSEF Runtime

knowledge_catalog_exporter.py
"""

from __future__ import annotations

from pathlib import Path

from implementation.runtime.knowledge_catalog import (
    KnowledgeCatalog,
)


class KnowledgeCatalogExporter:

    def export(
        self,
        catalog: KnowledgeCatalog,
        path: str,
    ) -> str:

        output_path = Path(path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            catalog.content,
            encoding="utf-8",
        )

        return str(output_path)
