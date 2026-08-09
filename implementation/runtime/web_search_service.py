"""
OSEF Runtime

web_search_service.py
"""

from __future__ import annotations

from implementation.runtime.web_search_adapter import (
    WebSearchAdapter,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class WebSearchService:

    def __init__(
        self,
        adapter: WebSearchAdapter,
    ) -> None:

        self.adapter = adapter

    def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[
        WebSearchResult
    ]:

        return self.adapter.search(
            query=query,
            limit=limit,
        )
