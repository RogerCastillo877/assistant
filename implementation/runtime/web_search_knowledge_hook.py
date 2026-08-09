"""
OSEF Runtime

web_search_knowledge_hook.py

Promotes web search results into memory and knowledge.
"""

from __future__ import annotations

import re

from implementation.runtime.knowledge_engine import (
    KnowledgeEngine,
    KnowledgeRecord,
)

from implementation.runtime.memory_engine import (
    MemoryEngine,
    MemoryRecord,
)

from implementation.runtime.traceability_engine import (
    TraceabilityEngine,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class WebSearchKnowledgeHook:
    """
    Promotes normalized web search results into
    runtime memory and knowledge.

    Expected event payload:

        {
            "context": ExecutionContext,
            "workflow_id": "...",
        }

    The search results are obtained from:

        context.outputs["tool:web-search"]["results"]
    """

    def __init__(
        self,
        memory_engine: MemoryEngine,
        knowledge_engine: KnowledgeEngine,
        traceability_engine: TraceabilityEngine,
    ) -> None:

        self.memory_engine = (
            memory_engine
        )

        self.knowledge_engine = (
            knowledge_engine
        )

        self.traceability_engine = (
            traceability_engine
        )

    def execute(
        self,
        payload: dict,
    ) -> None:

        context = payload.get(
            "context"
        )

        if context is None:
            return

        workflow_id = (
            payload.get(
                "workflow_id"
            )
            or getattr(
                context,
                "workflow_id",
                None,
            )
        )

        mission_id = (
            getattr(
                context,
                "mission_id",
                None,
            )
        )

        results = (
            self._extract_results(
                context
            )
        )

        if not results:
            return

        for index, result in enumerate(
            results
        ):

            if not isinstance(
                result,
                WebSearchResult,
            ):
                continue

            memory_id = (
                self._build_memory_id(
                    workflow_id=workflow_id,
                    index=index,
                    result=result,
                )
            )

            content = (
                self._build_content(
                    result
                )
            )

            memory = MemoryRecord(
                id=memory_id,
                title=result.title,
                content=content,
                memory_type="web-search",
                tags=[
                    "web-search",
                    result.source,
                ],
                source="web-search-hook",
            )

            self.memory_engine.store(
                memory
            )

            knowledge_id = (
                f"knowledge-{memory_id}"
            )

            knowledge = KnowledgeRecord(
                id=knowledge_id,
                title=result.title,
                content=content,
                knowledge_type="web-search",
                tags=[
                    "web-search",
                    result.source,
                ],
                source="web-search-hook",
                confidence=result.score,
            )

            self.knowledge_engine.store(
                knowledge
            )

            self.traceability_engine.link(
                source_id=memory.id,
                target_id=knowledge.id,
                relationship="promoted_to",
                metadata={
                    "source": result.source,
                    "url": result.url,
                    "workflow_id": workflow_id,
                    "mission_id": mission_id,
                },
            )

    @staticmethod
    def _extract_results(
        context,
    ) -> list[WebSearchResult]:

        outputs = getattr(
            context,
            "outputs",
            None,
        )

        if not isinstance(
            outputs,
            dict,
        ):
            return []

        tool_result = outputs.get(
            "tool:web-search"
        )

        if not isinstance(
            tool_result,
            dict,
        ):
            return []

        results = tool_result.get(
            "results",
            [],
        )

        if not isinstance(
            results,
            list,
        ):
            return []

        return [
            result
            for result in results
            if isinstance(
                result,
                WebSearchResult,
            )
        ]

    @staticmethod
    def _build_memory_id(
        workflow_id: str | None,
        index: int,
        result: WebSearchResult,
    ) -> str:

        workflow_part = (
            workflow_id
            or "unknown-workflow"
        )

        slug = re.sub(
            r"[^a-z0-9]+",
            "-",
            result.title.lower(),
        ).strip("-")

        return (
            f"memory-"
            f"{workflow_part}-"
            f"{index}-"
            f"{slug}"
        )

    @staticmethod
    def _build_content(
        result: WebSearchResult,
    ) -> str:

        return (
            f"{result.snippet}\n\n"
            f"URL: {result.url}\n"
            f"Source provider: {result.source}"
        )
