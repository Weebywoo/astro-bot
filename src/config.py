import os

nasa_api_urls: dict[str, str] = {
    'APOD': 'https://api.nasa.gov/planetary/apod'
}

discord_token: str = os.environ.get('DISCORD_API_KEY')
nasa_token: str = os.environ.get('NASA_API_KEY')
