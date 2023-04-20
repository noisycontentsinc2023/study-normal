import basic
import eventasyncio
import os
from bot import get_bot

TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False

def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()
    bot = get_bot()
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
