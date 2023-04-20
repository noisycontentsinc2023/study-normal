import basic
import eventasyncio
import os
import discord
from bot import get_bot

TOKEN = os.environ['TOKEN']
PREFIX = os.environ['PREFIX']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False

bot = get_bot()

def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()

    bot.run(TOKEN)

if __name__ == '__main__':
    main()
