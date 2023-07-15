import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Community


@allure.step('Get community comments by review_id "{id_data}"')
def get_community_comments(id_data, limit=None, offset=None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    url = f'{Community.COMMENTS}{id_data}'
    response = Requests.get(url=url, params=params, auth=auth)
    return response


@allure.step('Get community review by game_uuid "{id_data}"')
def get_community_review(id_data, limit=None, offset=None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    url = f'{Community.REVIEW}{id_data}'
    response = Requests.get(url=url, params=params, auth=auth)
    return response
