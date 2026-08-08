"""
OSEF Runtime

test_knowledge_document_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_document_builder():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="learning",
        inputs={
            "learning-goal":
            "Learn Kubernetes"
        },
    )

    document = (
        engine.knowledge_document_builder.build(
            "learning"
        )
    )

    assert (
        document.mission_id
        == "learning"
    )

    assert (
        "Learning Mission"
        in document.content
    )

    assert (
        "Knowledge Summary"
        in document.content
    )
