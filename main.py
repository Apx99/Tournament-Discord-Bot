import discord 
from discord.ext import commands
import requests
import json
import random
import os 
from dotenv import load_dotenv
load_dotenv()

 

client = discord.Client()
client = commands.Bot(command_prefix='b!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send('ur cringe')

@client.command()
async def imagine(ctx):
    await ctx.send('Imagine dragging these nuts on your face.')    


client.run(os.getenv("TOKEN"))






