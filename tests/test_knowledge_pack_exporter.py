"""
OSEF Runtime

test_knowledge_pack_exporter.py
"""

from pathlib import Path

from implementation.runtime.engine import (
    bootstrap,
)


def test_knowledge_pack_exporter():

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

    output = (
        engine.knowledge_pack_exporter.export(
            pack,
            "output/test-pack.md",
        )
    )

    assert output.exists()

    content = output.read_text(
        encoding="utf-8"
    )

    assert (
        "Marketing Content Mission"
        in content
    )
