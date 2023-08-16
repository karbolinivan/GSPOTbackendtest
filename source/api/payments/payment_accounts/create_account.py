import allure

from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts


@allure.step('Create account')
def create_account(json, auth=None):
    response = Requests.post(url=Payment_Accounts.CREATE_ACCOUNT, auth=auth, json=json)
    return response