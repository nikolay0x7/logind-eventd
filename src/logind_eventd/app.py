"""
Application runtime.
"""

from __future__ import annotations

import asyncio

from logind_eventd.bus.system import SystemBus
from logind_eventd.event_dispatcher import EventDispatcher
from logind_eventd.events import PrepareForSleepEvent
from logind_eventd.log import get_logger
from logind_eventd.logind.provider import LogindProvider
from logind_eventd.plugins.logger import LoggerPlugin
from logind_eventd.plugins.manager import PluginManager
from logind_eventd.registry import SessionRegistry
from logind_eventd.version import __version__


class Application:
    """Main application."""

    def __init__(self) -> None:
        self._log = get_logger(__name__)
        self._shutdown = asyncio.Event()

        self._dispatcher = EventDispatcher()

        self._plugins = PluginManager(
            self._dispatcher,
        )

        self._registry = SessionRegistry()

        self._plugins.register(
            self._registry,
        )

        self._plugins.register(
            LoggerPlugin(),
        )

    async def run(self) -> None:
        """Run the application."""

        self._log.info("Starting logind-eventd %s", __version__)
        self._log.info("Application initialized.")

        system_bus = SystemBus()

        provider = LogindProvider(
            system_bus,
            self._dispatcher,
        )

        await provider.connect()

        self._log.info("Connected to systemd-logind.")

        sessions = await provider.list_sessions()

        self._log.info(
            "Found %d active session(s).",
            len(sessions),
        )

        for session in sessions:
            self._registry.add(session)

            self._log.info(
                "%s",
                session,
            )

        self._log.info(
            "Session registry initialized with %d session(s).",
            len(self._registry),
        )

        self._log.info("Waiting for events...")

        try:
            await self._shutdown.wait()

        finally:
            self._log.info("Application stopped.")

    def shutdown(self) -> None:
        """Request application shutdown."""

        self._log.info("Shutdown requested.")
        self._shutdown.set()
