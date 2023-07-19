import pytest


def _create_data(api, json):
    response = api(json=json)
    assert response.status_code == 201, f'\nTest data was not created'


@pytest.fixture
def create_data():
    return _create_data


def _delete_created_data(api, id_data):
    response_delete = api(id_data=id_data)
    assert response_delete.status_code == 204


@pytest.fixture
def delete_created_data():
    return _delete_created_data


def pytest_make_parametrize_id(config, val):
    return repr(val)
