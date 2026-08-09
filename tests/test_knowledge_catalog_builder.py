"""
OSEF Runtime

test_knowledge_catalog_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_catalog_builder():

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

    assert (
        catalog.total_items
        >= 1
    )

    assert (
        len(catalog.items)
        >= 1
    )

    assert (
        "Knowledge Catalog"
        in catalog.content
    )
