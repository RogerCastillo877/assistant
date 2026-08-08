"""
OSEF Runtime

runtime_lifecycle.py

Runtime lifecycle events.
"""

from __future__ import annotations

from collections import defaultdict

from implementation.runtime.runtime_hooks import (
    RuntimeHook,
)


class RuntimeLifecycle:

    def __init__(self) -> None:

        self._hooks: dict[
            str,
            list[RuntimeHook],
        ] = defaultdict(list)

    def register(
        self,
        event: str,
        hook: RuntimeHook,
    ) -> None:

        self._hooks[event].append(
            hook
        )

    def emit(
        self,
        event: str,
        payload: dict,
    ) -> None:

        for hook in self._hooks.get(
            event,
            [],
        ):

            hook.execute(payload)
