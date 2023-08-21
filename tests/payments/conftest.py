import pytest

from source.api.payments.external_payments_services import create_service, delete_service
from source.api.payments.payment_accounts.payout import payout
from source.api.payments.payment_accounts.owner import update_owner
from source.base.generator import Generator
from source.base.validator import assert_status_code
from source.schemas.payments.external_payments.services_schema import Payments_Services
from source.schemas.payments.payment_accounts.payout_data_schema import PayoutData
from source.schemas.payments.payment_accounts.owner_schema import PaymentData
from source.base.validator import assertions
from source.api.payments.payment_accounts.constants import user_uuid


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
def create_delete_test_payment_payout_data():
    payload = Generator.object(model=PayoutData, user_uuid=user_uuid)
    response = payout.create_payout_data(json=payload)
    assertions.status_code(actual=response.status_code, expected=201)
    uuid_test = response.json().get('user_uuid')
    yield response
    response = payout.delete_payout_data_uuid(uuid_data=uuid_test)
    assertions.status_code(actual=response.status_code, expected=204)


@pytest.fixture()
def update_test_payment_owner_payout_day():
    payload = Generator.object(model=PaymentData)
    response = update_owner(json=payload)
    assertions.status_code(actual=response.status_code, expected=200)
    return response
