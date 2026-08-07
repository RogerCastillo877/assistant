"""
OSEF Runtime

engine.py

Runtime bootstrap.
"""

from __future__ import annotations

from dataclasses import dataclass

from implementation.runtime.loader import load_project

from implementation.runtime.project import Project

from implementation.runtime.registry import RuntimeRegistry

from implementation.runtime.resolver import RuntimeResolver


@dataclass(slots=True)
class RuntimeEngine:

    project: Project

    registry: RuntimeRegistry

    resolver: RuntimeResolver


def bootstrap() -> RuntimeEngine:

    project = load_project()

    registry = RuntimeRegistry.build(project)

    resolver = RuntimeResolver(registry)

    return RuntimeEngine(
        project=project,
        registry=registry,
        resolver=resolver,
    )
