from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.traceability_service import (
    TraceabilityService,
)


def test_track_workflow_memory():

    engine = TraceabilityEngine()

    service = TraceabilityService(
        traceability_engine=engine
    )

    service.track_workflow_memory(
        workflow_id="learning-workflow",
        memory_id="memory-001",
    )

    assert engine.count() == 1

    trace = engine.all()[0]

    assert (
        trace.relationship
        == "generated"
    )


def test_track_memory_knowledge():

    engine = TraceabilityEngine()

    service = TraceabilityService(
        traceability_engine=engine
    )

    service.track_memory_knowledge(
        memory_id="memory-001",
        knowledge_id="knowledge-001",
    )

    assert engine.count() == 1

    trace = engine.all()[0]

    assert (
        trace.relationship
        == "promoted_to"
    )
