"""
OSEF Runtime

engine.py

Runtime bootstrap and initialization.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.loader import load_project
from implementation.runtime.project import Project
from implementation.runtime.registry import RuntimeRegistry
from implementation.runtime.resolver import RuntimeResolver
from implementation.runtime.errors import ResolutionError
from implementation.runtime.executor import WorkflowExecutor


@dataclass(slots=True)
class RuntimeEngine:
    """
    Main runtime container.

    Holds the loaded project, entity registry
    and dependency resolver.
    """

    project: Project

    registry: RuntimeRegistry

    resolver: RuntimeResolver

    executor: WorkflowExecutor

def bootstrap(
    validate: bool = True,
) -> RuntimeEngine:
    """
    Bootstraps the OSEF runtime.

    Steps:

    1. Load project artifacts.
    2. Build registry indexes.
    3. Create dependency resolver.
    4. Validate references.
    5. Return runtime engine.
    """

    project = load_project()

    registry = RuntimeRegistry.build(project)

    resolver = RuntimeResolver(registry)

    executor = WorkflowExecutor(registry)

    if validate:

        report = resolver.validate()

        if not report.valid:

            raise ResolutionError(
                "\n".join(report.errors)
            )

    return RuntimeEngine(
        project=project,
        registry=registry,
        resolver=resolver,
        executor=executor,
    )
