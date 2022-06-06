import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTgzNDA1Mzc0NzA5MzIxNzM5.GFAggZ.5wmC2tn9XIb2E13kPEEBS41gTl-BRuwTC302Rc')