import asyncio
from time import sleep

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print("done fetching'")
    return {'data': 1}
    
async def print_numbers():
    for i in range(5):
        print(i)
    await asyncio.sleep(5)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)

    # await fetch_data()
    await task2

asyncio.run(main())