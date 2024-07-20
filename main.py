import asyncio

import discord

from src import Bot, config
from src.commands import NasaApiCommands


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    commands = [
        NasaApiCommands,
    ]

    async with Bot(command_prefix='>', intents=intents, custom_commands=commands) as bot:
        await bot.start(config.discord_token)


if __name__ == '__main__':
    asyncio.run(main())
