from basic import easic
from event1 import event1

bot.add_cog(basic(bot))
bot.add_cog(event1(bot))

if __name__ == '__main__':
    bot.run(TOKEN)
