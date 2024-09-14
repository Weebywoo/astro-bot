import requests

from src.config import NASA_API_URLS, NASA_TOKEN
from src.log import log


def do_request(url: str) -> dict[str, str]:
    log("info", f"Requesting {url}")

    response: requests.Response = requests.request(method="GET", url=url, params={"api_key": NASA_TOKEN})

    log("info", f"Received {response.headers['Content-Type']}")

    if response.ok:
        return response.json()

    response.raise_for_status()


class NasaEndpoints:
    @classmethod
    def get_apod(cls) -> dict[str, str]:
        return do_request(NASA_API_URLS["apod"])
