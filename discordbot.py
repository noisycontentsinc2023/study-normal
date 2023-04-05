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
import aiofiles
import json
import gspread

from google.oauth2 import service_account
from bs4 import BeautifulSoup
from discord import Embed
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get
from dataclasses import dataclass
from typing import List, Dict, Optional
from discord.ext.commands import check, when_mentioned_or, CommandNotFound, has_permissions, NoPrivateMessage, Bot, \
    ExpectedClosingQuoteError
from collections import defaultdict

intents = discord.Intents.default()
intents.members = True

naver_client_id = 'iuWr9aAAyKxNnRsRSQIt'
naver_client_secret = 'bkfPugeyIa'


TOKEN = os.environ['TOKEN']
PREFIX = os.environ['PREFIX']

intents=discord.Intents.all()
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

baseurl = "https://studymini.com/"

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_info = {
  "type": "service_account",
  "project_id": "thematic-bounty-382700",
  "private_key_id": "502d8dd4f035d15b57bff64ee323d544d28aedc4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQD4Kze3Hn/yxevG\nzHUklYGSDDs8qKQeyYdd1eWaR0PNKZ2+nwKFGmXGENS6vuy3U81dqI3AVgA3w6UW\nHEaVfPvc31OX5yNCIS0eQxxqWWGJJ5+MbvUC06qXi/7hCup0WK+hoqwjHtUX7AYu\nEDgtf6xd29gSvb3YXs6pvi+2tpwPt0SED6HGPU7qPRsAaPnyUsVCj/mW04ca2iea\nxMsIqxKT6ufNssiXX7qhKyziowneM0lp8BB3k2z+/FGPQOCdi/lIscC9zKbDOIcb\nOZw+B2sd2opp7Dwo3JMIkh3NJevw9hjp0+CFeqemGNsCAiSuFkvydx6BagWaWAPs\nC48nZLNZAgMBAAECggEAF3uUbTMZQZZVoAU5CPYOMY0PfmcJR6IDeX8715BKg8N+\nOhtHBGQJ8Rbm4Ehgcxz+i/AfAK4KnXw5dvkEO1E9Lmph+Tfdg9yKjchlLBGK24z4\nqZPWwpaXl/k+7BnJs2pwbROs5PJeEOJMN+fgPvrrqyJ6RNS4Pf0Dond9AZWwOQLL\naJPFZryK7Bmvtt0H8mDDWdfqmCQTtPJ9PUyDEUeenlyhuek8wH3GHcghOSlsCDF1\nW/3YXM9Vr/arE4V6hTLwXofrUnTuXTfo+DcaOIXpHqIPS+nCyzWZ0kAJ7/uKjhnN\nF4kgv9aXDX9Y7S+3irXazRhowfu2rGuPRO/2+FCuMQKBgQD+JRDctOrKvpl9zDaw\nWT2a3qmYuFf90+b8EkKsWzVBM7neEJlw1ZWxUZzkdHXwkxcM7w93BjZeXJRnI7HZ\n5sHMrRw3p7Cwy0REqC3GSbYMCIZ/98y5Ot5sOXamUCOtYnic1NG2PBzr9h94Nt7d\nZu9D7cD/kaogm9Fl9t1VMD3REQKBgQD5+vvxY0nUkzrPEHfAOnPRqt3fM9ryzmk9\n8WyffmWqaDcvb9pl1F/+/51u00cvh2Q6etvL0J850AB0AKC9QdYzIaSj4LeRNzjA\ns+K6Po5+HAYezxC1cYzFh+slAfX3gX9pa11f3aOltj4h7IXvqBB0iH4rl/i2KQ/G\ntSDa62K9yQKBgAXXEDYiKisSijBr2u3efx3p8/fAdLUug2ZTfRi819Jxv9msg/ol\nzlTOzU4qpvMqTiNL8w0HJYSxl+9u0I1zUgzEBZv5zIOjiCQTwUmHNBm+sGiMZzXy\ndl4CTAmyWb+IPcFM2qzXYMrDUyHOEP0BeooTEpZM4J3zNrKjI57rhuAhAoGAKWDC\nE1K8BdPZCC1RpSAHy8zcrPWIaGiCQx6TPFNPwMU/XTrGi9R7j1oAVTfjsJpYnNV5\nTGNb99XWPV1dPfaH3i7TcczglcjuO/eKsAlqzLUWzkK4IVCKXKgC5D1O2Yk17d03\nt4aYb/Wak0LzaJgJIUD2oYCmSoDBe8K/jX0o+wECgYBnxk9HR/23hjWaxrSnXGDB\nHxLXg9Wz5w0N+gdC/FNxknFOft+nsCMKWMocOtGYhJU3OvkTYYqL1iDsKoMb74xG\nVwB1fuoNrNp+aJ/CzbtZVT1WLzXG41e9cu2TuOy+wpDlryfJAZ6KNVgDOmhh8TR2\nz7T0rt1QSfOZILpiwpR4jg==\n-----END PRIVATE KEY-----\n",
  "client_email": "noisycontents@thematic-bounty-382700.iam.gserviceaccount.com",
  "client_id": "107322055541690533468",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/noisycontents%40thematic-bounty-382700.iam.gserviceaccount.com"
}
creds = service_account.Credentials.from_service_account_info(info=creds_info, scopes=scope)
client = gspread.authorize(creds)
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

@bot.command(name='클래스')
async def event(ctx):
        hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url='http://studymini.com/class'
        req=urllib.request.Request(url=url, headers=hdr)
        url_open=urllib.request.urlopen(req)
        
        bs=BeautifulSoup(url_open,'html.parser')

        #이벤트 이미지 가져오기
        class1 = bs.select_one('#content > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-2d562c2.elementor-section-stretched.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section > div > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-32ebfa0.animated-fast.animated.fadeInUp > div > div > div.elementor-element.elementor-element-2516c55.elementor-widget.elementor-widget-heading > div > h2').get_text()
        class1_url = bs.select_one('#content > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-2d562c2.elementor-section-stretched.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section > div > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-32ebfa0.animated-fast.animated.fadeInUp > div > div > div.elementor-element.elementor-element-0791b93.elementor-align-center.elementor-widget.elementor-widget-button > div > div > a')['href']
        class2 = bs.select_one('#content > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-2d562c2.elementor-section-stretched.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section > div > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-cc6698e.animated-fast.animated.fadeInUp > div > div > div.elementor-element.elementor-element-a76d78b.elementor-widget.elementor-widget-heading > div > h2').get_text()
        class2_url = bs.select_one('#content > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-2d562c2.elementor-section-stretched.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section > div > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-cc6698e.animated-fast.animated.fadeInUp > div > div > div.elementor-element.elementor-element-02a0d94.elementor-align-center.elementor-widget.elementor-widget-button > div > div > a')['href']

        embed = discord.Embed(title="현재 진행중인 클래스", description="자세한 내용은 홈페이지를 참고해주세요 http://studymini.com/class", color=0x62c1cc)
        embed.add_field(name="일본어", value=f"{class1}\n [자세히 보기]({class1_url})", inline=True)     
        embed.add_field(name="프랑스어", value=f"{class2}\n [자세히 보기]({class2_url})", inline=True)     
            
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
    
@bot.command(name='이미지')
async def search_image(ctx, *args):
    query = ' '.join(args)
    search_url = f'https://openapi.naver.com/v1/search/image?query={query}'

    headers = {
    'X-Naver-Client-Id': 'iuWr9aAAyKxNnRsRSQIt' ,
    'X-Naver-Client-Secret': 'bkfPugeyIa'
    }

    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if len(data['items']) > 0:
            # Extract the top 2 search results
            results = data['items'][:2]

            # Create a separate embedded message for each search result
            for result in results:
                embed = discord.Embed(color=0x0099ff)
                embed.set_image(url=result['thumbnail'])
                await ctx.send(embed=embed)
        else:
            await ctx.send(f"No search results for \"{query}\".")
    else:
        await ctx.send('에러가 요발생했어요')

#------------------------------------------------투표------------------------------------------------------#  
def get_emoji(emoji):
    if isinstance(emoji, str):
        return emoji
    elif isinstance(emoji, discord.Emoji):
        return f'{emoji.name}:{emoji.id}'
    elif isinstance(emoji, discord.PartialEmoji):
        return f'{emoji.name}:{emoji.id}'
    else:
        return None

polls = {}

@bot.command(name='투표')
async def vote(ctx, *, args):
    if not args:
        embed = discord.Embed(title=f'Vote Help', description=f'')
        embed.add_field(name=f'Like/Dislike', value=f'!vote title')
        embed.add_field(name=f'multiple options (1-9)', value=f'!vote title, option 1, option 2, ..., option 9')
        await ctx.send(embed=embed)
    else:
        # Split title and options
        parts = [part.strip() for part in args.split(',')]
        title = parts[0]
        options = parts[1:]
        # rest of the code

        # Create embed
        embed = discord.Embed(title=title)
        if not options:
            # Like/Dislike
            message = await ctx.send(embed=embed)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        else:
            # Multiple responses (1-9)
            emoji_list = [chr(0x31) + '\u20E3', chr(0x32) + '\u20E3', chr(0x33) + '\u20E3', chr(0x34) + '\u20E3', chr(0x35) + '\u20E3', chr(0x36) + '\u20E3', chr(0x37) + '\u20E3', chr(0x38) + '\u20E3', chr(0x39) + '\u20E3'] # Option number label

            s = ''
            emoji = iter(emoji_list)
            unicode_options = []  # New list for storing Unicode representation of options
            for option in options:
                try:
                    current_emoji = next(emoji)                    
                    s += f'{current_emoji} {option}\n'
                    unicode_options.append(current_emoji)
                except StopIteration:
                    await ctx.send('Maximum of 9 options allowed.')
                    return

            # Output title and poll ID to Discord
            embed.add_field(name='Options', value=s)
            embed.add_field(name='현재 투표 현황', value='투표를 시작하신 후에 확인이 가능합니다.')

            # Send poll message
            random_poll_id = str(random.randint(1000, 9999))
            poll_message = await ctx.send(f'투표가 생성되었어요! 투표 번호는: {random_poll_id}', embed=embed)

            # Add reactions to poll message
            for i in range(len(options)):
                await poll_message.add_reaction(emoji_list[i])

            # Save poll information
            poll_info = {'title': title, 'options': unicode_options, 'votes': {}, 'closed': False, 'message_id': poll_message.id} # Use unicode_options instead of options
            polls[poll_message.id] = poll_info
            
@bot.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is for a poll message
    message_id = reaction.message.id
    poll_id = None
    for pid, poll in polls.items():
        if 'message_id' in poll and poll['message_id'] == message_id:
            poll_id = pid
            break

    if not poll_id:
        print(f"Reaction received for non-poll message with message ID {message_id}")
        return

    # Check if the reaction was added to a message sent by the bot
    if user == bot.user:
        return

    # Check if the reaction is for a valid option
    emoji = get_emoji(reaction.emoji)
    poll_data = polls[poll_id]
    option_index = -1
    for i, option in enumerate(poll_data['options']):
        if emoji == option:
            option_index = i
            break
    if option_index == -1:
        print(f"User {user.name} reacted with invalid emoji {emoji} for poll {poll_data['title']} ({poll_id})")
        return

    # Add or update user vote
    user_id = str(user.id)
    if user_id not in poll_data['votes']:
        poll_data['votes'][user_id] = emoji
    else:
        poll_data['votes'][user_id] = emoji

    print(f"User {user.name} voted for option {emoji} in poll {poll_data['title']} ({poll_id})")

    # Update poll embed with current vote count
    poll_message_id = poll_data['message_id']
    poll_message = await reaction.message.channel.fetch_message(poll_message_id)

    poll_results = {}
    for option in poll_data['options']:
        poll_results[option] = 0
    for reaction in poll_message.reactions:
        emoji = get_emoji(reaction.emoji)
        if emoji in poll_data['options']:
            async for user in reaction.users():
                if user != bot.user:
                    poll_results[emoji] += 1

    result_message = ''
    for option in poll_data['options']:
        count = poll_results[option]
        result_message += f'{option}: {count} vote(s)\n'

    poll_embed = poll_message.embeds[0]
    poll_embed.set_field_at(1, name='현재 투표 현황', value=result_message)

    await poll_message.edit(embed=poll_embed)

    print(f"Poll {poll_data['title']} ({poll_id}) updated with current vote count")
                
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


#------------------------------------------------고정------------------------------------------------------# 

sheet1 = client.open('테스트').worksheet('고정')
rows = sheet1.get_all_values()

sticky_messages = {}

for row in rows:
    sticky_messages[int(row[0])] = row[1]
    
def has_specific_roles(allowed_role_ids):
    async def predicate(ctx):
        allowed_roles = [ctx.guild.get_role(role_id) for role_id in allowed_role_ids]
        return any(role in ctx.author.roles for role in allowed_roles)

    return check(predicate)

allowed_role_ids = [922400231549722664, 1019164281696174180]    
    
# 스프레드시트에서 초기 고정 메시지를 가져옵니다.
sticky_messages = {}

sheet1_values = sheet1.get_all_values()
for row in sheet1_values:
    if len(row) == 2 and row[0].isdigit():
        channel_id = int(row[0])
        message = row[1]
        sticky_messages[channel_id] = message

def refresh_sticky_messages():
    global sticky_messages
    global last_sticky_messages
    sheet1_values = sheet1.get_all_values()

    new_sticky_messages = {}  # 반복문 바깥에서 선언합니다.
    for row in sheet1_values:
        if len(row) == 2 and row[0].isdigit():
            channel_id = int(row[0])
            message = row[1]
            new_sticky_messages[channel_id] = message  # 값을 할당합니다.

    deleted_channel_ids = set(sticky_messages.keys()) - set(new_sticky_messages.keys())
    for channel_id in deleted_channel_ids:
        if channel_id in last_sticky_messages:
            old_message = last_sticky_messages[channel_id]
            try:
                asyncio.create_task(old_message.delete())  # asyncio.create_task를 사용하여 비동기로 실행합니다.
            except discord.NotFound:
                pass

    sticky_messages = new_sticky_messages
    last_sticky_messages = {}

@bot.command(name='고정')
@has_specific_roles(allowed_role_ids)
async def sticky(ctx, *, message):
    global sticky_messages
    channel_id = ctx.channel.id
    sticky_messages[channel_id] = message

    # 스프레드시트에 고정 메시지를 저장합니다.
    if str(channel_id) in sheet1.col_values(1):
        row_num = int(sheet1.col_values(1).index(str(channel_id))) + 1
    else:
        row_num = len(sheet1.col_values(1)) + 1

    sheet1.update_cell(row_num, 1, str(channel_id))
    sheet1.update_cell(row_num, 2, message)

    # 스프레드시트에 저장된 내용을 업데이트합니다.
    refresh_sticky_messages()

    await ctx.send(f'메시지가 고정됐습니다!')

@bot.command(name='해제')
@has_specific_roles(allowed_role_ids)
async def unsticky(ctx):
    global sticky_messages
    channel_id = ctx.channel.id

    if channel_id in sticky_messages:
        del sticky_messages[channel_id]

        # 스프레드시트에서 고정 메시지를 삭제합니다.
        row_num = int(sheet1.col_values(1).index(str(channel_id))) + 1
        sheet1.delete_row(row_num)

        # 스프레드시트에 저장된 내용을 업데이트합니다.
        refresh_sticky_messages()

        await ctx.send('고정이 해제됐어요!')
    else:
        await ctx.send('이 채널에는 고정된 메시지가 없어요')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    global sticky_messages
    global last_sticky_messages

    channel_id = message.channel.id

    if channel_id in sticky_messages:
        if channel_id in last_sticky_messages:
            old_message = last_sticky_messages[channel_id]
            try:
                await old_message.delete()
            except discord.NotFound:
                pass

        new_message = await message.channel.send(sticky_messages[message.channel.id])
        last_sticky_messages[message.channel.id] = new_message
#------------------------------------------------TODO list------------------------------------------------------# 

todos = {}
completed_dates = {}
creation_times = {}

async def reset_todos():
    while True:
        now = datetime.datetime.now()
        reset_time = datetime.datetime.combine(now.date(), datetime.time(hour=0))
        if now >= reset_time:
            # Reset TODO lists for each user
            todos.clear()
            completed_dates.clear()
            creation_times.clear()
        await asyncio.sleep(3600)  # Check every hour

@bot.event
async def on_ready():
    print("Bot is ready.")
    bot.loop.create_task(reset_todos())

@bot.command(name='할일')
async def todo(ctx, *, options=None):
    if ctx.author.id in todos and all(checked for _, checked in todos[ctx.author.id]):
        await ctx.send("오늘의 TODO list 를 모두 완료했습니다!")
    elif options is None:
        if ctx.author.id in todos:
            todo_list = "\n".join([f"[{'O' if checked else ' '}] {option}" for option, checked in todos[ctx.author.id]])
            creation_time = creation_times.get(ctx.author.id, None)
            if creation_time is not None:
                creation_time_str = creation_time.strftime("%Y-%m-%d %H:%M:%S")
                embed = discord.Embed(title=f"TODO list (만들어진 시간 {creation_time_str}):", description=todo_list, color=discord.Color.green())
                await ctx.send(f"{ctx.author.mention}", embed=embed)
            else:
                embed = discord.Embed(title="TODO list:", description=todo_list, color=discord.Color.green())
                await ctx.send(f"{ctx.author.mention}", embed=embed)
        elif options == "complete":
            if all(checked for _, checked in todos.get(ctx.author.id, [])):
                embed = discord.Embed(title="Congratulations!", description="All options are checked!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Not all options are checked.")
        else:
            await ctx.send("현재 TODO list 가 작성되지 않았어요")
    else:
        options = options.split(",")
        todos[ctx.author.id] = [(option.strip(), False) for option in options]
        creation_times[ctx.author.id] = datetime.datetime.now()
        await ctx.send("TODO list 가 작성되었습니다!")
        
@bot.command(name='취소')
async def cancel(ctx):
    if ctx.author.id in todos:
        del todos[ctx.author.id]
        await ctx.send("TODO list 가 취소됐어요")
    else:
        await ctx.send("작성된 TODO list 가 없습니다")

@bot.command(name='체크')
async def check(ctx, option_num: int):
    if ctx.author.id in todos and 0 <= option_num < len(todos[ctx.author.id]):
        todos[ctx.author.id][option_num] = (todos[ctx.author.id][option_num][0], True)
        all_checked = all(checked for option, checked in todos[ctx.author.id])
        await ctx.send(f"{option_num}번 째 TODO list 가 체크 됐어요!")
        if all_checked:
            embed = discord.Embed(title="축하드립니다!", description="모든 TODO list 가 완료됐어요!", color=discord.Color.green())
            await ctx.send(embed=embed)
    else:
        await ctx.send("TODO list에 없는 항목이에요")

@bot.command(name='체크해제')
async def uncheck(ctx, option_num: int):
    if ctx.author.id in todos and 0 <= option_num < len(todos[ctx.author.id]):
        todos[ctx.author.id][option_num] = (todos[ctx.author.id][option_num][0], False)
        await ctx.send(f"Option {option_num} unchecked.")
    else:
        await ctx.send("TODO list 에 없는 항목이에요")

#------------------------------------------------운세------------------------------------------------------# 
        
@bot.command(name='운세')
async def Fortune(ctx):
    embed = discord.Embed(title="2023년 외국어 운세보기", description="올해 나의 운세를 외국어로 점쳐봅시다!", color=0xffd700)
    embed.set_footer(text="클릭하여 운세를 확인하세요!")
    button = discord.ui.Button(style=discord.ButtonStyle.primary, label="올해 나의 운세는?", url="https://bit.ly/2023_fortune")
    view = discord.ui.View()
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

@bot.command(name='공부')
async def study(ctx):
    if random.random() < 0.8:
        message = "오늘 같은 날은 집에서 공부하고 일취월장 인증 어떠신가요 🥳"
    else:
        message = "오늘 공부는 패스!"
    embed = discord.Embed(title="공부..할까..말까?", description=message, color=0xffd700)
    await ctx.send(embed=embed)
    
#-------------------------메모-------------------------#

sheet = client.open('테스트').worksheet('메모')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='메모')
async def memo(ctx):
    # Extract user ID and memo content
    user_id = str(ctx.author.id)
    message_content = ctx.message.content
    memo = message_content.split('!메모 ')[1]

    # Find the next available column to write data to
    header_values = sheet.row_values(1)
    if not header_values:
        col = 1
        sheet.update_cell(1, col, user_id)
    elif user_id not in header_values:
        last_user_col = sheet.col_count
        last_user_id = header_values[-1]
        last_user_id_col = header_values.index(last_user_id) + 1
        col = last_user_id_col + 1
        sheet.add_cols(1)
        sheet.update_cell(1, col, user_id)
    else:
        col = header_values.index(user_id) + 1

    # Find the next available row to write data to
    values = sheet.col_values(col)
    row = len(values) + 1

    # Write user ID and memo content to the corresponding cell
    if row == 1:
        sheet.update_cell(row, col, user_id)
        row += 1
    sheet.update_cell(row, col, memo)

    await ctx.send(f'{ctx.author.mention} 메모가 저장됐어요')
    
@bot.command(name='메모보기')
async def view_memo(ctx):
    # Extract user ID
    user_id = str(ctx.author.id)

    # Find the column index of the user ID in row 1
    header_values = sheet.row_values(1)
    try:
        col = header_values.index(user_id) + 1
    except ValueError:
        await ctx.send(f'{ctx.author.mention} 메모를 찾을 수 없습니다 :(')
        return

    # Retrieve memo content for the user from row 2
    memo_values = sheet.col_values(col)[1:]
    if memo_values:
        memo_list = [f'{i+1}. {memo}' for i, memo in enumerate(memo_values)]
        memo_str = '\n'.join(memo_list)
        embed = discord.Embed(title=f"{ctx.author.name}의 메모입니다", description=memo_str)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'{ctx.author.mention} 메모를 찾지 못했어요')
        
@bot.command(name='메모삭제')
async def delete_memo(ctx, memo_number: int):
    # Extract user ID
    user_id = str(ctx.author.id)

    # Find the column index of the user ID in row 1
    header_values = sheet.row_values(1)
    try:
        col = header_values.index(user_id) + 1
    except ValueError:
        await ctx.send(f'{ctx.author.mention} 메모를 찾지 못했어요')
        return

    # Retrieve memo content for the user from row 2
    memo_values = sheet.col_values(col)[1:]

    # Check if the given memo number is valid
    if memo_number <= 0 or memo_number > len(memo_values):
        await ctx.send(f'{ctx.author.mention} 메모 번호가 틀린 것 같아요')
        return

    # Delete the memo content from the spreadsheet and shift the remaining memos up
    index_to_delete = memo_number + 1
    remaining_memos = memo_values[index_to_delete - 2:]
    for i, _ in enumerate(remaining_memos[:-1]):
        sheet.update_cell(index_to_delete + i, col, remaining_memos[i + 1])

    # Clear the last cell after shifting the memos or if the deleted memo is the last one
    sheet.update_cell(index_to_delete + len(remaining_memos) - 1, col, '')

    await ctx.send(f'{ctx.author.mention} {memo_number}번 메모가 정상적으로 삭제됐어요!')
    
@bot.command(name='전체삭제')
async def delete_all_memos(ctx):
    # Extract user ID
    user_id = str(ctx.author.id)

    # Find the column index of the user ID in row 1
    header_values = sheet.row_values(1)
    try:
        col = header_values.index(user_id) + 1
    except ValueError:
        await ctx.send(f'{ctx.author.mention} 저장된 메모가 없습니다')
        return

    # Delete the entire column for the user
    sheet.delete_columns(col)

    await ctx.send(f'{ctx.author.mention} 모든 메모가 삭제됐어요!')
   
#-------------------------메뉴추천-------------------------#

class MenuSelector(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=none)
        self.category = None
        self.foods = {
            "분식": ["김밥", "라면", "떡볶이", "튀김", "순대", "만두", "라볶이", "어묵", "소떡소떡", "핫도그", "떡국", "잔치국수", "볶음밥"],
            "한식": ["비빔밥", "불고기", "된장찌개", "김치찌개", "제육볶음", "족발", "부침개", "곱창", "보쌈", "치킨!!", "생선구이", "비빔밥", "쌈밥", "게장", "불고기"],
            "중식": ["짜장면", "짬뽕", "탕수육", "양장피", "마라탕", "마라샹궈", "양꼬치", "깐쇼새우", "깐풍기"],
            "일식": ["초밥", "우동", "돈까스", "라멘", "회", "타코야끼", "샤브샤브"],
            "양식": ["피자", "파스타", "스테이크", "샐러드", "햄버거", "바베큐", "그라탕"],
            "해장": ["우거지국", "홍합탕", "순대국", "콩나물국밥", "뼈해장국", "대파라면", "선지해장국", "매생이국", "북엇국"],
            "디저트": ["아이스크림", "빵", "과일", "케이크", "마카롱", "요거트", "와플"],
            "편의점": ["삼각김밥", "도시락", "샌드위치", "컵라면", "컵밥", "라이스바"],
            "기타": ["월남쌈", "나시고랭", "브리또", "케밥", "맥앤치즈", "분짜", "쌀국수"],
        }
        self.menu_select = discord.ui.Select(
            placeholder="원하시는 종류를 선택해주세요!",
            options=[
                discord.SelectOption(label="분식", value="분식"),
                discord.SelectOption(label="한식", value="한식"),
                discord.SelectOption(label="중식", value="중식"),
                discord.SelectOption(label="일식", value="일식"),
                discord.SelectOption(label="양식", value="양식"),
                discord.SelectOption(label="해장", value="해장"),
                discord.SelectOption(label="디저트", value="디저트"),
                discord.SelectOption(label="편의점", value="편의점"),
                discord.SelectOption(label="기타", value="기타"),
            ],
        )
        self.menu_select.callback = self.select_callback
        self.add_item(self.menu_select)

        self.recommend_button = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="추천받기!",
            disabled=True
        )
        self.recommend_button.callback = self.recommend_callback
        self.add_item(self.recommend_button)

        self.map_button = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label="재학생들의 국내/외 맛집 리스트",
            url="https://www.google.com/maps/d/edit?mid=1-le8EVMGB6tH-4ryziNUUub1XyOSgHI&usp=sharing"
        )
        self.add_item(self.map_button)

    async def select_callback(self, interaction: discord.Interaction):
        self.category = interaction.data['values'][0]

        # update the label and disabled state of the existing button
        self.recommend_button.callback = self.recommend_callback
        self.recommend_button.disabled = False

        await interaction.response.edit_message(view=self)

    async def recommend_callback(self, interaction: discord.Interaction):
        if self.category is not None:
            selected_food = random.choice(self.foods[self.category])
        else:
            selected_food = "카테고리를 선택해주세요."
        food = discord.Embed(title=f"{self.category} 추천메뉴", description="아래 추천받기 버튼을 클릭해서 메뉴를 추천받아보세요!", color=0x00ff00)
        food.add_field(name="메뉴", value=f"{selected_food}")
        food.set_footer(text="맛있게 드세요! 🥳")
        await interaction.response.edit_message(embed=food, view=self)
                        
@bot.command(name='메뉴추천')
async def menu_recommendation(ctx):
    selector_view = MenuSelector()
    message = await ctx.send("원하시는 종류를 선택해주세요!", view=selector_view)
    selector_view.message = message
   
#------------------------------------------------#

@bot.command(name='가위')
async def rock_paper_scissors(ctx):
    user_choice = '가위'
    await play_game(user_choice, ctx, '✌️')

@bot.command(name='바위')
async def rock_paper_scissors(ctx):
    user_choice = '바위'
    await play_game(user_choice, ctx, '✊')

@bot.command(name='보')
async def rock_paper_scissors(ctx):
    user_choice = '보'
    await play_game(user_choice, ctx, '🖐️')

async def play_game(user_choice, ctx, user_emoji):
    rps = ['가위', '바위', '보']
    bot_choice = random.choice(rps)

    # 가위, 바위, 보에 대응하는 이모지
    rps_emoji = {'가위': '✌️', '바위': '✊', '보': '🖐️'}

    result = None
    if user_choice == bot_choice:
        result = '비겼습니다!'
        color = discord.Color.dark_gray()
        emoji = '🤝'
    elif (user_choice == '가위' and bot_choice == '보') or \
         (user_choice == '바위' and bot_choice == '가위') or \
         (user_choice == '보' and bot_choice == '바위'):
        result = '테이망령이 졌습니다!😭'
        color = discord.Color.green()
        emoji = '🎉'
    else:
        result = '테이망령이 이겼습니다!🥳'
        color = discord.Color.red()
        emoji = '😭'

    embed = discord.Embed(title=f'{user_emoji} 대 {rps_emoji[bot_choice]}', description=result, color=color)
    embed.set_author(name='게임 결과')

    await ctx.send(embed=embed)
    
#Run the bot
bot.run(TOKEN)

