"""
OSEF Runtime

mock_web_search_adapter.py

Deterministic web search adapter used for tests and development.
"""

from __future__ import annotations

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class MockWebSearchAdapter:
    """
    Deterministic web search provider for tests.
    """

    def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[WebSearchResult]:

        query = query.strip()

        if not query:
            return []

        result = WebSearchResult(
            title=f"Mock Result for {query}",
            url="https://mock.local",
            snippet=(
                f"Mock search result for "
                f"query '{query}'."
            ),
            source="mock",
            score=1.0,
        )

        return [result][:limit]
