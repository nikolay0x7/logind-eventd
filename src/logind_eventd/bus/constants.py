"""
Constants used for communicating with systemd-logind.
"""

from __future__ import annotations

BUS_NAME = "org.freedesktop.login1"

MANAGER_PATH = "/org/freedesktop/login1"

MANAGER_INTERFACE = "org.freedesktop.login1.Manager"

SESSION_INTERFACE = "org.freedesktop.login1.Session"

SEAT_INTERFACE = "org.freedesktop.login1.Seat"

USER_INTERFACE = "org.freedesktop.login1.User"

PROPERTIES_INTERFACE = "org.freedesktop.DBus.Properties"

OBJECT_MANAGER_INTERFACE = "org.freedesktop.DBus.ObjectManager"
