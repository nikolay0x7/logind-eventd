from __future__ import annotations

from logind_eventd.event_dispatcher import EventDispatcher
from logind_eventd.plugins.base import Plugin


class PluginManager:
    """Manage loaded plugins."""

    def __init__(
        self,
        dispatcher: EventDispatcher,
    ) -> None:
        self._dispatcher = dispatcher
        self._plugins: list[Plugin] = []

    def register(
        self,
        plugin: Plugin,
    ) -> None:
        plugin.register(self._dispatcher)
        self._plugins.append(plugin)

    @property
    def plugins(self) -> tuple[Plugin, ...]:
        return tuple(self._plugins)
