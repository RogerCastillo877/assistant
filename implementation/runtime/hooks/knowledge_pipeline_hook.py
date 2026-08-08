"""
OSEF Runtime

knowledge_pipeline_hook.py

Promotes workflow memories into knowledge.
"""

from __future__ import annotations

from implementation.runtime.memory_engine import (
    MemoryRecord,
)


class KnowledgePipelineHook:

    def __init__(
        self,
        knowledge_pipeline,
    ) -> None:

        self.knowledge_pipeline = (
            knowledge_pipeline
        )

    def execute(
        self,
        payload: dict,
    ) -> None:

        context = payload.get(
            "context"
        )

        workflow_id = payload.get(
            "workflow_id"
        )

        if context is None:
            return

        if context.memory is None:
            return

        memory = MemoryRecord(
            id=f"memory-{workflow_id}",
            title=f"Workflow {workflow_id}",
            content=(
                "Workflow executed successfully"
            ),
            memory_type="workflow",
            tags=[
                "workflow",
                workflow_id,
            ],
            source="knowledge-hook",
        )

        context.memory.store(
            memory
        )

        self.knowledge_pipeline.process(
            memory
        )

        print(
            "[HOOK] workflow.completed"
        )
