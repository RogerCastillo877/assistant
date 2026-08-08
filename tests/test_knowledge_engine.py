from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
    KnowledgeRecord,
)


def test_store_knowledge():

    engine = KnowledgeEngine()

    record = KnowledgeRecord(
        id="knw-001",
        title="Search Pattern",
        content="Use trusted sources.",
        knowledge_type="pattern",
        tags=["search"],
        source="manual",
    )

    engine.store(record)

    assert engine.count() == 1

    loaded = engine.get(
        "knw-001"
    )

    assert loaded is not None

    assert loaded.title == (
        "Search Pattern"
    )


def test_search_by_tag():

    engine = KnowledgeEngine()

    engine.store(
        KnowledgeRecord(
            id="knw-001",
            title="Search Pattern",
            content="Pattern",
            knowledge_type="pattern",
            tags=["search"],
        )
    )

    results = engine.search_by_tag(
        "search"
    )

    assert len(results) == 1


def test_search_by_type():

    engine = KnowledgeEngine()

    engine.store(
        KnowledgeRecord(
            id="knw-001",
            title="Pattern",
            content="Pattern",
            knowledge_type="pattern",
        )
    )

    results = engine.search_by_type(
        "pattern"
    )

    assert len(results) == 1


def test_clear_knowledge():

    engine = KnowledgeEngine()

    engine.store(
        KnowledgeRecord(
            id="knw-001",
            title="Pattern",
            content="Pattern",
            knowledge_type="pattern",
        )
    )

    assert engine.count() == 1

    engine.clear()

    assert engine.count() == 0
