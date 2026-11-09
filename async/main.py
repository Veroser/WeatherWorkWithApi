import asyncio

import aiohttp

from weather import fetch_wether

async def main() -> None:
    t = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=t) as session:
        forecast = await fetch_wether(session, city="Irkutsk")
    print(forecast)


if __name__ == "__main__":
    asyncio.run(main())