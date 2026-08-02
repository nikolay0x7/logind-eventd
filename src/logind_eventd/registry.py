"""
Session registry.
"""

from __future__ import annotations

from logind_eventd.models.session import Session
from logind_eventd.event_dispatcher import EventDispatcher
from logind_eventd.events import (
    SessionCreatedEvent,
    SessionRemovedEvent,
)
from logind_eventd.plugins.base import Plugin

class SessionRegistry(Plugin):
    """Keep track of known sessions."""
    name = "session_registry"

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def register(
        self,
        dispatcher: EventDispatcher,
    ) -> None:
        """Register event handlers."""

        dispatcher.subscribe(
            SessionCreatedEvent,
            self._on_session_created,
        )

        dispatcher.subscribe(
            SessionRemovedEvent,
            self._on_session_removed,
        )

    def _on_session_created(
        self,
        event: SessionCreatedEvent,
    ) -> None:
        """Handle SessionCreatedEvent."""

        self.add(
            event.session,
        )


    def _on_session_removed(
        self,
        event: SessionRemovedEvent,
    ) -> None:
        """Handle SessionRemovedEvent."""

        self.remove(
            event.session_id,
        )

    def add(self, session: Session) -> None:
        """Add or replace a session."""

        self._sessions[session.id] = session

    def remove(self, session_id: str) -> None:
        """Remove a session."""

        self._sessions.pop(session_id, None)

    def get(self, session_id: str) -> Session | None:
        """Return a session."""

        return self._sessions.get(session_id)

    def clear(self) -> None:
        """Remove all sessions."""

        self._sessions.clear()

    @property
    def sessions(self) -> tuple[Session, ...]:
        """Return all sessions."""

        return tuple(self._sessions.values())

    def __len__(self) -> int:
        return len(self._sessions)
