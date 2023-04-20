import basic
import eventasyncio
import asyncio
import os
from bot import get_bot

TOKEN = os.environ['TOKEN']

async def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()
    bot = get_bot()
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
