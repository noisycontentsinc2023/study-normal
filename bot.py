from discord.ext import commands

PREFIX = os.environ['PREFIX']
prefix = !
bot = commands.Bot(command_prefix=prefix, intents=intents)

def get_bot():
    return bot
