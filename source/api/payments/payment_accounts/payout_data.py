import allure

from source.base.client import Requests
from source.enums.payments.payments import Payment_Accounts


@allure.step('Delete payout data')
def delete_payout_data(uuid, auth=None):
    url = f"{Payment_Accounts.PAYOUT_DATA}{uuid}/"
    response = Requests.delete(url=url, auth=auth)
    return response
