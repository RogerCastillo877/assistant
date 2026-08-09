"""
OSEF Runtime

test_web_search_adapter.py
"""

from implementation.runtime.web_search_adapter import (
    WebSearchAdapter,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)


class FakeWebSearchAdapter(
    WebSearchAdapter,
):

    def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[
        WebSearchResult
    ]:

        return [
            WebSearchResult(
                title="Strength Training",
                url="https://example.com",
                snippet="Benefits of strength training",
                source="fake",
            )
        ]


def test_web_search_adapter():

    adapter = (
        FakeWebSearchAdapter()
    )

    results = adapter.search(
        "strength training"
    )

    assert (
        len(results)
        == 1
    )

    assert (
        results[0].title
        == "Strength Training"
    )
