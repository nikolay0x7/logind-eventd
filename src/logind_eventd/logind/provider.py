"""
systemd-logind provider.
"""

from __future__ import annotations

import asyncio

from dbus_next.aio import ProxyInterface

from logind_eventd.bus.constants import (
    BUS_NAME,
    MANAGER_INTERFACE,
    MANAGER_PATH,
)
from logind_eventd.bus.system import SystemBus
from logind_eventd.event_dispatcher import EventDispatcher
from logind_eventd.events import (
    PrepareForSleepEvent,
    SessionCreatedEvent,
    SessionRemovedEvent,
)
from logind_eventd.logind.loader import SessionLoader
from logind_eventd.logind.mapper import map_session
from logind_eventd.models.session import Session


class LogindProvider:
    """Access to the systemd-logind D-Bus API."""

    def __init__(
        self,
        system_bus: SystemBus,
        dispatcher: EventDispatcher,
    ) -> None:
        self._system_bus = system_bus
        self._dispatcher = dispatcher

        self._loader = SessionLoader(
            system_bus,
        )

        self._manager: ProxyInterface | None = None

    async def connect(self) -> None:
        """Connect to systemd-logind."""

        bus = await self._system_bus.connect()

        introspection = await bus.introspect(
            BUS_NAME,
            MANAGER_PATH,
        )

        proxy = bus.get_proxy_object(
            BUS_NAME,
            MANAGER_PATH,
            introspection,
        )

        self._manager = proxy.get_interface(
            MANAGER_INTERFACE,
        )

        self.manager.on_prepare_for_sleep(
            self._prepare_for_sleep,
        )

        self.manager.on_session_new(
            self._session_new,
        )

        self.manager.on_session_removed(
            self._session_removed,
        )

    async def list_sessions(self) -> list[Session]:
        """Return all active logind sessions."""

        sessions = await self.manager.call_list_sessions()

        return [
            map_session(entry)
            for entry in sessions
        ]

    def _prepare_for_sleep(
        self,
        sleeping: bool,
    ) -> None:
        """Forward PrepareForSleep signal."""

        self._dispatcher.emit(
            PrepareForSleepEvent(
                sleeping=sleeping,
            )
        )

    def _session_new(
        self,
        session_id: str,
        object_path: str,
    ) -> None:
        """Handle SessionNew signal."""

        asyncio.create_task(
            self._handle_session_new(
                session_id,
                object_path,
            )
        )

    async def _handle_session_new(
        self,
        session_id: str,
        object_path: str,
    ) -> None:
        """Process a newly created session."""

        session = await self._loader.load(
            object_path,
        )

        self._dispatcher.emit(
            SessionCreatedEvent(
                session=session,
            )
        )

    def _session_removed(
        self,
        session_id: str,
        object_path: str,
    ) -> None:
        """Handle SessionRemoved signal."""

        self._dispatcher.emit(
            SessionRemovedEvent(
                session_id=session_id,
            )
        )

    @property
    def manager(self) -> ProxyInterface:
        """Return the logind manager interface."""

        if self._manager is None:
            raise RuntimeError(
                "LogindProvider is not connected."
            )

        return self._manager
