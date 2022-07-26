# bot.py
import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = 'MTAwMTMxMzAzNTM5NjMxNzI0NA.GKCu6C.KYnKTfSxef2daWYB-66oFxnq35fl5KDpxmP_uw'

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Game(name=":help  for commands")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)