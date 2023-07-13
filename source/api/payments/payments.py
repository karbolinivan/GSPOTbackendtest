import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.payments.payments import External_Payments


@allure.step('Get services list')
def get_services_list(auth=tester_auth):
    response = Requests.get(url=External_Payments.SERVICES, auth=auth)
    return response

@allure.step('Create service')
def create_service(json, auth=tester_auth, name=""):
    response = Requests.post(url=External_Payments.SERVICES, json=json, auth=auth)
    return response

@allure.step('Delete service')
def delete_service(service_id, auth=tester_auth):
    url = f"{External_Payments.SERVICES}/{service_id}"
    response = Requests.delete(url=url, auth=auth)
    return response