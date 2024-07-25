import asyncio

def callback():
    print("Callback called!")

loop = asyncio.get_event_loop()
loop.call_soon(callback)
loop.run_forever()