from basic import Basic
from event1 import Event1

if __name__ == '__main__':
    bot.add_cog(Basic(bot))
    bot.add_cog(Event1(bot))
    bot.run(TOKEN)
