import allure

from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts


@allure.step('Get balance by id')
def get_balance(user_uuid, auth=None):
    url = f"{Payment_Accounts.BALANCES}{user_uuid}/"
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Post balance')
def post_balance(json, auth=None):
    response = Requests.post(url=Payment_Accounts.BALANCES, auth=auth, json=json)
    return response