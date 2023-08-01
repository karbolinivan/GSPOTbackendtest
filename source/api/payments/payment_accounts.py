import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts


@allure.step('Get balance by id')
def get_balance(user_uuid, auth=None):
    url = f"{Payment_Accounts.BALANCES}{user_uuid}/"
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Increase balance')
def increase_balance(auth=None):
    response = Requests.post(url=Payment_Accounts.INCREASE_BALANCE, auth=auth)
    return response


@allure.step('Delete balance')
def delete_balance(id_data, auth=None):
    url = f"{Payment_Accounts.INCREASE_BALANCE}{id_data}/"
    response = Requests.delete(url=url, auth=auth)
    return response


@allure.step('Create account')
def create_account(json, auth=None):
    response = Requests.post(url=Payment_Accounts.CREATE_ACCOUNT, auth=auth, json=json)
    return response


@allure.step('Delete payout data')
def delete_payout_data(uuid, auth=None):
    url = f"{Payment_Accounts.PAYOUT_DATA}{uuid}/"
    response = Requests.delete(url=url, auth=auth)
    return response
