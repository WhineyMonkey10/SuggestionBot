import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(';hello'):
        await message.channel.send('Hello!')

client.run('f.GfjplP.8RlivW2TF-TdWgK1_6ade0Ro0Ssaq42j4yMevM')
