"""
OSEF Runtime

runtime_hooks.py

Runtime hook definitions.
"""

from __future__ import annotations

from typing import Protocol


class RuntimeHook(Protocol):

    def execute(
        self,
        payload: dict,
    ) -> None:
        ...
