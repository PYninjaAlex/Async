import asyncio
import time

async def first():
    await asyncio.sleep(1)
    print("Coroutine_1 is done")

async def second():
    await asyncio.sleep(1)
    print("Coroutine_2 is done")

async def third():
    await asyncio.sleep(1)
    print("Coroutine_3 is done")

async def main():
    await first()
    await second()
    await third()

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main()) 
    
