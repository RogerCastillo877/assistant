def assert_registry_loaded(
    registry,
):

    assert len(
        registry.missions
    ) >= 1

    assert len(
        registry.agents
    ) >= 1

    assert len(
        registry.workflows
    ) >= 1

    assert len(
        registry.capabilities
    ) >= 1

    assert len(
        registry.skills
    ) >= 1

    assert len(
        registry.tools
    ) >= 1
