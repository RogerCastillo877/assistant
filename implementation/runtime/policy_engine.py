"""
OSEF Runtime

policy_engine.py

Policy enforcement layer.
"""

from __future__ import annotations

from implementation.runtime.registry import (
    RuntimeRegistry,
)


class PolicyEngine:

    def __init__(
        self,
        registry: RuntimeRegistry,
    ) -> None:

        self.registry = registry

    def enforce_workflow(
        self,
        workflow,
        context,
    ) -> bool:

        return True
