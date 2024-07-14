from discord.embeds import Embed


def create_apod_embed(apod: dict[str, str]) -> Embed:
    embed: Embed = Embed(
        title=apod['title'],
        description=apod['explanation'],
    )

    if (author := apod['copyright']) is not None:
        embed.set_author(name=author)
        embed.set_footer(text=apod['copyright'])

    embed.set_image(url=apod['hdurl'])

    return embed
