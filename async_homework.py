import asyncio


async def print_odd_number():
    for i in range(0, 11):
        if i % 2 == 1:
            print(f"Odd number: {i}")
        await asyncio.sleep(1)


async def print_even_number():
    for i in range(0, 11):
        if i % 2 == 0:
            print(f"Even number: {i}")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(print_odd_number(), print_even_number())


asyncio.run(main())
