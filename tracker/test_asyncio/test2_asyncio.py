import asyncio

async def my_task():
    print("Task executed")

async def repeat_task(interval):
    while True:
        await my_task()
        await asyncio.sleep(interval)

async def main():
    task_interval = 30  # Interval in seconds
    await repeat_task(task_interval)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Received exit, exiting")