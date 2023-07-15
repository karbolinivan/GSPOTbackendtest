import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Core


@allure.step('Get the product by id "{id_data}"')
def get_product(id_data: str, auth=tester_auth):
    url = f'{Core.PRODUCT}{id_data}'
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Get product list')
def get_product_list(auth=tester_auth, params=None):
    response = Requests.get(url=Core.PRODUCT, params=params, auth=auth)
    return response


@allure.step('Create a product')
def create_system_requirement(json, auth=tester_auth):
    response = Requests.post(url=Core.PRODUCT, json=json, auth=auth)
    return response


@allure.step('Update the product with id "{id_data}"')
def update_product(id_data: str, json, auth=tester_auth):
    url = f'{Core.PRODUCT}{id_data}/'
    response = Requests.put(url=url, json=json, auth=auth)
    return response


@allure.step('Update the product partly with id "{id_data}"')
def update_product_partly(id_data: str, json, auth=tester_auth):
    url = f'{Core.PRODUCT}{id_data}/'
    response = Requests.patch(url=url, json=json, auth=auth)
    return response


@allure.step('Delete the product with id "{id_data}"')
def delete_product(id_data: str, auth=tester_auth):
    url = f'{Core.PRODUCT}{id_data}'
    response = Requests.delete(url=url, auth=auth)
    return response
