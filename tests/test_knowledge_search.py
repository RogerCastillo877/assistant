"""
OSEF Runtime

test_knowledge_search.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_search():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="marketing-content",
        inputs={
            "topic":
            "Protein intake"
        },
    )

    results = (
        engine.knowledge_search.search(
            "workflow"
        )
    )

    assert (
        len(results)
        >= 1
    )

    assert (
        results[0].score
        > 0
    )

    assert (
        results[0].source_type
        in [
            "memory",
            "knowledge",
        ]
    )
