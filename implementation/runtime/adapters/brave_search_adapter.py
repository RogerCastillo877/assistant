"""
OSEF Runtime

brave_search_adapter.py
"""

from __future__ import annotations

from implementation.runtime.web_search_adapter import (
    WebSearchAdapter,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class BraveSearchAdapter(
    WebSearchAdapter,
):

    def __init__(
        self,
        api_key: str,
    ) -> None:

        self.api_key = api_key

    def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[
        WebSearchResult
    ]:

        raise NotImplementedError(
            "BraveSearchAdapter "
            "not implemented yet."
        )
