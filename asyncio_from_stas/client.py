import asyncio

import aiohttp

url1 = 'http://0.0.0.0:8080/1/'


async def gen(session, n):
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(session.get(url1)))
    for task in tasks:
        yield await task


async def main():
    session = aiohttp.ClientSession()
    async for r in gen(session, 10):
        response_data1 = r
        print(await response_data1.json())

    await session.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())