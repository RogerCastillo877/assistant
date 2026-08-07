"""
OSEF Runtime

events.py

Runtime events and event collection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class RuntimeEvent:

    event_type: str

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )

    payload: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass(slots=True)
class EventStore:

    events: list[RuntimeEvent] = field(
        default_factory=list
    )

    def emit(
        self,
        event_type: str,
        payload: dict[str, Any] | None = None,
    ) -> RuntimeEvent:

        event = RuntimeEvent(
            event_type=event_type,
            payload=payload or {},
        )

        self.events.append(event)

        return event

    def all(self) -> list[RuntimeEvent]:

        return list(self.events)

    def clear(self) -> None:

        self.events.clear()

    def count(self) -> int:

        return len(self.events)

    def by_type(
        self,
        event_type: str,
    ) -> list[RuntimeEvent]:

        return [
            event
            for event in self.events
            if event.event_type == event_type
        ]
