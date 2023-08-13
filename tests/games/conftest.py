from http import HTTPStatus

import pytest

from source.api.games.genre import genres
from source.api.games.languages import languages
from source.api.games.product_languages import product_languages
from source.api.games.subgenre import subgenres
from source.api.games.system_requirement import system_requirements
from source.base.generator import Generator
from source.base.validator import assertions
from source.database.connection import Database
from source.enums.path import Path
from source.schemas.games.genre_schema import Genre
from source.schemas.games.laguage_schema import Language
from source.schemas.games.product_languages import ProductLanguages
from source.schemas.games.subgenre import Subgenre
from source.schemas.games.system_requirement import SystemRequirement


@pytest.fixture()
def db_games_connection():
    db_games = Database(path_settings=Path.GAMES_DB).connect()
    yield db_games
    db_games.close()


@pytest.fixture()
def create_delete_test_languages():
    payload = Generator.object(model=Language)
    response = languages.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    id_test = response.json().get('id')
    yield response
    response = languages.delete(id_data=id_test)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@pytest.fixture()
def create_test_languages():
    payload = Generator.object(model=Language)
    response = languages.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    return response


@pytest.fixture()
def create_delete_test_product_languages():
    payload = Generator.object(model=ProductLanguages)
    response = product_languages.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    id_test = response.json().get('id')
    yield response
    response = product_languages.delete(id_data=id_test)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@pytest.fixture()
def create_test_product_languages():
    payload = Generator.object(model=ProductLanguages)
    response = product_languages.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    return response


@pytest.fixture()
def create_delete_test_genre():
    payload = Generator.object(model=Genre)
    response = genres.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    id_test = response.json().get('id')
    yield response
    response = genres.delete(id_data=id_test)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@pytest.fixture()
def create_test_genre():
    payload = Generator.object(model=Genre)
    response = genres.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    return response


@pytest.fixture()
def create_delete_test_subgenre():
    payload = Generator.object(model=Subgenre)
    response = subgenres.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    id_test = response.json().get('id')
    yield response
    response = subgenres.delete(id_data=id_test)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@pytest.fixture()
def create_test_subgenre():
    payload = Generator.object(model=Subgenre)
    response = subgenres.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    return response


@pytest.fixture()
def create_delete_test_system_requirement():
    payload = Generator.object(model=SystemRequirement)
    response = system_requirements.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    id_test = response.json().get('id')
    yield response
    response = system_requirements.delete(id_data=id_test)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@pytest.fixture()
def create_test_system_requirement():
    payload = Generator.object(model=SystemRequirement)
    response = system_requirements.create(json=payload)
    assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
    return response
