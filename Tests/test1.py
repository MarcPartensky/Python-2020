import asyncio

q = asyncio.Queue(10)

async def test():
    await print(1)

q.put_nowait(test)
q.put_nowait(test)

async def main():
    while not q.empty():
        a = await q.get()
        print(await a)

asyncio.run(main())

