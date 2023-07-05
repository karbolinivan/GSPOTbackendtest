import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.payments.payments import External_Payments


# @allure.step('Get languages with id "{id_data}"')
# def get_languages(id_data: int, auth=tester_auth):
#     url = f'{Reference.LANGUAGES}{id_data}'
#     response = Requests.get(url=url, auth=auth)
#     return response


@allure.step('Get services list')
def get_services_list(auth=None):
    response = Requests.get(url=External_Payments.SERVICES, auth=auth)
    return response





# @allure.step('Create a language')
# def create_languages(json, auth=tester_auth):
#     response = Requests.post(url=Reference.LANGUAGES, json=json, auth=auth)
#     return response
#
#
# @allure.step('Update the language with id "{id_data}"')
# def update_languages(id_data: int, json, auth=tester_auth):
#     url = f'{Reference.LANGUAGES}{id_data}/'
#     response = Requests.put(url=url, json=json, auth=auth)
#     return response
#
#
# @allure.step('Update the language partly with id "{id_data}"')
# def update_languages_partly(id_data: int, json, auth=tester_auth):
#     url = f'{Reference.LANGUAGES}{id_data}/'
#     response = Requests.patch(url=url, json=json, auth=auth)
#     return response
#
#
# @allure.step('Delete the language with id "{id_data}"')
# def delete_languages(id_data: int, auth=tester_auth):
#     url = f'{Reference.LANGUAGES}{id_data}'
#     response = Requests.delete(url=url, auth=auth)
#     return response
