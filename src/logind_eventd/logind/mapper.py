"""
Mapping helpers for Session objects.
"""

from __future__ import annotations

from logind_eventd.models.session import Session


def map_session(entry: tuple) -> Session:
    """Convert ListSessions() entry into a Session."""

    session_id, uid, user, seat, _object_path = entry

    return Session(
        id=session_id,
        uid=uid,
        user=user,
        seat=seat or None,
    )
