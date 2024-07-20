import requests

nasa_api_urls: dict[str, str] = {
    'APOD': 'https://api.nasa.gov/planetary/apod'
}

token_response: dict[str, str] = requests.get('host.docker.internal:8000/api/token/astro-bot').json()
discord_token: str = token_response['discord_token']
nasa_token: str = token_response['nasa_token']
