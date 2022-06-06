import os
import discord
import requests
from sefariaRef import api_url
from parsingService import checkBook, textClean
from formatService import formatEmbed

client = discord.Client()
token = os.environ['TOKEN']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
      return
  info = checkBook(message.content)
  if info != False:
    embed = formatEmbed(requests.get(api_url + info[0] + "." + str(info[1])).json(), info)
    await message.channel.send(embed=embed)

client.run(token)