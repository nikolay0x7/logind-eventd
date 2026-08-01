"""
Logging utilities for logind-eventd.
"""

from __future__ import annotations

import logging

_CONFIGURED = False


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Logging is configured only once, regardless of how many times this
    function is called.
    """
    global _CONFIGURED

    if not _CONFIGURED:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        )
        _CONFIGURED = True

    return logging.getLogger(name)
