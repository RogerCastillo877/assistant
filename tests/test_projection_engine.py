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

from implementation.runtime.artifact_record import (
    ArtifactRecord,
)

from implementation.runtime.decision_engine import (
    DecisionEngine,
)

from implementation.runtime.decision_record import (
    DecisionRecord,
)

from implementation.runtime.outcome_engine import (
    OutcomeEngine,
)

from implementation.runtime.outcome_record import (
    OutcomeRecord,
)

from implementation.runtime.projection_engine import (
    ProjectionEngine,
)


def test_projection_engine():

    memory = MemoryEngine()

    knowledge = KnowledgeEngine()

    traceability = TraceabilityEngine()

    artifacts = ArtifactEngine()

    decisions = DecisionEngine()

    outcomes = OutcomeEngine()

    memory.store(
        MemoryRecord(
            id="mem-001",
            title="Memory",
            content="content",
            memory_type="execution",
        )
    )

    knowledge.store(
        KnowledgeRecord(
            id="knw-001",
            title="Knowledge",
            content="content",
            knowledge_type="pattern",
        )
    )

    traceability.link(
            source_id="mem-001",
            target_id="knw-001",
            relationship="promoted_to",
    )

    artifacts.store(
        ArtifactRecord(
            id="art-001",
            title="Artifact",
            content="content",
            artifact_type="report",
        )
    )

    decisions.record(
        DecisionRecord(
            id="dec-001",
            title="Decision",
            decision="approved",
            rationale="test",
            decision_type="execution",
        )
    )

    outcomes.store(
        OutcomeRecord(
            id="out-001",
            title="Outcome",
            description="done",
            outcome_type="workflow",
            status="completed",
        )
    )

    engine = ProjectionEngine(
        memory_engine=memory,
        knowledge_engine=knowledge,
        traceability_engine=traceability,
        artifact_engine=artifacts,
        decision_engine=decisions,
        outcome_engine=outcomes,
    )

    projection = engine.build(
        "learning-workflow"
    )

    assert projection.workflow_id == (
        "learning-workflow"
    )

    assert len(projection.memories) == 1

    assert len(projection.knowledge) == 1

    assert len(projection.traces) == 1

    assert len(projection.artifacts) == 1

    assert len(projection.decisions) == 1

    assert len(projection.outcomes) == 1
