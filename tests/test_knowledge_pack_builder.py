"""
OSEF Runtime

test_knowledge_pack_builder.py
"""

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_pack_builder():

    engine = bootstrap()

    engine.mission_runtime.execute(
        mission_id="marketing-content",
        inputs={
            "topic":
            "Protein intake"
        },
    )

    pack = (
        engine.knowledge_pack_builder.build(
            "marketing-content"
        )
    )

    assert (
        pack.mission_id
        == "marketing-content"
    )

    assert len(pack.memories) >= 1

    assert len(pack.knowledge) >= 1

    assert len(pack.traces) >= 1

    assert (
        "Marketing Content Mission"
        in pack.content
    )

    assert (
        "Workflow marketing-content-workflow"
        in pack.content
    )
