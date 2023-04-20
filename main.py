import basic
import eventasyncio
import os
from bot import get_bot

TOKEN = os.environ['TOKEN']

def main():
    basic.run_basic()
    eventasyncio.run_eventasyncio()
    bot = get_bot()
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
