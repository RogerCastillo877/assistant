from implementation.runtime.engine import bootstrap


def test_runtime_bootstrap():

    runtime = bootstrap()

    assert runtime.project is not None

    assert runtime.project.loaded is True

    assert len(runtime.project.missions) == 1

    assert len(runtime.project.agents) == 1

    assert len(runtime.project.workflows) == 1

    assert len(runtime.project.capabilities) == 1

    assert len(runtime.project.skills) == 1

    assert len(runtime.project.tools) == 1

    assert len(runtime.project.resources) == 1

    assert len(runtime.project.memory) == 1

    assert len(runtime.project.knowledge) == 1


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
