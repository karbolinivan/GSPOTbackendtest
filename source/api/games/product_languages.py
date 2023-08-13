import allure

from constants import tester_auth
from source.base.client import client
from source.enums.games import Reference


class ProductLanguages:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth if auth else tester_auth

    @allure.step('Get the product language by id "{id_data}"')
    def get_id(self, id_data: int):
        url = f'{Reference.PRODUCT_LANGUAGES}{id_data}/'
        response = self.client.get(url=url, auth=self.auth)
        return response

    @allure.step('Get product languages list')
    def get_list(self, limit: int = None, offset: int = None):
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self.client.get(url=Reference.PRODUCT_LANGUAGES, params=params, auth=self.auth)
        return response

    @allure.step('Create a product language')
    def create(self, json):
        response = self.client.post(url=Reference.PRODUCT_LANGUAGES, json=json, auth=self.auth)
        return response

    @allure.step('Update the product language with id "{id_data}"')
    def update(self, id_data: int, json):
        url = f'{Reference.PRODUCT_LANGUAGES}{id_data}/'
        response = self.client.put(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Update the product language partly with id "{id_data}"')
    def update_partly(self, id_data: int, json):
        url = f'{Reference.PRODUCT_LANGUAGES}{id_data}/'
        response = self.client.patch(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Delete the product language with id "{id_data}"')
    def delete(self, id_data: int):
        url = f'{Reference.PRODUCT_LANGUAGES}{id_data}'
        response = self.client.delete(url=url, auth=self.auth)
        return response


product_languages = ProductLanguages()
