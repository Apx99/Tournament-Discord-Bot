import discord 
from discord.ext import commands
import os 
from dotenv import load_dotenv
load_dotenv()
import requests as rq
import json
import random
from test import *   

client = discord.Client()
client = commands.Bot(command_prefix='b!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send('ur cringe')


client.run(os.getenv("TOKEN"))






