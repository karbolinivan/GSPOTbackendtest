from http import HTTPStatus

import allure
import pytest

from source.base.generator import Generator
from source.api.games.languages import languages
from source.enums.data import Cases
from source.schemas.games.laguage_schema import Language
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test patch languages')
@pytest.mark.smoke
class TestLanguagesPartialUpdate:
    @allure.title(f'{Cases.GAMES["TG95"]["id"]} Test languages partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении языка')
    @allure.testcase(name=Cases.GAMES["TG95"]["name"], url=Cases.GAMES["TG95"]["link"])
    def test_languages_partial_update(self, create_delete_test_languages):
        id_test = create_delete_test_languages.json().get('id')

        payload = Generator.object(model=Language, seed=2)
        response = languages.update_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Language)
        assertions.json_equal_json(actual=response.json(), expected=payload)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')
