import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello, world!")

async def main(loop):
    # Schedule the coroutine to run
    future = asyncio.ensure_future(say_hello(), loop=loop)

    # Do other things while waiting for the coroutine to complete
    await asyncio.sleep(0.5)
    print("Doing other things...")

    # Wait for the coroutine to complete
    await future

#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))