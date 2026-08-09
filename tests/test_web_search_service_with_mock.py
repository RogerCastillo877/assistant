"""
OSEF Runtime

test_web_search_service_with_mock.py
"""

from implementation.runtime.adapters.mock_web_search_adapter import (
    MockWebSearchAdapter,
)

from implementation.runtime.web_search_service import (
    WebSearchService,
)


def test_web_search_service_with_mock():

    adapter = (
        MockWebSearchAdapter()
    )

    service = (
        WebSearchService(
            adapter
        )
    )

    results = (
        service.search(
            "protein intake"
        )
    )

    assert len(results) == 1

    result = results[0]

    assert (
        "protein intake"
        in result.title.lower()
    )
