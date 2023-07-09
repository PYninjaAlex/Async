import asyncio

async def generate(nums):
    for num in nums:
        print(num)

async def main():
    numbers = [num for num in range(10)]
    await generate(numbers)

asyncio.run(main())