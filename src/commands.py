from discord import Embed
from discord.ext.commands import Bot, Cog, command, Context

from src.create_embeds import create_apod_embed
from src.nasa_endpoints import NasaEndpoints


class NasaApiCommands(Cog):
    path: str = __name__

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="apod")
    async def apod(self, context: Context):
        apod: dict = NasaEndpoints.get_apod()
        embed: Embed = create_apod_embed(apod)

        await context.message.reply(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(NasaApiCommands(bot))
