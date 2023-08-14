import allure

from constants import tester_auth
from source.base.client import client
from source.enums.games import Core


class Products:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth if auth else tester_auth

    @allure.step('Get the product by id "{id_data}"')
    def get_id(self, id_data: str):
        url = f'{Core.PRODUCT}{id_data}'
        response = self.client.get(url=url, auth=self.auth)
        return response

    @allure.step('Get product list')
    def get_list(self, params=None):
        response = self.client.get(url=Core.PRODUCT, params=params, auth=self.auth)
        return response

    @allure.step('Create a product')
    def create(self, json):
        response = self.client.post(url=Core.PRODUCT, json=json, auth=self.auth)
        return response

    @allure.step('Update the product with id "{id_data}"')
    def update(self, id_data: str, json):
        url = f'{Core.PRODUCT}{id_data}/'
        response = self.client.put(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Update the product partly with id "{id_data}"')
    def update_partly(self, id_data: str, json):
        url = f'{Core.PRODUCT}{id_data}/'
        response = self.client.patch(url=url, json=json, auth=self.auth)
        return response

    @allure.step('Delete the product with id "{id_data}"')
    def delete(self, id_data: str):
        url = f'{Core.PRODUCT}{id_data}'
        response = self.client.delete(url=url, auth=self.auth)
        return response


products = Products()
