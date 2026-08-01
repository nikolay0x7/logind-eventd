"""
Simple synchronous event dispatcher.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any

from logind_eventd.events import Event


class EventDispatcher:
    """Dispatch domain events to subscribers."""

    def __init__(self) -> None:
        self._handlers: dict[type[Event], list[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(
        self,
        event_type: type[Event],
        handler: Callable[[Any], None],
    ) -> None:
        """Register an event handler."""

        self._handlers[event_type].append(handler)

    def emit(self, event: Event) -> None:
        """Dispatch an event."""

        for handler in self._handlers[type(event)]:
            handler(event)
