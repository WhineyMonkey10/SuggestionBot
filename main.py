import discord
from discord.ext.commands import Bot
from asyncio import sleep
from discord import User

intents = discord.Intents.default()
intents.message_content = True

client = Bot(command_prefix=';', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def suggest(ctx, *, suggestion: str):
    await ctx.send('Suggestion sent!')
    await sleep(1)
    await ctx.message.delete()
    channel = client.get_channel(969009498058530863)
    await channel.send(f'{ctx.message.author.mention} has suggested: {suggestion}')

client.run('')
