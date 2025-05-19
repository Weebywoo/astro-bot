import os

NASA_API_URLS: dict[str, str | dict] = {
    "apod": "https://api.nasa.gov/planetary/apod",
    "earth": "https://api.nasa.gov/planetary/earth/assets",
}
DISCORD_TOKEN: str = os.environ.get("DISCORD_TOKEN")
NASA_TOKEN: str = os.environ.get("NASA_API_KEY")
