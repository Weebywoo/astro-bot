import json

import discord
import requests
from discord.ext import commands
from requests import Response

from .interfaces import NasaEndpoints
from .log import Severity, log


class Bot(commands.Bot):
    def __init__(self, custom_commands: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._commands = custom_commands

    async def setup_hook(self) -> None:
        if self._commands is not None:
            for extension in self._commands:
                await self.load_extension(extension.path)

        loaded_cogs = {
            cog_name: cog_cls.description for cog_name, cog_cls in self.cogs.items()
        }
        log(Severity.INFO, f'Cogs loaded: {json.dumps(loaded_cogs, indent=2)}')

        healthcheck_result = NasaEndpoints.do_healthcheck()

        if list(healthcheck_result.values()).count(True) >= 1:
            # Add pretty printing of available Nasa endpoints and response times
            log(Severity.INFO, 'NASA endpoints up and running!')

            for name, status in healthcheck_result.items():
                log(Severity.INFO, f'{name.ljust(7)}: {str(status).rjust(1)}')

        else:
            log(Severity.ERROR, 'Database unreachable. Exiting...')
            exit()

    async def on_ready(self) -> None:
        log(Severity.INFO, f"Logged in as '{self.user}'")

    async def on_message(self, message: discord.Message) -> None:
        context = await self.get_context(message)

        if context.valid:
            if context.command:
                log(Severity.INFO, f"'{message.author}' used '{context.command}'")

                await self.process_commands(message)
