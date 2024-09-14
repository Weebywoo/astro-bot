from typing import Type

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from src.log import log


class Bot(commands.Bot):
    def __init__(self, custom_commands: list[Type[Cog]] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._commands: list[Type[Cog]] = custom_commands

    async def setup_hook(self) -> None:
        if self._commands is not None:
            for extension in self._commands:
                await self.load_extension(extension.path)

        log("info", f"Cogs loaded: {list(self.cogs.keys())}")

    async def on_ready(self) -> None:
        log("info", f"Logged in as '{self.user}'")

    async def on_message(self, message: discord.Message) -> None:
        context = await self.get_context(message)

        if context.valid:
            if context.command:
                log(
                    "info",
                    f"'{message.author}' from '{message.guild.name}' ({message.guild.id}) used '{context.command}'",
                )

                await self.process_commands(message)
