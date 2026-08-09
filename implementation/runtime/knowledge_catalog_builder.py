"""
OSEF Runtime

knowledge_catalog_builder.py
"""

from __future__ import annotations

from implementation.runtime.knowledge_catalog import (
    KnowledgeCatalog,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
)


class KnowledgeCatalogBuilder:

    def __init__(
        self,
        knowledge_engine: KnowledgeEngine,
    ) -> None:

        self.knowledge_engine = (
            knowledge_engine
        )

    def build(
        self,
    ) -> KnowledgeCatalog:

        items = (
            self.knowledge_engine.all()
        )

        content = (
            "# Knowledge Catalog\n\n"
            f"Total Items: {len(items)}\n\n"
        )

        if items:

            for item in items:

                content += (
                    f"## {item.title}\n\n"
                    f"ID: {item.id}\n\n"
                    f"Type: {item.knowledge_type}\n\n"
                    f"Source: {item.source}\n\n"
                    f"Confidence: "
                    f"{item.confidence}\n\n"
                )

        else:

            content += (
                "No knowledge available.\n"
            )

        return KnowledgeCatalog(
            total_items=len(items),
            items=items,
            content=content,
        )
