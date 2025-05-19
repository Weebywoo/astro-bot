import json

from discord import Embed
from discord.ext.commands import Bot, Cog, command, Context

from src.auxiliary import do_request, create_apod_embed, create_earth_embed, log
from src.config import NASA_API_URLS


class NasaApiCommands(Cog):
    path: str = __name__

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="apod")
    async def astronomical_picture_of_the_day(self, context: Context):
        apod: dict = do_request(NASA_API_URLS["apod"])
        embed: Embed = create_apod_embed(apod)

        await context.reply(embed=embed)

    @command(name="earth")
    async def earth_observation_data(self, context: Context, *, message: str):
        query_parameters: dict[str, str] = dict(
            map(lambda query_parameter: query_parameter.split("="), message.split(" "))
        )

        log("info", json.dumps(query_parameters))
        earth: dict = do_request(NASA_API_URLS["earth"], **query_parameters)
        embed: Embed = create_earth_embed(earth, **query_parameters)

        await context.reply(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(NasaApiCommands(bot))
