import discord
from discord.ext import tasks, commands
from discord.utils import get
from dotenv import load_dotenv
import asyncio
import os
import random
import googletrans 
from discord import Embed


translator = googletrans.Translator()
intents = discord.Intents.default()
intents.members = True

# Create a dictionary of flag emojis and their corresponding language codes
flag_emoji_dict = {
"🇺🇸": "en",
"🇩🇪": "de",
"🇫🇷": "fr",
"🇪🇸": "es",
"🇮🇹": "it",
"🇵🇹": "pt",
"🇷🇺": "ru",
"🇦🇱": "sq",
"🇸🇦": "ar",
"🇧🇦": "bs",
"🇨🇳": "zh-CN",
"🇹🇷": "tr",
"🇵🇱": "pl",
"🇳🇴": "no",
"🇸🇬": "sv",
"🇯🇵": "ja",
"🇰🇷": "ko",
}

#For a more secure, we loaded the .env file and assign the token value to a variable 
TOKEN = os.environ['TOKEN']
PREFIX = os.environ['PREFIX']

intents=discord.Intents.all()
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

#------------------------------------------------번역기------------------------------------------------------#

@bot.event
async def on_reaction_add(reaction, user):
  
    # Check if the reaction is a flag emoji
    if reaction.emoji in flag_emoji_dict:
        # Get the language code corresponding to the flag emoji
        lang_code = flag_emoji_dict[reaction.emoji]
        # Get the original message
        message = reaction.message
        # Translate the message to the desired language
        detected_lang = translator.detect(message.content)
        translated_message = translator.translate(message.content, dest=lang_code).text
        pronunciation_message = translator.translate(message.content, dest=lang_code).pronunciation

        embed = Embed(title='번역된 문장', description=f'{translated_message}', color=0x00ff00)
        embed.add_field(name="원문", value=message.content, inline=False)
        embed.add_field(name="발음", value=pronunciation_message, inline=False)
       # await reaction.message.channel.send(content=f'{reaction.user.mention}',embed=embed)
        await reaction.message.channel.send(content=f'{user.mention}',embed=embed)

#------------------------------------------------검색------------------------------------------------------#
@bot.event
async def on_message(message):
    if message.content.startswith("!로또"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6] # 배열크기 선언해줌
        count = 0
        for i in range(0, 6):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title=" 망령의 추천 번호는!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)
        
#------------------------------------------------검색------------------------------------------------------# 
@bot.event
async def on_message(message):
if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

#Run the bot
bot.run(TOKEN)
    

