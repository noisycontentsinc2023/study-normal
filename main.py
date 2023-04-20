import asyncio
from basic import run_basic
from eventasyncio import run_eventasyncio

TOKEN = os.environ['TOKEN']

async def main():
    bot = run_basic()
    await bot.login(TOKEN)
    await run_eventasyncio()
    await bot.connect()

if __name__ == '__main__':
    asyncio.run(main())
