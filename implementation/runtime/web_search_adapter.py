"""
OSEF Runtime

web_search_adapter.py
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class WebSearchAdapter(
    ABC,
):

    @abstractmethod
    def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[
        WebSearchResult
    ]:
        """
        Execute a search query.
        """
