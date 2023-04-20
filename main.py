import basic
import eventasyncio
import os
import discord
from bot import get_bot

TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False

async def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()
    bot = get_bot(intents=intents)
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
