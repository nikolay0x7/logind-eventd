"""
Domain events.
"""

from __future__ import annotations

from dataclasses import dataclass

from logind_eventd.models.session import Session


@dataclass(frozen=True, slots=True)
class Event:
    """Base class for all events."""


@dataclass(frozen=True, slots=True)
class SessionEvent(Event):
    """Base class for session events."""

    session: Session


@dataclass(frozen=True, slots=True)
class SessionCreatedEvent(SessionEvent):
    """A new session appeared."""


@dataclass(frozen=True, slots=True)
class SessionRemovedEvent(Event):
    """A session disappeared."""

    session_id: str


@dataclass(frozen=True, slots=True)
class PrepareForSleepEvent(Event):
    """PrepareForSleep signal."""

    sleeping: bool
