import discord
from discord.ext.commands import Bot
from asyncio import sleep
from discord import User
import os
from dotenv import load_dotenv
import asyncio
from discord.ext import commands
import re

load_dotenv()
token = str(os.getenv('TOKEN'))
prefix = str(os.getenv('PREFIX'))

intents = discord.Intents.default()
intents.message_content = True

client = Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def suggest(ctx, *, suggestion: str):
    await ctx.send('Suggestion sent!')
    await sleep(1)
    await ctx.message.delete()
    channel = client.get_channel(969009498058530863)
    embed = discord.Embed(title='New Suggestion', description=f'{suggestion}', color=0x00ff00)
    embed.add_field(name="Author", value=ctx.message.author.mention, inline=False)
    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def approve(ctx, user: User, suggestionMessageID: int,*, reason: str):
    await ctx.message.delete()
    channel = client.get_channel(969009498058530863)
    message = await channel.fetch_message(suggestionMessageID)
    embed = discord.Embed(title='Suggestion Approved', description=f'{reason}', color=0x00ff00)
    embed.add_field(name="Administrator", value=ctx.message.author.mention, inline=False)
    await user.send(embed=embed)
    await message.reply(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def deny(ctx, user: User, suggestionMessageID: int,*, reason: str):
    await ctx.message.delete()
    channel = client.get_channel(969009498058530863)
    message = await channel.fetch_message(suggestionMessageID)
    embed = discord.Embed(title='Suggestion Denied', description=f'{reason}', color=0x00ff00)
    embed.add_field(name="Administrator", value=ctx.message.author.mention, inline=False)
    await user.send(embed=embed)
    await message.reply(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def customEmbed(ctx):
    await ctx.send('What would you like the title to be?')
    title = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    title = title.content
    await ctx.send('What would you like the description to be?')
    description = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    description = description.content
    await ctx.send('What would you like the footer to be?')
    footer = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    footer = footer.content
    await ctx.send('What channel would you like to send the embed to?')
    channel = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    channel_mention = channel.content
    channel_id = int(re.search(r'\d+', channel_mention).group())
    channel = client.get_channel(channel_id)

    await ctx.message.delete()
    embed = discord.Embed(title=f'{title}', description=f'{description}', color=0x00ff00)
    embed.set_footer(text=f'{footer}')
    await channel.send(embed=embed)

    



client.run(token)
