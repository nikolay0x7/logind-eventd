"""
Immutable representation of a systemd-logind session.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Session:
    """Snapshot of a logind session."""

    id: str
    uid: int
    user: str

    seat: str | None = None
    tty: str | None = None
    display: str | None = None

    remote: bool = False
    active: bool = False

    class_name: str = "user"
