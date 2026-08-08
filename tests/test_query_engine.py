"""
OSEF Runtime

test_query_engine.py
"""

from implementation.runtime.engine import (
    bootstrap,
)

from implementation.runtime.memory_engine import (
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeRecord,
)


def test_query_engine():

    engine = bootstrap()

    engine.memory_engine.store(
        MemoryRecord(
            id="mem-001",
            title="Kubernetes",
            content="kubectl get nodes",
            memory_type="execution",
            tags=["kubernetes"],
            source="test",
        )
    )

    engine.knowledge.store(
        KnowledgeRecord(
            id="knw-001",
            title="Pattern",
            content="Use trusted sources",
            knowledge_type="pattern",
            tags=["search"],
            source="test",
        )
    )

    memories = (
        engine.query.memories(
            tag="kubernetes"
        )
    )

    knowledge = (
        engine.query.knowledge(
            knowledge_type="pattern"
        )
    )

    assert len(memories) == 1

    assert len(knowledge) == 1
