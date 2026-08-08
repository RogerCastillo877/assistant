"""
OSEF Runtime

test_search_service.py
"""

from implementation.runtime.memory_engine import (
    MemoryEngine,
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
    KnowledgeRecord,
)

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.artifact_engine import (
    ArtifactEngine,
)

from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)

from implementation.runtime.query_engine import (
    QueryEngine,
)

from implementation.runtime.search_service import (
    SearchService,
)

def test_search_service():


    memory_engine = (
        MemoryEngine()
    )

    knowledge_engine = (
        KnowledgeEngine()
    )

    traceability_engine = (
        TraceabilityEngine()
    )

    artifact_engine = (
        ArtifactEngine()
    )

    decision_engine = (
        DecisionEngine()
    )

    outcome_engine = (
        OutcomeEngine()
    )

    memory_engine.store(
        MemoryRecord(
            id="mem-001",
            title="Kubernetes Memory",
            content=(
                "Kubernetes cluster "
                "management"
            ),
            memory_type="workflow",
            tags=[],
            source="test",
        )
    )

    knowledge_engine.store(
        KnowledgeRecord(
            id="knw-001",
            title="Kubernetes Knowledge",
            content=(
                "Kubernetes best "
                "practices"
            ),
            knowledge_type="pattern",
            tags=[],
            source="test",
        )
    )

    query_engine = QueryEngine(
        memory_engine=memory_engine,
        knowledge_engine=knowledge_engine,
        traceability_engine=traceability_engine,
        artifact_engine=artifact_engine,
        decision_engine=decision_engine,
        outcome_engine=outcome_engine,
    )

    search_service = SearchService(
        query_engine=query_engine
    )

    results = (
        search_service.search(
            "Kubernetes"
        )
    )

    assert len(results) == 2

    assert (
        results[0].source_type
        in [
            "memory",
            "knowledge",
        ]
    )

    assert (
        results[1].source_type
        in [
            "memory",
            "knowledge",
        ]
    )
