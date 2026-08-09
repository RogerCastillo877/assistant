"""
OSEF Runtime

test_mock_web_search_adapter.py
"""

from implementation.runtime.adapters.mock_web_search_adapter import (
    MockWebSearchAdapter,
)


def test_mock_web_search_adapter():

    adapter = (
        MockWebSearchAdapter()
    )

    results = (
        adapter.search(
            "strength training"
        )
    )

    assert len(results) == 1

    result = results[0]

    assert (
        result.title
        == "Mock Result for strength training"
    )

    assert (
        result.source
        == "mock"
    )

    assert (
        result.score
        == 1.0
    )
