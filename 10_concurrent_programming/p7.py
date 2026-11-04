import asyncio 

async def task():
    print("Task started")
    await asyncio.sleep(3)
    print("Tast Completed")

asyncio.run(task())