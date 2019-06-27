import discord
from discord.ext import commands
import asyncio

client = discord.Client()
guild = client.get_guild(id=593449968648585236)

@client.event
async def on_ready():
    print('Startando...')
    print(client.user.name)
    print('Pronto !')

@client.event
async def on_message(message):
    guild = client.get_guild(593449968648585236)
    nodewar = guild.get_channel(520001040289103903)
    if message.content == '!nodewar':
        members =[m.name for m in nodewar.members]
        await message.channel.send(members)

client.run('NTkzNDQ5OTY4NjQ4NTg1MjM2.XRURrA.oFsjb1AYZySz_Us-JWZ7I3kgxpE')