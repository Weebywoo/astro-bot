import json
from datetime import datetime
from typing import Literal

import requests
from discord import Embed

from src.config import NASA_TOKEN


def log(severity: Literal["info", "error"], message: str) -> None:
    print(f"[{datetime.now()}]", f"[{severity}]", message)


def do_request(url: str, **query_parameters) -> dict[str, str] | None:
    log("info", f"Requesting {url}")

    query_parameters.update({"api_key": NASA_TOKEN})

    response: requests.Response = requests.request(method="GET", url=url, params=query_parameters)

    if response.ok:
        log("info", f"Received {json.dumps(response.json(), indent=4)}")

        return response.json()

    response.raise_for_status()

    return None


def create_apod_embed(apod: dict[str, str]) -> Embed:
    embed: Embed = Embed(
        title=apod["title"], description=apod["explanation"], timestamp=datetime.fromisoformat(apod["date"])
    )

    if "copyright" in apod:
        author: str = apod["copyright"]
        embed.set_author(name=author)
        embed.set_footer(text=author)

    if "hdurl" in apod:
        embed.set_image(url=apod["hdurl"])

    return embed


def create_earth_embed(earth: dict[str, str], **query_parameters) -> Embed:
    description: str = f"Latitude: {query_parameters['lat']}\nLongitude: {query_parameters['lon']}\nDate: {query_parameters['date']}\nDimension: {query_parameters['dim'] if 'dim' in query_parameters else 0.025}°"
    embed: Embed = Embed(
        title="Earth observation data", description=description, timestamp=datetime.fromisoformat(earth["date"])
    )

    embed.set_image(url=earth["url"])

    return embed
