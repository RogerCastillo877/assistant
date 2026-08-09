"""
OSEF Runtime

test_web_search_knowledge_hook.py
"""

from types import SimpleNamespace

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
)

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)

from implementation.runtime.web_search_knowledge_hook import (
    WebSearchKnowledgeHook,
)


def test_web_search_knowledge_hook():

    memory_engine = MemoryEngine()

    knowledge_engine = KnowledgeEngine()

    traceability_engine = (
        TraceabilityEngine()
    )

    hook = WebSearchKnowledgeHook(
        memory_engine=memory_engine,
        knowledge_engine=knowledge_engine,
        traceability_engine=traceability_engine,
    )

    result = WebSearchResult(
        title="Strength Training Benefits",
        url="https://example.com/strength",
        snippet=(
            "Strength training can improve "
            "muscle strength and physical function."
        ),
        source="mock",
        score=0.9,
    )

    context = SimpleNamespace(
        workflow_id="marketing-content-workflow",
        mission_id="marketing-content",
        outputs={
            "tool:web-search": {
                "tool": "web-search",
                "status": "success",
                "results": [
                    result
                ],
            }
        },
    )

    hook.execute(
        {
            "context": context,
            "workflow_id": (
                "marketing-content-workflow"
            ),
        }
    )

    memories = (
        memory_engine.all()
    )

    knowledge = (
        knowledge_engine.all()
    )

    traces = (
        traceability_engine.all()
    )

    assert len(memories) == 1

    assert len(knowledge) == 1

    assert len(traces) == 1

    assert (
        memories[0].title
        == "Strength Training Benefits"
    )

    assert (
        memories[0].memory_type
        == "web-search"
    )

    assert (
        knowledge[0].knowledge_type
        == "web-search"
    )

    assert (
        knowledge[0].confidence
        == 0.9
    )

    assert (
        traces[0].source_id
        == memories[0].id
    )

    assert (
        traces[0].target_id
        == knowledge[0].id
    )

    assert (
        traces[0].relationship
        == "promoted_to"
    )


def test_web_search_knowledge_hook_without_results():

    memory_engine = MemoryEngine()

    knowledge_engine = KnowledgeEngine()

    traceability_engine = (
        TraceabilityEngine()
    )

    hook = WebSearchKnowledgeHook(
        memory_engine=memory_engine,
        knowledge_engine=knowledge_engine,
        traceability_engine=traceability_engine,
    )

    context = SimpleNamespace(
        workflow_id="marketing-content-workflow",
        mission_id="marketing-content",
        outputs={
            "tool:web-search": {
                "tool": "web-search",
                "status": "success",
                "results": [],
            }
        },
    )

    hook.execute(
        {
            "context": context,
            "workflow_id": (
                "marketing-content-workflow"
            ),
        }
    )

    assert (
        memory_engine.count()
        == 0
    )

    assert (
        knowledge_engine.count()
        == 0
    )

    assert (
        traceability_engine.count()
        == 0
    )


def test_web_search_knowledge_hook_without_search_output():

    memory_engine = MemoryEngine()

    knowledge_engine = KnowledgeEngine()

    traceability_engine = (
        TraceabilityEngine()
    )

    hook = WebSearchKnowledgeHook(
        memory_engine=memory_engine,
        knowledge_engine=knowledge_engine,
        traceability_engine=traceability_engine,
    )

    context = SimpleNamespace(
        workflow_id="marketing-content-workflow",
        mission_id="marketing-content",
        outputs={},
    )

    hook.execute(
        {
            "context": context,
            "workflow_id": (
                "marketing-content-workflow"
            ),
        }
    )

    assert (
        memory_engine.count()
        == 0
    )

    assert (
        knowledge_engine.count()
        == 0
    )

    assert (
        traceability_engine.count()
        == 0
    )
