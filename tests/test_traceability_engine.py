from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)


def test_trace_creation():

    engine = TraceabilityEngine()

    engine.link(
        source_id="workflow-1",
        target_id="memory-1",
        relationship="generated",
    )

    assert engine.count() == 1


def test_trace_by_source():

    engine = TraceabilityEngine()

    engine.link(
        source_id="workflow-1",
        target_id="memory-1",
        relationship="generated",
    )

    records = engine.by_source(
        "workflow-1"
    )

    assert len(records) == 1


def test_trace_by_target():

    engine = TraceabilityEngine()

    engine.link(
        source_id="workflow-1",
        target_id="memory-1",
        relationship="generated",
    )

    records = engine.by_target(
        "memory-1"
    )

    assert len(records) == 1


def test_trace_descendants():

    engine = TraceabilityEngine()

    engine.link(
        source_id="workflow-1",
        target_id="memory-1",
        relationship="generated",
    )

    engine.link(
        source_id="workflow-1",
        target_id="memory-2",
        relationship="generated",
    )

    descendants = engine.descendants(
        "workflow-1"
    )

    assert len(descendants) == 2

    assert descendants == [
        "memory-1",
        "memory-2",
    ]
