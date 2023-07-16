import json

import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.payments.payments import External_Payments


@allure.step('Get services list')
def get_services_list(auth=None):
    response = Requests.get(url=External_Payments.SERVICES, auth=auth)
    return response

@allure.step('Create service')
def create_service(json, auth=None, name=""):
    response = Requests.post(url=External_Payments.SERVICES, json=json, auth=auth)
    return response

@allure.step('Delete service')
def delete_service(service_id, auth=None):
    url = f"{External_Payments.SERVICES}{service_id}/"
    response = Requests.delete(url=url, auth=auth)
    return response


def test_delete_all():
    response = get_services_list()
    parsed_data = json.loads(response.text)

    for item in parsed_data:
        service_id = item['id']
        r = delete_service(service_id)
        print(f"Deleted service with ID {service_id}. Status code: {r.status_code}")

