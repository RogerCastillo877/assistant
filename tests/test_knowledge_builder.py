from implementation.runtime.memory_engine import (
    MemoryEngine,
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
)

from implementation.runtime.knowledge_builder import (
    KnowledgeBuilder,
)


def test_promote_memory():

    memory = MemoryEngine()

    knowledge = KnowledgeEngine()

    builder = KnowledgeBuilder(
        memory_engine=memory,
        knowledge_engine=knowledge,
    )

    memory.store(
        MemoryRecord(
            id="mem-001",
            title="Kubernetes Learning",
            content=(
                "Use official documentation."
            ),
            memory_type="learning",
            tags=["kubernetes"],
            source="workflow",
        )
    )

    record = builder.promote_memory(
        "mem-001"
    )

    assert (
        record.id
        == "knowledge-mem-001"
    )

    assert (
        knowledge.count()
        == 1
    )

    assert (
        knowledge.get(
            "knowledge-mem-001"
        )
        is not None
    )
