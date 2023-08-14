from http import HTTPStatus

import allure
import pytest

from source.api.games.product_languages import product_languages
from source.base.generator import Generator
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.product_languages import ProductLanguages


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test post product languages')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Product languages cannot be created')
class TestProductLanguagesCreate:
    @allure.title(f'{Cases.GAMES["TG15"]["id"]}-Test product languages create')
    @allure.description('Проверка успешного ответа [201] при создании языка продукта.')
    @allure.testcase(name=Cases.GAMES["TG15"]["name"], url=Cases.GAMES["TG15"]["link"])
    def test_product_languages_create(self, delete_created_data):
        payload = Generator.object(model=ProductLanguages, seed=111)
        response = product_languages.create(json=payload)

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=ProductLanguages)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=product_languages.delete, id_data=id_data)
