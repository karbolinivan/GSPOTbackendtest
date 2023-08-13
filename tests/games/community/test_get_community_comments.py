import allure
import pytest

from source.api.games.community import community
from source.base.validator import assertions
from source.enums.data import Cases
from http import HTTPStatus


@allure.epic('Games')
@allure.feature('Community')
@allure.story('Comments')
@allure.suite('Test get community comments')
@pytest.mark.smoke
class TestCommunityComments:
    @allure.title(f'{Cases.GAMES["TG1"]["id"]}-Test community comments read')
    @allure.description('Проверка успешного ответа [200] при запросе коментариев пользователей.')
    @allure.testcase(name=Cases.GAMES["TG1"]["name"], url=Cases.GAMES["TG1"]['link'])
    def test_community_comments_read(self):
        id_test = 1
        response = community.comments_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
