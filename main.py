from discord.ext import commands
from basic import easic
from slotm import slotm

bot.add_cog(basic(bot))
bot.add_cog(slotm(bot))

if __name__ == '__main__':
    bot.run(TOKEN)
