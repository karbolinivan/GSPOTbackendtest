import allure

from source.base.client import client
from source.enums.payments.payments import Payment_Accounts


class Payout:
    def __init__(self, auth=None):
        self.client = client
        self.auth = auth

    @allure.step('Get payout data uuid')
    def get_payout_data_uuid(self, uuid_data, auth=None):
        url = f"{Payment_Accounts.PAYOUT_DATA}{uuid_data}/"
        response = self.client.get(url=url, auth=auth)
        return response

    @allure.step('Create payout')
    def create_payout(self, json, auth=None):
        url = Payment_Accounts.PAYOUT
        response = self.client.post(url=url, json=json, auth=auth)
        return response

    @allure.step('Create payout data')
    def create_payout_data(self, json, auth=None):
        url = Payment_Accounts.PAYOUT_DATA
        response = self.client.post(url=url, json=json, auth=auth)
        return response

    @allure.step('Update payout data uuid')
    def update_payout_data_uuid(self, uuid_data, json, auth=None):
        url = f"{Payment_Accounts.PAYOUT_DATA}{uuid_data}/"
        response = self.client.put(url=url, json=json, auth=auth)
        return response

    @allure.step('Partial update payout data uuid')
    def update_payout_data_uuid_partial(self, uuid_data, json, auth=None):
        url = f"{Payment_Accounts.PAYOUT_DATA}{uuid_data}/"
        response = self.client.patch(url=url, json=json, auth=auth)
        return response

    @allure.step('Delete payout data uuid')
    def delete_payout_data_uuid(self, uuid_data, auth=None):
        url = f"{Payment_Accounts.PAYOUT_DATA}{uuid_data}/"
        response = self.client.delete(url=url, auth=auth)
        return response


payout = Payout()
