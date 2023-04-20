import basic
import eventasyncio
import asyncio
import os
from bot import get_bot

TOKEN = os.environ['TOKEN']

async def main():
    bot = get_bot()

    basic.setup(bot)
    eventasyncio.setup(bot)

    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
