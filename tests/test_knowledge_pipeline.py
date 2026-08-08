from implementation.runtime.memory_engine import (
    MemoryRecord,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
)

from implementation.runtime.knowledge_builder import (
    KnowledgeBuilder,
)

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.traceability_service import (
    TraceabilityService,
)

from implementation.runtime.knowledge_pipeline import (
    KnowledgePipeline,
)


def test_memory_to_knowledge_pipeline():

    knowledge_engine = (
        KnowledgeEngine()
    )

    trace_engine = (
        TraceabilityEngine()
    )

    builder = KnowledgeBuilder(
        knowledge_engine=
            knowledge_engine
    )

    trace_service = (
        TraceabilityService(
            traceability_engine=
                trace_engine
        )
    )

    pipeline = KnowledgePipeline(
        knowledge_builder=builder,
        traceability_service=
            trace_service,
    )

    memory = MemoryRecord(
        id="mem-001",
        title="Kubernetes Pattern",
        content=(
            "Always start with "
            "kubectl get nodes"
        ),
        memory_type="execution",
        tags=["kubernetes"],
        source="manual",
    )

    knowledge_engine = KnowledgeEngine()

    knowledge = pipeline.process(
        memory,
        knowledge_engine
    )

    assert (
        knowledge_engine.count()
        == 1
    )

    assert (
        trace_engine.count()
        == 1
    )

    assert (
        knowledge.id
        == "knowledge-mem-001"
    )
