from datetime import datetime

from discord.embeds import Embed

from src.log import log


def create_apod_embed(apod: dict[str, str]) -> Embed:
    embed: Embed = Embed(
        title=apod["title"],
        description=apod["explanation"],
        timestamp=datetime.fromisoformat(apod["date"])
    )

    if "copyright" in apod:
        author: str = apod["copyright"]
        embed.set_author(name=author)
        embed.set_footer(text=apod["copyright"])

    embed.set_image(url=apod["hdurl"])

    return embed


def create_neows_embed(neows: dict[str, str]):
    log("info", str(neows))
