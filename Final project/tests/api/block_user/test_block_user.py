import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Блокировка пользователя')
class TestBlockUser(BaseApiTestCase):
    @allure.title('Блокировка пользователя через API')
    @pytest.mark.API
    def test_block_user(self, new_user):
        """
        Проверяем, что при api запросе на блокировку, пользователь действительно блокируется.

        Шаг 1. Создаем пользователя <username>
        Шаг 2. Авторизуемся в API
        Шаг 3. GET запрос http://<app_url/api/block_user/<username>

        Ожидаемое поведение:
            1. Ответ со статус кодом 200
            2. Текст ответа  = "User was blocked!"
            3. Пользователю <username> проставляется access=0 в бд
        """
        username = new_user.username
        response = self.myapp_client.block_user(username)

        assert not self.mysql_client.builder.is_user_accepted(username), ('Пользователь не заблокирован '
                                                                          '(access != 0 в бд)')
        assert response.status_code == 200, 'Неверный статус код'
        assert response.text == 'User was blocked!', 'Неверное тело ответа'

    @allure.title('Блокировка несуществующего пользователя через API')
    @pytest.mark.API
    def test_block_user_negative(self):
        """
        Проверяем, что при api запросе на блокировку несуществующего
         пользователя, возвращается ответ 404

        Шаг 2. Авторизуемся в API
        Шаг 3. GET запрос http://<app_url>/api/block_user/wrong_user_name

        Ожидаемое поведение: ответ со статус кодом 404 и текстом "User does not exist!"
        """
        response = self.myapp_client.block_user('wrong_user_name')

        assert response.status_code == 404, 'Неверный статус код'
        assert response.text == 'User does not exist!', 'Неверное тело ответа'

    @allure.title('API блокировка уже заблокированного пользователя')
    @pytest.mark.API
    def test_block_blocked_user(self, new_user):
        """
        Проверяем, что при api запросе на блокировку уже заблокированного пользователя,
            возвращается ответ 304

        Шаг 1. Создаем пользователя <username>
        Шаг 2. Блокируем его
        Шаг 3. Авторизуемся в API
        Шаг 4. GET запрос http://<app_url/api/block_user/<username>

        Ожидаемое поведение:
            1. Ответ со статус кодом 304
        """
        username = new_user.username
        self.mysql_client.builder.block_user(username)

        response = self.myapp_client.block_user(username)
        assert response.status_code == 304, 'Неверный статус код'
