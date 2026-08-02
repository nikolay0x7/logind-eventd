"""
Load session objects from systemd-logind.
"""

from __future__ import annotations

import asyncio

from logind_eventd.bus.constants import BUS_NAME
from logind_eventd.bus.system import SystemBus
from logind_eventd.models.session import Session


class SessionLoader:
    """Load Session objects from systemd-logind."""

    SESSION_INTERFACE = "org.freedesktop.login1.Session"

    def __init__(
        self,
        system_bus: SystemBus,
    ) -> None:
        self._system_bus = system_bus

    async def load(
        self,
        object_path: str,
    ) -> Session:
        """Load a Session from its object path."""

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

        interface = proxy.get_interface(
            self.SESSION_INTERFACE,
        )

        (
            session_id,
            user_info,
            seat_info,
            active,
            remote,
            class_name,
            session_type,
            tty,
            display,
            user_name,
        ) = await asyncio.gather(
            interface.get_id(),
            interface.get_user(),
            interface.get_seat(),
            interface.get_active(),
            interface.get_remote(),
            interface.get_class(),
            interface.get_type(),
            interface.get_tty(),
            interface.get_display(),
            interface.get_name(),
        )

        uid = user_info[0]

        seat = seat_info[0] or None

        return Session(
            id=session_id,
            uid=uid,
            user=user_name,
            seat=seat,
            tty=tty or None,
            display=display or None,
            remote=remote,
            active=active,
            class_name=class_name,
            session_type=session_type or None,
        )
