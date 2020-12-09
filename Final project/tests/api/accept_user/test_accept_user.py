import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Разблокировка пользователя через api')
class TestAcceptUser(BaseApiTestCase):
    @allure.title('Разблокировка пользователя через API')
    @pytest.mark.API
    def test_accept_user(self, new_user):
        """
        Проверяем, что при api запросе на разблокировку,
         пользователь действительно разблокируется.

        Шаг 1. Создаем заблокированного пользователя <username>
        Шаг 2. Авторизуемся в API
        Шаг 3. GET запрос http://<app_url/api/accept_user/<username>

        Ожидаемое поведение:
            1. Ответ со статус кодом 200
            2. Текст ответа  = "User access granted!"
            3. Пользователю <username> проставляется access=1 в бд
        """
        username = new_user.username
        self.mysql_client.builder.block_user(username)

        response = self.myapp_client.accept_user(username)

        assert response.status_code == 200, 'Неверный статус код'
        assert response.text == 'User access granted!', 'Неверное тело ответа'
        assert self.mysql_client.builder.is_user_accepted(username), ('Пользователь не разблокирован',
                                                                      '(access != 1 в бд')

    @allure.title('Разблокировка незаблокированнового пользователя через API')
    @pytest.mark.API
    def test_accept_user(self, new_user):
        """
        Проверяем, что при api запросе на разблокировку,
         незаблокированного пользователя, статус код ответа 304

        Шаг 1. Создаем пользователя <username>
        Шаг 2. Авторизуемся в API
        Шаг 3. GET запрос http://<app_url/api/accept_user/<username>

        Ожидаемое поведение: ответ со статус кодом 304
        """
        username = new_user.username

        response = self.myapp_client.accept_user(username)
        assert response.status_code == 304, 'Неверный статус код'

    @allure.title('Разблокировка несуществующего пользователя через API отдает 404')
    @pytest.mark.API
    def test_accept_wrong_user(self):
        """
        Проверяем, что при api запросе на разблокировку,
         несуществующего пользователя, статус код ответа 404

        Шаг 2. Авторизуемся в API
        Шаг 3. GET запрос http://<app_url/api/accept_user/wrong_user

        Ожидаемое поведение: ответ со статус кодом 404 и текстом "User does not exist!"
        """
        response = self.myapp_client.accept_user('wrong_user')
        assert response.status_code == 404, 'Неверный статус код'
        assert response.text == "User does not exist!", 'Неверное тело ответа'

