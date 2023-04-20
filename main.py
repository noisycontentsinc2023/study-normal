import basic
import eventasyncio
import os
import discord
from bot import get_bot

TOKEN = os.environ['TOKEN']

async def main():
    basic.get_bot()
    eventasyncio.get_bot()
    bot = get_bot()
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
