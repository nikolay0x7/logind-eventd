"""
Session registry.
"""

from __future__ import annotations

from logind_eventd.models.session import Session


class SessionRegistry:
    """Keep track of known sessions."""

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

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
