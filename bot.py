from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=intents)

def get_bot():
    return bot
