"""
Load session objects from systemd-logind.
"""

from __future__ import annotations

from dbus_next.aio import ProxyInterface

from logind_eventd.bus.constants import BUS_NAME
from logind_eventd.bus.system import SystemBus


class SessionLoader:
    """Load logind session objects."""

    SESSION_INTERFACE = "org.freedesktop.login1.Session"

    def __init__(
        self,
        system_bus: SystemBus,
    ) -> None:
        self._system_bus = system_bus

    async def load(
        self,
        object_path: str,
    ) -> ProxyInterface:
        """Return the D-Bus interface for a session."""

        bus = await self._system_bus.connect()

        introspection = await bus.introspect(
            BUS_NAME,
            object_path,
        )

        proxy = bus.get_proxy_object(
            BUS_NAME,
            object_path,
            introspection,
        )

        return proxy.get_interface(
            self.SESSION_INTERFACE,
        )
