import discord
import os
from dotenv import load_dotenv  # For loading environment variables from .env file

# Intents are required for bots to receive certain events
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Example command: !hello
    if message.content == '!hello':
        await message.channel.send('Hello!')
    
    # --- Command scaffolding ---
    # Add future commands below:
    # if message.content.startswith('!yourcommand'):
    #     await message.channel.send('Response here')

# Entry point for running the bot
if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()
    # Get the token from the .env file
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        raise ValueError('Please set the DISCORD_BOT_TOKEN environment variable in your .env file.')
    client.run(token)

