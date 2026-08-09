"""
OSEF Runtime

web_search_result.py

Normalized web search result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class WebSearchResult:

    title: str

    url: str

    snippet: str

    source: str

    score: float = 1.0
