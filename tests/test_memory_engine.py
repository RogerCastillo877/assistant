from implementation.runtime.memory_engine import (
    MemoryEngine,
)

from implementation.runtime.memory_engine import (
    MemoryRecord,
)


def test_store_memory():

    memory = MemoryEngine()

    record = MemoryRecord(
        id="mem-001",
        title="Kubernetes",
        content="Pods are basic units",
        memory_type="lesson",
        tags=["kubernetes"],
    )

    memory.store(record)

    assert memory.count() == 1

    assert memory.get(
        "mem-001"
    ) is not None


def test_search_by_tag():

    memory = MemoryEngine()

    memory.store(
        MemoryRecord(
            id="mem-001",
            title="Kubernetes",
            content="Pods",
            memory_type="lesson",
            tags=["kubernetes"],
        )
    )

    memory.store(
        MemoryRecord(
            id="mem-002",
            title="Docker",
            content="Containers",
            memory_type="lesson",
            tags=["docker"],
        )
    )

    results = memory.search_by_tag(
        "kubernetes"
    )

    assert len(results) == 1

    assert (
        results[0].id
        == "mem-001"
    )


def test_search_by_type():

    memory = MemoryEngine()

    memory.store(
        MemoryRecord(
            id="mem-001",
            title="Lesson",
            content="Content",
            memory_type="lesson",
        )
    )

    memory.store(
        MemoryRecord(
            id="mem-002",
            title="Pattern",
            content="Content",
            memory_type="pattern",
        )
    )

    results = memory.search_by_type(
        "lesson"
    )

    assert len(results) == 1

    assert (
        results[0].memory_type
        == "lesson"
    )


def test_clear_memory():

    memory = MemoryEngine()

    memory.store(
        MemoryRecord(
            id="mem-001",
            title="Test",
            content="Test",
            memory_type="lesson",
        )
    )

    assert memory.count() == 1

    memory.clear()

    assert memory.count() == 0
