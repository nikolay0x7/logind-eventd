"""
Helpers for converting systemd-logind data into domain models.
"""

from __future__ import annotations

from typing import TypeAlias

from logind_eventd.models.session import Session

SessionEntry: TypeAlias = tuple[str, int, str, str, str]


def map_session(entry: SessionEntry) -> Session:
    """Convert a ListSessions() entry into a Session model."""

    session_id, uid, user, seat, object_path = entry

    del object_path

    return Session(
        id=session_id,
        uid=uid,
        user=user,
        seat=seat or None,
    )
