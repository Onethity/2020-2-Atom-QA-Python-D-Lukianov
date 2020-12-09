import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Удаление пользователя')
class TestDelUser(BaseApiTestCase):
    @allure.title('/api/del_user действительно удаляет пользователя')
    @pytest.mark.API
    def test_del_user(self, new_user):
        """
        Проверям, что GET запрос на /api/del_user/<username> удаляет пользователя

        Шаг 1. Авторизация в API
        Шаг 2. Добавление пользователя <username> в базу
        Шаг 3. GET запрос /api/del_user/<username>

        Ожидаемое поведение:
            1. Запрос возвращает 204
            2. Текст ответа "User was deleted!"
            3. Пользователя <username> нет в базе

        """
        username = new_user.username
        response = self.myapp_client.del_user(username)

        assert not self.mysql_client.builder.does_user_exist(username), 'Пользователь не удален из базы'
        assert response.status_code == 204, 'Неверный код ответа'
        assert response.text == 'User was deleted!', 'Неверное тело ответа'

    @allure.title('/api/del_user возвращает 404 на невалидном пользователе')
    @pytest.mark.API
    @pytest.mark.parametrize('username', ['wrong_user_name', ''])
    def test_del_user_negative(self, username):
        """
        Проверям, что GET запрос на /api/del_user/<username> отдает 404 на несуществующем username

        Шаг 1. Авторизация в API
        Шаг 2. GET запрос /api/del_user/wrong_user_name

        Ожидаемое поведение: запрос возвращает 404 и текст "User does not exist!"

        """
        response = self.myapp_client.del_user('wrong_user_name')

        assert response.status_code == 404, 'Неверный код ответа'
        assert response.text == 'User does not exist!', 'Неверное тело ответа'
