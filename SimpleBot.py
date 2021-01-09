import os
import config
import discord
from dotenv import load_dotenv

from bs4 import BeautifulSoup
import urllib.request

import requests
from discord.utils import get
import spotipy

import urllib.parse






load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('SERVER_NAME')

from discord.ext import commands

client = commands.Bot(command_prefix='!')

client_id = config.client_id
client_secret = config.client_secret
username = config.username


#@bot.command()
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

players = {}

@client.command(pass_context=True)
async def link(ctx, info):
    textToSearch = str(info)
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href'])
    #webbrowser.open('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href'])
    await ctx.send('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href'])



#bot.run(TOKEN)

client.run(TOKEN)