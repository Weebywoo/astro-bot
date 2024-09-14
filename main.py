import asyncio
from typing import Type

import discord
from discord.ext.commands import Cog

from src.config import DISCORD_TOKEN
from src.bot import Bot
from src.commands import NasaApiCommands


async def main():
    intents: discord.Intents = discord.Intents.default()
    intents.message_content = True
    commands: list[Type[Cog]] = [
        NasaApiCommands,
    ]

    async with Bot(command_prefix=">", intents=intents, custom_commands=commands) as bot:
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
