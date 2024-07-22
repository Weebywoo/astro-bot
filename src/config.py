import os

nasa_api_urls: dict[str, str] = {
    'APOD': 'https://api.nasa.gov/planetary/apod'
}

discord_token: str = os.environ.get('discord_token')
nasa_token: str = os.environ.get('nasa_token')
