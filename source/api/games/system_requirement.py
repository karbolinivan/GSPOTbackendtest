import allure

from constants import tester_auth
from source.base.client import client
from source.enums.games import Core


class SystemRequirements:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth if auth else tester_auth

    @allure.step('Get the system requirement by id "{id_data}"')
    def get_id(self, id_data: str):
        url = f'{Core.SYSTEM_REQUIREMENT}{id_data}'
        response = self.client.get(url=url, auth=self.auth)
        return response

    @allure.step('Get system requirement list')
    def get_list(self, limit: int = None, offset: int = None):
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self.client.get(url=Core.SYSTEM_REQUIREMENT, params=params, auth=self.auth)
        return response

    @allure.step('Create a system requirement')
    def create(self, json):
        response = self.client.post(url=Core.SYSTEM_REQUIREMENT, json=json, auth=self.auth)
        return response

    @allure.step('Update the system requirement with id "{id_data}"')
    def update(self, id_data: str, json):
        url = f'{Core.SYSTEM_REQUIREMENT}{id_data}/'
        response = self.client.put(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Update the system requirement partly with id "{id_data}"')
    def update_partly(self, id_data: str, json):
        url = f'{Core.SYSTEM_REQUIREMENT}{id_data}/'
        response = self.client.patch(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Delete the system requirement with id "{id_data}"')
    def delete(self, id_data: str):
        url = f'{Core.SYSTEM_REQUIREMENT}{id_data}'
        response = self.client.delete(url=url, auth=self.auth)
        return response


system_requirements = SystemRequirements()
