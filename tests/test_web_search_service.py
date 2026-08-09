"""
OSEF Runtime

test_web_search_service.py
"""

from implementation.runtime.web_search_adapter import (
    WebSearchAdapter,
)

from implementation.runtime.web_search_result import (
    WebSearchResult,
)

from implementation.runtime.web_search_service import (
    WebSearchService,
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
                title="Protein Intake",
                url="https://example.com",
                snippet="Daily protein recommendations",
                source="fake",
            )
        ]


def test_web_search_service():

    service = (
        WebSearchService(
            FakeWebSearchAdapter()
        )
    )

    results = service.search(
        "protein intake"
    )

    assert (
        len(results)
        == 1
    )

    assert (
        results[0].title
        == "Protein Intake"
    )
