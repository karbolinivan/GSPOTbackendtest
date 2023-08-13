import allure

from constants import tester_auth
from source.base.client import client
from source.enums.games import Utils


class Filters:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth if auth else tester_auth

    @allure.step('Get filters prices list')
    def prices_list(self, limit: int = None, offset: int = None):
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self.client.get(url=Utils.PRICES, params=params, auth=self.auth)
        return response

    @allure.step('Get filters platforms list')
    def platforms_list(self, limit: int = None, offset: int = None):
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self.client.get(url=Utils.PLATFORMS, params=params)
        return response

    @allure.step('Get filters genres list')
    def genres_list(self, limit: int = None, offset: int = None):
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self.client.get(url=Utils.GENRES, params=params, auth=self.auth)
        return response


filters = Filters()
