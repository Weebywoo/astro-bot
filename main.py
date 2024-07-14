import asyncio
import os

import discord

from src.bot import Bot
from src.commands import NasaApiCommands


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    commands = [
        NasaApiCommands,
    ]

    async with Bot(command_prefix=">", intents=intents, custom_commands=commands) as bot:
        await bot.start(os.environ.get('DISCORD_TOKEN'))


asyncio.run(main())
