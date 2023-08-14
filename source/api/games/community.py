import allure

from constants import tester_auth
from source.base.client import client
from source.enums.games import Community


class Communities:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth if auth else tester_auth

    @allure.step('Get community comments by review_id "{id_data}"')
    def comments_id(self, id_data, limit=None, offset=None):
        params = {
            'limit': limit,
            'offset': offset
        }
        url = f'{Community.COMMENTS}{id_data}'
        response = self.client.get(url=url, params=params, auth=self.auth)
        return response

    @allure.step('Get community review by game_uuid "{id_data}"')
    def review_id(self, id_data, limit=None, offset=None):
        params = {
            'limit': limit,
            'offset': offset
        }
        url = f'{Community.REVIEW}{id_data}'
        response = self.client.get(url=url, params=params, auth=self.auth)
        return response


community = Communities()
