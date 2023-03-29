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

intents.messages = True



sticky_messages = {}
last_sticky_messages = {}

def has_specific_roles(allowed_role_ids):
    async def predicate(ctx):
        allowed_roles = [ctx.guild.get_role(role_id) for role_id in allowed_role_ids]
        return any(role in ctx.author.roles for role in allowed_roles)

    return check(predicate)

allowed_role_ids = [922400231549722664, 1019164281696174180]    

@bot.command(name='고정')
@has_specific_roles(allowed_role_ids)
async def sticky(ctx, *, message):
    global sticky_messages
    sticky_messages[ctx.channel.id] = message
    await ctx.send(f'메시지가 고정됐습니다!')

@bot.command(name='해제')
@has_specific_roles(allowed_role_ids)
async def unsticky(ctx):
    global sticky_messages
    if ctx.channel.id in sticky_messages:
        del sticky_messages[ctx.channel.id]
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

    if message.channel.id in sticky_messages:
        if message.channel.id in last_sticky_messages:
            old_message = last_sticky_messages[message.channel.id]
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

#Run the bot
bot.run(TOKEN)

