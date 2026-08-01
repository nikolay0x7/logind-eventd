"""
Core event definitions.

All events emitted inside logind-eventd inherit from Event.

Events are immutable and transport only data.
"""

from __future__ import annotations

from dataclasses import dataclass

from logind_eventd.models.session import Session


@dataclass(frozen=True, slots=True)
class Event:
    """Base class for all events."""


@dataclass(frozen=True, slots=True)
class SessionEvent(Event):
    """Base class for events related to a logind session."""

    session: Session
