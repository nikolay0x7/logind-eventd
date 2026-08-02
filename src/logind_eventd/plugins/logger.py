from __future__ import annotations

import logging

from logind_eventd.event_dispatcher import EventDispatcher
from logind_eventd.events import (
    PrepareForSleepEvent,
    SessionCreatedEvent,
)
from logind_eventd.plugins.base import Plugin


class LoggerPlugin(Plugin):
    """Simple logging plugin."""

    name = "logger"

    def __init__(self) -> None:
        self._log = logging.getLogger(__name__)

    def register(
        self,
        dispatcher: EventDispatcher,
    ) -> None:
        dispatcher.subscribe(
            PrepareForSleepEvent,
            self._on_prepare_for_sleep,
        )

        dispatcher.subscribe(
            SessionCreatedEvent,
            self._on_session_created,
        )

    def _on_prepare_for_sleep(
        self,
        event: PrepareForSleepEvent,
    ) -> None:
        self._log.info(
            "PrepareForSleep: sleeping=%s",
            event.sleeping,
        )

    def _on_session_created(
        self,
        event: SessionCreatedEvent,
    ) -> None:
        """Log SessionCreated events."""

        self._log.info(
            "SessionCreated: %s",
            event.session,
        )
