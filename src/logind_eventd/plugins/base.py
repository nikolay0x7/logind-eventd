from __future__ import annotations

from abc import ABC, abstractmethod

from logind_eventd.event_dispatcher import EventDispatcher


class Plugin(ABC):
    """Base class for all plugins."""

    name = "plugin"

    @abstractmethod
    def register(
        self,
        dispatcher: EventDispatcher,
    ) -> None:
        """Register event handlers."""
