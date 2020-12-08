import allure
import pytest

from api.client.myapp_client import MyappApiClient
from db.mysql_client import MysqlConnection


@allure.feature('API')
@allure.story('Запросы с неавторизованного пользователя')
class TestUnauthorizedUser:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, myapp_api_client_no_auth, db_connection):
        self.myapp_client: MyappApiClient = myapp_api_client_no_auth
        self.mysql_client: MysqlConnection = db_connection

    @allure.title('Запрос на добавление пользователя через API без авторизации')
    @pytest.mark.API
    def test_add_user_no_auth(self, random_username, random_password, random_email):
        """
        Проверяем, что API запрос без авторизации на добавление пользователя возвращает 401
            и не добавляет пользователя.

        Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
            {
               "username": "<random_username>",
               "password": "<random_password>",
               "email": "<random_email>"
            }

        Ожидаемое поведение:
            1. Статус код 401
            2. Пользователь не добавлен
        """
        response = self.myapp_client.add_user(random_username, random_password, random_email)
        assert response.status_code == 401, 'Неверный статус код'
        assert not self.mysql_client.builder.does_user_exist(random_username), 'Пользователь добавлен'

    @allure.title('Запрос на удаление пользователя через API без авторизации')
    @pytest.mark.API
    def test_del_user_no_auth(self, new_user):
        """
        Проверям, что GET запрос без авторизации
         на /api/del_user/<username> не удаляет пользователя и отдает 401

        Шаг 1. GET запрос /api/del_user/<random_username>

        Ожидаемое поведение:
            1. Запрос возвращает 401
            2. Пользователь не удален из базы

        """
        username = new_user.username
        response = self.myapp_client.del_user(username)

        assert response.status_code == 401, 'Неверный код ответа'
        assert self.mysql_client.builder.does_user_exist(username), 'Пользователь не удален из базы'

    @allure.title('Запрос на разблокировку пользователя через API без авторизации')
    @pytest.mark.API
    def test_accept_user_no_auth(self, new_user):
        """
        Проверяем, что при api запросе без авторизации на разблокировку пользователя,
         статус код ответа 401 и пользователь не разблокирован

        Шаг 1. Создаем заблокированного пользователя <username>
        Шаг 3. GET запрос http://<app_url/api/accept_user/<username>

        Ожидаемое поведение: ответ со статус кодом 401, пользователь не разблокирован
        """
        username = new_user.username
        self.mysql_client.builder.block_user(username)

        response = self.myapp_client.accept_user(username)

        assert response.status_code == 401, 'Неверный статус код'
        assert not self.mysql_client.builder.is_user_accepted(username), ('Пользователь разблокирован',
                                                                          '(access == 1 в бд')

    @allure.title('Запрос на блокировку пользователя через API без авторизации')
    @pytest.mark.API
    def test_block_user_no_auth(self, new_user):
        """
        Проверяем, что при api запросе на блокировку без авториации,
         возвращается статус код 401 и пользователь не блокируется

        Шаг 1. Создаем пользователя <username>
        Шаг 2. GET запрос http://<app_url/api/block_user/<username>

        Ожидаемое поведение:
            1. Ответ со статус кодом 401
            3. Пользователь <username> не блокируется (access==1 в бд)


        """
        username = new_user.username
        response = self.myapp_client.block_user(username)

        assert self.mysql_client.builder.is_user_accepted(username), ('Пользователь заблокирован '
                                                                      '(access == 0 в бд)')
        assert response.status_code == 401, 'Неверный статус код'
