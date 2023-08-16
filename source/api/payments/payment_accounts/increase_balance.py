import allure

from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts


@allure.step('Increase balance')
def increase_balance(json, auth=None):
    response = Requests.post(url=Payment_Accounts.INCREASE_BALANCE, auth=auth, json=json)
    return response


@allure.step('Delete balance')
def delete_balance(id_data, auth=None):
    url = f"{Payment_Accounts.INCREASE_BALANCE}{id_data}/"
    response = Requests.delete(url=url, auth=auth)
    return response