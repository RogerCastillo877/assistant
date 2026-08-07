from implementation.runtime.loader import load_project

from implementation.runtime.registry import RuntimeRegistry

from implementation.runtime.resolver import RuntimeResolver


def test_resolver_validation():

    project = load_project()

    registry = RuntimeRegistry.build(project)

    resolver = RuntimeResolver(registry)

    report = resolver.validate()

    assert report.valid is True

    assert report.errors == []
