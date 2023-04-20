import basic
import eventasyncio
import asyncio

async def main():
    basic.run_basic()
    bot = eventasyncio.run_eventasyncio()
    await bot.start("TOKEN")

if __name__ == '__main__':
    asyncio.run(main())
