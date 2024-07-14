import os

import requests

from src.config import NASA_API_URLS


class NasaEndpoints:
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

            print('Requests left:', response.headers['X-RateLimit-Remaining'])

            return response.json()

        except Exception as exception:
            print(exception)

            return None

    @classmethod
    def get_apod(cls) -> dict[str, str] | None:
        response = cls.do_request('GET', NASA_API_URLS['APOD'], params={'api_key': os.environ.get('NASA_API_KEY')})

        return response
