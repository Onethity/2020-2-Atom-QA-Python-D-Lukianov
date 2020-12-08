import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Негативные кейсы на добавление пользователя')
class TestAddUserNegative(BaseApiTestCase):
    @allure.title('Запрос на API для добавления пользователя с невалидным username')
    @pytest.mark.API
    @pytest.mark.parametrize('username', ['', '123', 'a' * 20])
    def test_add_user_wrong_username(self, random_email, random_password, username):
        """
         Запрос на API для добавления пользователя с невалидным username (пустой или короткий)

         Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
        {
           "username": "" или "123",
           "password": "<random_password>",
           "email": "<random_email>"
        }

        Ожидаемое поведение: статус код 400, действие не выполнено
        """

        response = self.myapp_client.add_user(username, random_email, random_password)
        assert not self.mysql_client.builder.does_user_exist(username=username), 'Пользователь добавлен в базу'
        assert response.status_code == 400, 'Неверный код ответа'

    @allure.title('Запрос на API для добавления пользователя с невалидным password')
    @pytest.mark.API
    @pytest.mark.parametrize('password', ['', '1' * 270])
    def test_add_user_wrong_password(self, random_username, random_email, password):
        """
         Запрос на API для добавления пользователя с невалидным паролем (пустой или слишком длинный)

         Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
        {
           "username": "<random_username>",
           "password": '' или '123,
           "email": "<random_email>"
        }

        Ожидаемое поведение: статус код 400, действие не выполнено
        """

        response = self.myapp_client.add_user(random_username, random_email, password)
        assert not self.mysql_client.builder.does_user_exist(username=random_username), 'Пользователь добавлен в базу'
        assert response.status_code == 400, 'Неверный код ответа'

    @allure.title('Запрос на API для добавления пользователя с пустым и неверным форматом email')
    @pytest.mark.API
    @pytest.mark.parametrize('email', ['', 'wrong_email'])
    def test_add_user_wrong_email(self, random_username, random_password, email):
        """
         Запрос на API для добавления пользователя с пустым и неверным форматом email

         Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
        {
           "username": "<random_username>",
           "password": "<random_password>",
           "email": "wrong_email_format"
        }

        Ожидаемое поведение: статус код 400, действие не выполнено
        """

        response = self.myapp_client.add_user(random_username, email, random_password)
        assert not self.mysql_client.builder.does_user_exist(username=random_username), 'Пользователь добавлен в базу'
        assert response.status_code == 400, 'Неверный код ответа'
