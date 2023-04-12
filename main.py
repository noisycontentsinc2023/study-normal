from discord.ext import commands
from basic import easic
from huodong import huodong

bot.add_cog(basic(bot))
bot.add_cog(huodong(bot))

if __name__ == '__main__':
    bot.run(TOKEN)
