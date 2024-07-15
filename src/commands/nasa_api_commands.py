from discord.ext import commands
from discord.ext.commands import Bot

from src.create_embeds import create_apod_embed
from src.interfaces import NasaEndpoints


class NasaApiCommands(commands.Cog):
    path: str = __name__

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name='apod')
    async def apod(self, context: commands.Context):
        await context.channel.send(embed=create_apod_embed(NasaEndpoints.get_apod()))


async def setup(bot: Bot):
    await bot.add_cog(NasaApiCommands(bot))
