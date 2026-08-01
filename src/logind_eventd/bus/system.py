"""
System D-Bus connection.
"""

from __future__ import annotations

from dbus_next import BusType
from dbus_next.aio import MessageBus


class SystemBus:
    """Wrapper around the system D-Bus connection."""

    def __init__(self) -> None:
        self._bus: MessageBus | None = None

    async def connect(self) -> MessageBus:
        """Connect to the system bus."""
        if self._bus is None:
            self._bus = await MessageBus(
                bus_type=BusType.SYSTEM,
            ).connect()

        return self._bus

    @property
    def bus(self) -> MessageBus | None:
        """Return the current connection."""
        return self._bus
