# bot.py
import os

import discord
from discord.ext import commands
import requests
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = 'test_token'

bot = commands.Bot(command_prefix='~', description="test bot", intent=discord.Intents.default())

@bot.event
async def on_ready():
    print ('bot is ready')
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Responded in {round(bot.latency * 1000)}ms')

@bot.command()
async def roast_koko(ctx):
    response = requests.get("https://insult.mattbas.org/api/insult")
    await ctx.send(response.text) 

# @bot.event
# async def on_message():
#     activity = discord.Game(name=":help  for commands")
#     await bot.change_presence(status=discord.Status.online, activity=activity)
#     print ('bot is ready')
#     print('We have logged in as {0.user}'.format(bot))

bot.run(TOKEN)