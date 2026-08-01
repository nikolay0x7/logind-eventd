from __future__ import annotations

import asyncio

from logind_eventd.app import Application


def main() -> None:
    asyncio.run(Application().run())


if __name__ == "__main__":
    main()
