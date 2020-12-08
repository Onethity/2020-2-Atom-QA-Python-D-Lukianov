import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Активность пользователя')
class TestActive(BaseApiTestCase):

    @allure.title('Для залогиненого пользователя active = True')
    @pytest.mark.API
    def test_active_user(self):
        """
        Проверка на то, что для авторизованного пользователя значение
         active в базе данных равно 1

        Шаг 1. Авторизация через post запрос

        Ожидаемое поведение: для данного пользователя поле active в базе данных равно 1
        """
        assert self.mysql_client.builder.is_user_active(
            username=self.myapp_client.username,
        ), 'Пользователь не активен (active != 1 в бд)'

    @allure.title('Если пользователь выходит, то его active = False')
    @pytest.mark.API
    def test_deactivate_user(self):
        """
        Проверка на то, что если пользователь нажал Logout, то
         active в базе данных равно 0

        Шаг 1. Авторизация через post запрос
        Шаг 2. GET запрос на logout

        Ожидаемое поведение: для данного пользователя поле active в базе данных равно 0
        """
        self.myapp_client.logout()
        assert not self.mysql_client.builder.is_user_active(
            username=self.myapp_client.username,
        ), 'Пользователь активнен (active = 1 в бд)'
