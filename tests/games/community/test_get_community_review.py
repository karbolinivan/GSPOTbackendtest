from http import HTTPStatus

import allure
import pytest

from source.api.games.community import community
from source.base.validator import assertions
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Community')
@allure.story('Review')
@allure.suite('Test get community review')
@pytest.mark.smoke
class TestCommunityReview:
    @allure.title(f'{Cases.GAMES["TG2"]["id"]}-Test community review read')
    @allure.description('Проверка успешного ответа [200] при запросе обзора пользователей.')
    @allure.testcase(name=Cases.GAMES["TG2"]["name"], url=Cases.GAMES["TG2"]["link"])
    def test_community_review_read(self):
        id_test = '6f98f5fe-8b36-4bc8-874e-0feeb910747a'
        response = community.review_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
