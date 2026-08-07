from implementation.runtime.loader import load_project

from implementation.runtime.registry import RuntimeRegistry


def test_build_registry():

    project = load_project()

    registry = RuntimeRegistry.build(project)

    assert registry.get_mission("learning") is not None

    assert registry.get_agent("planner") is not None

    assert registry.get_workflow("learning-workflow") is not None

    assert registry.get_capability("planning") is not None

    assert registry.get_skill("search") is not None

    assert registry.get_tool("web-search") is not None

    assert registry.get_resource("knowledge-base") is not None

    assert registry.get_memory("semantic-memory") is not None

    assert registry.get_knowledge("search-best-practices") is not None
