import basic
import eventasyncio
import asyncio
from bot import get_bot

async def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()
    bot = get_bot()
    await bot.start("TOKEN")

if __name__ == '__main__':
    asyncio.run(main())
