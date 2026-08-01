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

    async def run(self) -> None:
        """Run the application."""
        self._log.info("Starting logind-eventd %s", __version__)
        self._log.info("Application initialized.")
        self._log.info("Waiting for events...")

        while True:
            await asyncio.sleep(3600)
