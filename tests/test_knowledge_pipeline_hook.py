from implementation.runtime.memory_engine import (
    MemoryEngine,
)

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
)

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.traceability_service import (
    TraceabilityService,
)

from implementation.runtime.knowledge_builder import (
    KnowledgeBuilder,
)

from implementation.runtime.knowledge_pipeline import (
    KnowledgePipeline,
)

from implementation.runtime.context import (
    ExecutionContext,
)

from implementation.runtime.hooks.knowledge_pipeline_hook import (
    KnowledgePipelineHook,
)


def test_hook_promotes_memory():

    memory_engine = MemoryEngine()

    knowledge_engine = (
        KnowledgeEngine()
    )

    traceability_engine = (
        TraceabilityEngine()
    )

    builder = KnowledgeBuilder(
        memory_engine=memory_engine,
        knowledge_engine=knowledge_engine,
    )

    traceability_service = (
        TraceabilityService(
            traceability_engine=
            traceability_engine
        )
    )

    pipeline = KnowledgePipeline(
        knowledge_builder=builder,
        traceability_service=
        traceability_service,
    )

    hook = KnowledgePipelineHook(
        pipeline
    )

    context = ExecutionContext(
        workflow_id="learning-workflow",
        memory=memory_engine,
    )

    hook.execute(
        {
            "workflow_id":
            "learning-workflow",
            "context":
            context,
        }
    )

    assert (
        memory_engine.count()
        == 1
    )

    assert (
        knowledge_engine.count()
        == 1
    )

    assert (
        traceability_engine.count()
        == 1
    )
