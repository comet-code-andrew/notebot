import discord

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.sent('hello, I am a bot')

client.run(env('SECRET_KEY'))
