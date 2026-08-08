from implementation.runtime.engine import bootstrap

from tests.common import (
    assert_registry_loaded
)

def test_runtime_bootstrap():

    runtime = bootstrap()

    assert runtime.project is not None

    assert runtime.project.loaded is True

    assert (
        "learning"
        in runtime.registry.missions
    )

    assert (
        "marketing-content"
        in runtime.registry.missions
    )

    assert_registry_loaded(
        runtime.registry
    )

def test_registry_resolution():

    runtime = bootstrap()

    registry = runtime.registry

    assert registry.get_mission("learning")

    assert registry.get_agent("planner")

    assert registry.get_workflow("learning-workflow")

    assert registry.get_capability("planning")

    assert registry.get_skill("search")

    assert registry.get_tool("web-search")

    assert registry.get_resource("knowledge-base")

    assert registry.get_memory("semantic-memory")

    assert registry.get_knowledge(
        "search-best-practices"
    )


def test_runtime_resolution():

    runtime = bootstrap()

    report = runtime.resolver.validate()

    assert report.valid

    assert len(report.errors) == 0
