import discord
import urllib.request
import asyncio
import threading
import os
import random
import googletrans 
import requests
import re

from bs4 import BeautifulSoup
from discord import Embed
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get
from dataclasses import dataclass
from typing import List, Dict, Optional

translator = googletrans.Translator()
intents = discord.Intents.default()
intents.members = True

naver_client_id = 'iuWr9aAAyKxNnRsRSQIt'
naver_client_secret = 'bkfPugeyIa'

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

TOKEN = os.environ['TOKEN']
PREFIX = os.environ['PREFIX']

intents=discord.Intents.all()
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

baseurl = "https://studymini.com/"

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

#------------------------------------------------로또------------------------------------------------------#

@bot.command(name='로또')
async def lotto(ctx):
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
    await ctx.send(embed=embed)
        
#------------------------------------------------검색------------------------------------------------------# 

@bot.command(name='주사위')
async def dice(ctx):
    randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
    print(randomNum)
    if randomNum == 1:
        await ctx.send(embed=discord.Embed(description=':game_die: '+ ':one:'))
    if randomNum == 2:
        await ctx.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
    if randomNum ==3:
        await ctx.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
    if randomNum ==4:
        await ctx.send(embed=discord.Embed(description=':game_die: ' + ':four:'))
    if randomNum ==5:
        await ctx.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
    if randomNum ==6:
        await ctx.send(embed=discord.Embed(description=':game_die: ' + ':six: '))

#------------------------------------------------이벤트------------------------------------------------------# 

@bot.command(name='이벤트')
async def event(ctx):
        hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url='http://studymini.com'
        req=urllib.request.Request(url=url, headers=hdr)
        url_open=urllib.request.urlopen(req)
        
        bs=BeautifulSoup(url_open,'html.parser')

        #이벤트 이미지 가져오기
        vent1 = bs.select('div>h2>a')[0].get_text()
        vent11_url = bs.select('div>h2>a')[1].get('href')
        vent11 = bs.select('div>h2>a')[1].get_text()
        vent2 = bs.select('div>h2>a')[3].get_text()
        vent21_url = bs.select('div>h2>a')[4].get('href')
        vent21 = bs.select('div>h2>a')[4].get_text()
        vent3 = bs.select('div>h2>a')[6].get_text()
        vent31_url = bs.select('div>h2>a')[7].get('href')
        vent31 = bs.select('div>h2>a')[7].get_text()


        embed = discord.Embed(title="현재 진행중인 이벤트", description="자세한 정보는 홈페이지를 참고해주세요 http://studymini.com/", color=0x62c1cc)
        embed.add_field(name="이벤트 1", value=f"{vent1}\n\u200c{vent11}\n [자세히 보기]({vent11_url})", inline=True)
        embed.add_field(name="이벤트 2", value=f"{vent2}\n\u200c{vent21}\n [자세히 보기]({vent21_url})", inline=True)
        embed.add_field(name="이벤트 3", value=f"{vent3}\n\u200c{vent31}\n [자세히 보기]({vent31_url})", inline=True)

        # 가운데 정렬
        for field in embed.fields:
            field.value = f"{field.value.center(40, ' ')}"
            
        await ctx.send(embed=embed)

#------------------------------------------------클라스------------------------------------------------------# 
#------------------------------------------------검색------------------------------------------------------#

@bot.command(name='검색')
async def search(ctx, *args):
  query = ' '.join(args)
  search_url = f'https://openapi.naver.com/v1/search/webkr.json?query={query}'

  headers = {
    'X-Naver-Client-Id': 'iuWr9aAAyKxNnRsRSQIt' ,
    'X-Naver-Client-Secret': 'bkfPugeyIa'
  }
  response = requests.get(search_url, headers=headers)

  if response.status_code == 200:
    data = response.json()

    if len(data['items']) > 0:
      # Extract the top 3 search results
      results = data['items'][:3]

      # Format the results as an embedded message
      embed = discord.Embed(title=f"Search Results for \"{query}\"", color=0x0099ff)

      for result in results:
        embed.add_field(name=result['title'], value=result['link'], inline=False)

      await ctx.send(embed=embed)
    else:
      await ctx.send(f"검색결과가 없습니다 \"{query}\".")
  else:
    await ctx.send('에러가 발생했어요! 명령어를 깜빡 하신건 아닐까요?')

#------------------------------------------------투표------------------------------------------------------#  
class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="투표")
    async def create_poll(self, ctx, *, args):
        options = args.split(", ")
        if len(options) < 2:
            await ctx.send("투표 옵션은 2개 이상이어야 합니다.")
            return
        elif len(options) > 10:
            await ctx.send("투표 옵션은 10개 이하이어야 합니다.")
            return

        poll_embed = discord.Embed(title=f"📊 {options[0]}")
        for i, option in enumerate(options[1:]):
            poll_embed.add_field(name=f"{i+1}. {option}", value="\u200b", inline=False)

        poll_message = await ctx.send(embed=poll_embed)

        for i in range(1, len(options)):
            await poll_message.add_reaction(f"{i}\u20e3")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        embeds = message.embeds
        if len(embeds) == 0 or not embeds[0].title.startswith("📊"):
            return
        for field in embeds[0].fields:
            if reaction.emoji == f"{field.name.split('.')[0]}\u20e3":
                count = int(field.value.split()[0]) + 1
                field.value = f"{count}명 참여"
                new_embed = discord.Embed(title=embeds[0].title, color=embeds[0].color)
                for field in embeds[0].fields:
                    new_embed.add_field(name=field.name, value=field.value, inline=False)
                await message.edit(embed=new_embed)
                break

bot.add_cog(Poll(bot))
#Run the bot
bot.run(TOKEN)
    

