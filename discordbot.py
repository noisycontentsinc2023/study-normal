import discord
import urllib.request
import asyncio
import threading
import os
import random
import googletrans 
import requests
import re
import time
import datetime
import uuid
import string

from bs4 import BeautifulSoup
from discord import Embed
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get
from dataclasses import dataclass
from typing import List, Dict, Optional
from discord.ext.commands import when_mentioned_or, CommandNotFound, has_permissions, NoPrivateMessage, Bot, \
    ExpectedClosingQuoteError
from collections import defaultdict

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
polls = {}

@bot.command(name='vote')
async def create_poll(ctx, *, args):
    if not args:
        embed = discord.Embed(title='Vote Help')
        embed.add_field(name='Like/Dislike', value='!vote title')
        embed.add_field(name='Multiple options (max 9)', value='!vote title, option1, option2, ..., option9')
        await ctx.send(embed=embed)
    else:
        parts = [part.strip() for part in args.split(',')]
        title = parts[0]
        options = parts[1:]

        if len(options) > 9:
            await ctx.send('You can only have up to 9 options.')
            return

        embed = discord.Embed(title=title)
        if not options:
            message = await ctx.send(embed=embed)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        else:
            emoji_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
            s = ''
            emoji = iter(emoji_list)
            for option in options:
                try:
                    s += f'{next(emoji)} {option}\n'
                except StopIteration:
                    await ctx.send('You can only have up to 9 options.')
                    return

            embed.add_field(name='Options', value=s)
            embed.add_field(name='Current Voting Status', value='No votes yet')

            poll_message = await ctx.send('Poll created!', embed=embed)

            for i in range(len(options)):
                await poll_message.add_reaction(emoji_list[i])

            poll_info = {'title': title, 'options': options, 'votes': {option: 0 for option in options}, 'closed': False}
            polls[poll_message.id] = poll_info

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    poll_id = None
    for message_id, poll in polls.items():
        if message_id == reaction.message.id:
            poll_id = message_id
            break

    if not poll_id:
        return

    option = None
    for i, emoji in enumerate(poll['options']):
        if str(reaction.emoji) == f'{i+1}\u20e3':
            option = emoji
            break

    if not option:
        return

    poll['votes'][option] += 1

    poll_message = await reaction.message.channel.fetch_message(poll_id)

    poll_results = ''
    for i, option in enumerate(poll['options']):
        poll_results += f'{i+1}\u20e3 {option}: {poll["votes"][option]} votes\n'

    poll_embed = discord.Embed(title=poll['title'])
    poll_embed.add_field(name='Options', value=poll_results)
    poll_embed.add_field(name='Current Voting Status', value='Votes in progress')

    await poll_message.edit(embed=poll_embed)
                
@bot.command(name='닫기')
async def close_poll(ctx, poll_id: str):
    """
    Close a poll and display the results
    :param poll_id: ID of the poll to close
    """
    # Check if poll exists
    if poll_id not in polls:
        await ctx.send(f'No poll with ID {poll_id} exists.')
        return

    poll_data = polls[poll_id]

    # Check if poll is closed
    if poll_data['closed']:
        await ctx.send(f'The poll with ID {poll_id} is already closed.')
        return

    # Get poll message
    poll_message_id = poll_data['message_id']
    poll_message = await ctx.channel.fetch_message(poll_message_id)

    # Get poll results
    poll_results = {}
    for option in poll_data['options']:
        poll_results[option] = 0
    for reaction in poll_message.reactions:
        emoji = get_emoji(reaction.emoji)
        if emoji in poll_data['options']:
            async for user in reaction.users():
                if user != bot.user:
                    poll_data['votes'][user.id] = emoji  # store user's vote
                    poll_results[emoji] += 1

    # Update poll data
    poll_data['closed'] = True

    # Create result message
    result_message = f'Poll results for {poll_data["title"]}:\n'
    for option in poll_data['options']:
        count = poll_results[option]
        result_message += f'{option}: {count} vote(s)\n'

    # Create embed
    embed = discord.Embed(title=f'Poll results for {poll_id}', description=result_message)

    # Send result message as an embed
    await ctx.send(embed=embed)
    
#Run the bot
bot.run(TOKEN)

