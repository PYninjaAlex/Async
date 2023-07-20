import asyncio


max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

async def counter_1():
    nums = [i for i in range(1, max_counts["Counter 1"] + 1)]
    for num in nums:
        print("Counter 1:", num)
        await asyncio.sleep(0)

async def counter_2():
    nums = [i for i in range(1, max_counts["Counter 2"] + 1)]
    for num in nums:
        print("Counter 2:", num)
        await asyncio.sleep(0)

async def main():
    coro1 = asyncio.create_task(counter_1())
    coro2 = asyncio.create_task(counter_2())
    await coro1
    await coro2

if __name__ == "__main__":
    asyncio.run(main())    
