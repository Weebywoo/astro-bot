import asyncio
import os

import discord
from fastapi import FastAPI

from src.api import router as api_router
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


app = FastAPI()
app.include_router(api_router)

asyncio.run(main())
