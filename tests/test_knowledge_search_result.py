"""
OSEF Runtime

test_knowledge_search_result.py
"""

from implementation.runtime.knowledge_engine import (
    KnowledgeRecord,
)

from implementation.runtime.knowledge_search_result import (
    KnowledgeSearchResult,
)


def test_knowledge_search_result():

    result = (
        KnowledgeSearchResult(
            query="workflow"
        )
    )

    assert result.query == "workflow"

    assert result.empty is True

    record = KnowledgeRecord(
        id="knowledge-001",
        title="Workflow Pattern",
        content="Workflow executed successfully",
        knowledge_type="pattern",
        tags=[
            "workflow"
        ],
        source="test",
        confidence=1.0,
    )

    result.add(
        record
    )

    assert result.empty is False

    assert (
        result.total_results
        == 1
    )

    assert (
        len(
            result.results
        )
        == 1
    )

    assert (
        result.top(1)[0].id
        == "knowledge-001"
    )
