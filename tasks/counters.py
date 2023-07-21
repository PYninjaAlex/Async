import asyncio


max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}  

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

async def counter(counter_name: str, delay: int) -> None:
    for num in range(1, max_counts[counter_name] + 1):
        await asyncio.sleep(delay)
        print(f"{counter_name}: {num}")

async def main():
    coro1 = asyncio.create_task(counter("Counter 1", delays["Counter 1"]))
    coro2 = asyncio.create_task(counter("Counter 2", delays["Counter 2"]))
    coro3 = asyncio.create_task(counter("Counter 3", delays["Counter 3"]))
    await coro1
    await coro2
    await coro3

if __name__ == "__main__":
    asyncio.run(main())    
