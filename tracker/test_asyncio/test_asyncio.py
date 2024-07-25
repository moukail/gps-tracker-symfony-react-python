import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    await nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".
    await asyncio.Future()  # Run forever

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Received exit, exiting")