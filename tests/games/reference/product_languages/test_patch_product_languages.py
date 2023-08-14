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
@allure.suite('Test patch product languages')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Product languages cannot be created')
class TestProductLanguagesPartialUpdate:
    @allure.title(f'{Cases.GAMES["TG18"]["id"]}-Test product languages partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении языка продукта')
    @allure.testcase(name=Cases.GAMES["TG18"]["name"], url=Cases.GAMES["TG18"]["link"])
    def test_product_languages_partial_update(self, create_delete_test_product_languages):
        id_test = create_delete_test_product_languages.json().get('id')

        payload = Generator.object(model=ProductLanguages, seed=2)
        response = product_languages.update_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=ProductLanguages)
        assertions.json_equal_json(actual=response.json(), expected=payload)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')
