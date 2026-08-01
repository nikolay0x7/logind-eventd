"""
Application runtime.
"""

from __future__ import annotations

import asyncio

from logind_eventd.log import get_logger
from logind_eventd.version import __version__


class Application:
    """Main application."""

    def __init__(self) -> None:
        self._log = get_logger(__name__)
        self._shutdown = asyncio.Event()

    async def run(self) -> None:
        """Run the application."""
        self._log.info("Starting logind-eventd %s", __version__)
        self._log.info("Application initialized.")
        from logind_eventd.bus.system import SystemBus
        from logind_eventd.logind.provider import LogindProvider

        system_bus = SystemBus()
        provider = LogindProvider(system_bus)

        await provider.connect()

        self._log.info("Connected to systemd-logind.")
        self._log.info("Waiting for events...")

        try:
            await self._shutdown.wait()
        finally:
            self._log.info("Application stopped.")

    def shutdown(self) -> None:
        """Request application shutdown."""
        self._log.info("Shutdown requested.")
        self._shutdown.set()
