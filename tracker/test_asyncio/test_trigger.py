import asyncio

# Create an asyncio Event
trigger = asyncio.Event()

async def waiter():
    print("Waiting for the event to be set...")
    await trigger.wait()
    print("Event has been set! Continuing execution...")

async def setter():
    print("Setting the event in 2 seconds...")
    await asyncio.sleep(2)
    trigger.set()
    print("Event has been set.")

async def main():
    # Run the waiter and setter coroutines concurrently
    await asyncio.gather(waiter(), setter())

# Run the main coroutine
asyncio.run(main())