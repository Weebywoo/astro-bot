import os

import requests

from src import config
from src.config import nasa_api_urls
from src.log import log, Severity


class NasaEndpoints:
    NASA_API_KEY: str = config.nasa_token

    @classmethod
    def do_healthcheck(cls) -> dict[str, bool]:
        endpoints: dict[str, callable] = {
            'APOD': cls.get_apod
        }
        result: dict[str, bool] = {}

        for name, endpoint in endpoints.items():
            response: dict[str, str] | None = endpoint()
            result[name] = response is not None

        return result

    @classmethod
    def do_request(cls, method: str, url: str, params: dict[str, str]) -> dict[str, str] | None:
        try:
            response = requests.request(method=method, url=url, params=params)

            log(Severity.INFO, 'Requests left: ' + response.headers['X-RateLimit-Remaining'])
            log(Severity.INFO, response.json())

            return response.json()

        except Exception as exception:
            log(Severity.ERROR, str(exception))

            return None

    @classmethod
    def get_apod(cls) -> dict[str, str] | None:
        response: dict[str, str] = cls.do_request('GET', nasa_api_urls['APOD'], params={'api_key': cls.NASA_API_KEY})

        return response
