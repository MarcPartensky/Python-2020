import discord
from discord.ext import commands

TOKEN = "NzAzMjAwOTQwNDU4NzcwNjEz.XqLJsw.djqZwgImOVdfrfGYj5R3Nrw_EN0"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('salut'):
        await message.channel.send('Bien le bonjour.')
"""

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def salut(ctx):
    ctx.send('Salut')

client.run(TOKEN)
