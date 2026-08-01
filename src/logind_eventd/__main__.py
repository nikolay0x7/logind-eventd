from __future__ import annotations

import asyncio
import signal

from logind_eventd.app import Application


async def _main() -> None:
    app = Application()

    loop = asyncio.get_running_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, app.shutdown)

    await app.run()


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
