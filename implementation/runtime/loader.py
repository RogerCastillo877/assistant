"""
OSEF Runtime

loader.py

Loads an OSEF project into memory.
"""

from dataclasses import dataclass, field

from implementation.runtime.common import (
    find_yaml_files,
    load_yaml,
    get_project_root
)


@dataclass
class ProjectModel:

    config: dict = field(default_factory=dict)

    missions: list = field(default_factory=list)

    policies: list = field(default_factory=list)

    agents: list = field(default_factory=list)

    workflows: list = field(default_factory=list)

    capabilities: list = field(default_factory=list)

    skills: list = field(default_factory=list)

    tools: list = field(default_factory=list)

    resources: list = field(default_factory=list)

    memory: list = field(default_factory=list)

    knowledge: list = field(default_factory=list)

    documents: list = field(default_factory=list)

    releases: list = field(default_factory=list)

    decisions: list = field(default_factory=list)

    traceability: list = field(default_factory=list)


def load_project() -> ProjectModel:

    """
    Load every OSEF artifact into memory.
    """

    project = ProjectModel()

    #
    # implementation
    #

    return project
