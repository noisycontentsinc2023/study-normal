from discord.ext import commands

PREFIX = os.environ['PREFIX']
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

def get_bot():
    return bot
