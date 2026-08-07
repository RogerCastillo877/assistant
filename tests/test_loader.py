from implementation.runtime.loader import load_project


def test_load_project():

    project = load_project()

    assert project.loaded is True

    assert len(project.missions) == 1

    assert len(project.agents) == 1

    assert len(project.workflows) == 1

    assert len(project.capabilities) == 1

    assert len(project.skills) == 1

    assert len(project.tools) == 1

    assert len(project.resources) == 1

    assert len(project.memory) == 1

    assert len(project.knowledge) == 1


def test_project_entity_count():

    project = load_project()

    assert project.entity_count == 9
