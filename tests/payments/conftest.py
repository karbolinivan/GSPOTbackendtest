import pytest

from source.api.payments.external_payments_services import create_service, delete_service
from source.api.payments.payment_accounts.owner import update_owner, update_owner_partial
from source.base.generator import Generator
from source.base.validator import assert_status_code
from source.schemas.payments.external_payments.services_schema import Payments_Services
from source.schemas.payments.payment_accounts.owner_schema import PaymentData


@pytest.fixture()
def create_delete_test_payment_service():
    payload = Generator.object(model=Payments_Services)
    response = create_service(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_service(id_data=id_test)
    assert_status_code(response=response, expected=204)

@pytest.fixture()
def create_test_payment_service():
    payload = Generator.object(model=Payments_Services)
    response = create_service(json=payload)
    assert_status_code(response=response, expected=201)
    return response

@pytest.fixture()
def update_test_payment_owner():
    payload = Generator.object(model=PaymentData)
    response = update_owner(json=payload)
    assert_status_code(response=response, expected=200)
    return response
