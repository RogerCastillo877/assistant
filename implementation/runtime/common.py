"""
OSEF Runtime

common.py

Shared utility functions used by all runtime validators.

This module MUST NOT contain OSEF business logic.

Responsibilities

- File loading
- File discovery
- Path utilities
- Safe parsing
- Generic dictionary traversal

Everything in this module should be reusable outside OSEF.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Generator

import json
import yaml


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RUNTIME_ROOT.parent


def get_runtime_root() -> Path:
    """Return the runtime root directory."""
    return RUNTIME_ROOT


def get_project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


# ---------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------

def find_yaml_files(root: Path) -> list[Path]:
    """Return every YAML file below root."""
    return sorted(root.rglob("*.yaml"))


def find_json_files(root: Path) -> list[Path]:
    """Return every JSON file below root."""
    return sorted(root.rglob("*.json"))


# ---------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------

def load_yaml(path: Path) -> dict[str, Any]:
    """Safely load a YAML file."""

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:

        data = yaml.safe_load(f)

    return data or {}


def load_json(path: Path) -> dict[str, Any]:
    """Safely load a JSON file."""

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    return data or {}


# ---------------------------------------------------------------------
# Saving
# ---------------------------------------------------------------------

def save_yaml(path: Path, data: dict[str, Any]) -> None:

    with path.open(
        "w",
        encoding="utf-8"
    ) as f:

        yaml.safe_dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True
        )


def save_json(path: Path, data: dict[str, Any]) -> None:

    with path.open(
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def is_yaml(path: Path) -> bool:
    return path.suffix.lower() in (
        ".yaml",
        ".yml"
    )


def is_json(path: Path) -> bool:
    return path.suffix.lower() == ".json"


# ---------------------------------------------------------------------
# Dictionary traversal
# ---------------------------------------------------------------------

def walk(
    node: Any
) -> Generator[Any, None, None]:
    """
    Recursively iterate every node inside a nested
    dict/list structure.
    """

    yield node

    if isinstance(node, dict):

        for value in node.values():
            yield from walk(value)

    elif isinstance(node, list):

        for item in node:
            yield from walk(item)


# ---------------------------------------------------------------------
# Generic search
# ---------------------------------------------------------------------

def find_objects_with_key(
    data: Any,
    key: str
) -> list[dict]:

    matches = []

    for node in walk(data):

        if isinstance(node, dict):

            if key in node:
                matches.append(node)

    return matches
