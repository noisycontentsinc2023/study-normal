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

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

if __name__ == '__main__':
    bot.load_extension('basic')
    bot.load_extension('eventasyncio')
    bot.run(TOKEN)
