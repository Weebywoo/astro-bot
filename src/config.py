import os

NASA_API_URLS: dict[str, str | dict] = {
    "apod": "https://api.nasa.gov/planetary/apod",
    "neows": {
        "feed": "https://api.nasa.gov/neo/rest/v1/feed",
        "lookup": "https://api.nasa.gov/neo/rest/v1/neo/",
        "browse": "https://api.nasa.gov/neo/rest/v1/neo/browse/",
    },
}
DISCORD_TOKEN: str = os.environ.get("DISCORD_TOKEN")
NASA_TOKEN: str = os.environ.get("NASA_API_KEY")
