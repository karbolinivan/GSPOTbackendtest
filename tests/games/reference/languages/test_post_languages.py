import allure
import pytest

from source.base.generator import Generator
from source.schemas.laguage_schema import Language
from source.api.languages import create_languages, delete_languages
from source.base.validator import assert_json_by_model, assert_json_key_value, assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test post languages')
@pytest.mark.smoke
class TestLanguagesCreate:

    @allure.title('Test languages create')
    @allure.description('Проверка успешного ответа [201] при создании языка.')
    def test_languages_create(self, delete_created_data):
        payload = Generator.object(model=Language, seed=1, exclude='id')
        response = create_languages(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_languages, id_data=id_data)
