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

#------------------------------------------------말하기------------------------------------------------------# 
intents.typing = False
intents.presences = False

class UserMentions:
    def __init__(self, bot):
        self.bot = bot
        self.user_mentions = None
        self.bot.loop.create_task(self.load_user_mentions())

    async def load_user_mentions(self):
    print("Loading user mentions...")
    try:
        async with aiofiles.open("user_mentions.json", "r") as f:
            data = await f.read()
            print("JSON data:", data)
            user_mentions = json.loads(data)
            print("Parsed user mentions:", user_mentions)
            self.user_mentions = {k: [await self.bot.fetch_user(int(user_id)) for user_id in v] for k, v in user_mentions.items()}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.user_mentions = {}
            print("Exception:", e)
    print("User mentions loaded:", self.user_mentions)

    async def save_user_mentions(self):
        data = {k: [user.id for user in v] for k, v in self.user_mentions.items()}
        async with aiofiles.open("user_mentions.json", "w") as f:
            await f.write(json.dumps(data))

user_mentions_instance = None

async def setup():
    global user_mentions_instance
    user_mentions_instance = UserMentions(bot)
    await user_mentions_instance.load_user_mentions()

class CustomView(discord.ui.View):
    def __init__(self, user_mentions=None):
        super().__init__(timeout=None)
        self.user_mentions = user_mentions or {}

    def add_button(self, button):
        self.add_item(button)
        if button.custom_id not in self.user_mentions:
            self.user_mentions[button.custom_id] = []

class ButtonClick(discord.ui.Button):
    def __init__(self, label, view):
        super().__init__(label=label, custom_id=label)
        self.parent_view = view

    async def callback(self, interaction: discord.Interaction):
        view = self.parent_view
        user = interaction.user
        user_mentions = view.user_mentions[self.custom_id]
        guild = interaction.guild
        role_id = 1076005878290989097
        role = guild.get_role(role_id)

        if not role:
            await interaction.response.send_message("Role not found. Please check if the role ID is correct.", ephemeral=True)
            return

        if user in user_mentions:
            user_mentions.remove(user)
            await interaction.user.remove_roles(role)
        else:
            user_mentions.append(user)
            await interaction.user.add_roles(role)

        await user_mentions_instance.save_user_mentions()

        embed = discord.Embed(title="말하기 스터디 참여 현황")
        for button in view.children:
            mentions_str = " ".join([f"{user.mention}" for user in view.user_mentions[button.custom_id]])
            embed.add_field(name=button.label, value=mentions_str if mentions_str else "아직 참여자가 없어요 :(", inline=True)
        await interaction.response.edit_message(embed=embed)

@bot.event
async def on_ready():
    user_mentions_instance = UserMentions(bot)
        
@bot.command(name='말하기')
async def speak(ctx):
    print(user_mentions_instance)  # check if user_mentions_instance has been initialized
    await display_speak(ctx)
    
async def display_speak(ctx):
    if user_mentions_instance is None:
        await ctx.send("User mentions not loaded yet. Please wait a moment and try again.")
        return

    user_mentions = user_mentions_instance.user_mentions
    view = CustomView(user_mentions)
    buttons = [
        ButtonClick("스페인어", view),
        ButtonClick("중국어", view),
        ButtonClick("일본어", view),
        ButtonClick("영어", view),
        ButtonClick("프랑스어", view),
        ButtonClick("독일어", view),
    ]

    for button in buttons:
        view.add_button(button)

    embed = discord.Embed(title="말하기 스터디 참여 현황")
    for button in buttons:
        mentions_str = " ".join([f"{user.mention}" for user in view.user_mentions[button.custom_id]])
        embed.add_field(name=button.label, value=mentions_str if mentions_str else "아직 참여자가 없어요 :(", inline=True)
    await ctx.send(embed=embed, view=view)
            
#------------------------------------------------고정------------------------------------------------------# 

intents.messages = True

stichy_message = None
sticky_channel = None

sticky_messages = {}

@bot.command(name='고정')
async def sticky(ctx, *, message):
    global sticky_messages
    sticky_messages[ctx.channel.id] = message
    await ctx.send(f'메시지가 정상적으로 고정되었습니다')

@bot.command(name='해제')
async def unsticky(ctx):
    global sticky_messages
    if ctx.channel.id in sticky_messages:
        del sticky_messages[ctx.channel.id]
        await ctx.send('고정 메시지가 삭제됐어요')
    else:
        await ctx.send('고정 메시지가 없습니다')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    global sticky_messages
    if message.channel.id in sticky_messages:
        await message.channel.send(sticky_messages[message.channel.id])

#Run the bot
bot.run(TOKEN)

