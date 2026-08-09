"""
OSEF Runtime

test_knowledge_catalog_exporter.py
"""

from pathlib import Path

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_catalog_exporter():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="marketing-content",
        inputs={
            "topic":
            "Protein intake"
        },
    )

    catalog = (
        engine.knowledge_catalog_builder.build()
    )

    path = (
        engine.knowledge_catalog_exporter.export(
            catalog,
            "output/catalog.md",
        )
    )

    exported_file = Path(path)

    assert exported_file.exists()

    content = (
        exported_file.read_text(
            encoding="utf-8",
        )
    )

    assert (
        "Knowledge Catalog"
        in content
    )

    assert (
        catalog.content
        == content
    )
