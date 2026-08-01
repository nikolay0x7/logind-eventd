"""
systemd-logind provider.
"""

from __future__ import annotations

from dbus_next.aio import ProxyInterface

from logind_eventd.bus.constants import (
    BUS_NAME,
    MANAGER_INTERFACE,
    MANAGER_PATH,
)
from logind_eventd.bus.system import SystemBus


class LogindProvider:
    """Access to the systemd-logind D-Bus API."""

    def __init__(self, system_bus: SystemBus) -> None:
        self._system_bus = system_bus
        self._manager: ProxyInterface | None = None

    async def connect(self) -> None:
        """Connect to systemd-logind."""

        bus = await self._system_bus.connect()

        introspection = await bus.introspect(
            BUS_NAME,
            MANAGER_PATH,
        )

        proxy = bus.get_proxy_object(
            BUS_NAME,
            MANAGER_PATH,
            introspection,
        )

        self._manager = proxy.get_interface(MANAGER_INTERFACE)

    @property
    def manager(self) -> ProxyInterface:
        """Return the logind manager interface."""

        if self._manager is None:
            raise RuntimeError("LogindProvider is not connected.")

        return self._manager
