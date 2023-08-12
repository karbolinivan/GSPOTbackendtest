import allure

from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts

@allure.step('Get owner list')
def get_owner_list():
    url = Payment_Accounts.OWNER
    response = Requests.get(url=url)
    return response

@allure.step('Update owner')
def update_owner(json):
    url = Payment_Accounts.OWNER
    response = Requests.put(url=url, json=json)
    return response

@allure.step('Partial update owner')
def update_owner_partial(json):
    url = Payment_Accounts.OWNER
    response = Requests.patch(url=url, json=json)
    return response
