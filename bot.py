import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=intents)

def get_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.typing = False
    intents.presences = False

    return commands.Bot(command_prefix=prefix, intents=intents)
