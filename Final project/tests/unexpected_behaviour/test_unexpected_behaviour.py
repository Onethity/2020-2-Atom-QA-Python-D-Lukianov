import allure
import pytest

from bs4 import BeautifulSoup


class NoFlashMessageException(Exception):
    pass


@allure.feature('Unexpected behaviour')
@allure.story('Тест кейсы на необычное поведение пользователя ')
class TestUnexpectedBehaviour:
    @allure.title('Плохой запрос на авторизацию после успешной авторизации')
    def test_login_twice(self, myapp_api_client):
        """
        Отправка невалидного запроса на авторизацию без пароля в случае, если
        пользователь уже авторизован

        Шаг 1. Авторизация
        Шаг 2. Невалидный POST запрос на /login
            Body:
                username:test123
                submit:Login

        Ожидаемое поведение: на странице welcome не должен
         отображается <div id="flash> с ошибкой
        """

        myapp_api_client.auth()  # Авторизовались

        # Теперь авторизуемся еще раз
        myapp_api_client.password = None  # Но уже не отправляем пароль
        response = myapp_api_client.auth()
        welcome_page_text = response.text

        with pytest.raises(NoFlashMessageException):
            # Никакого flash сообщения тут быть не должно!
            self._get_flash_message_text(welcome_page_text)

    @allure.title('Принудительная отправка неправильного запроса (без password) на авторизацию'
                  ' в обход браузерной валидации')
    def test_login_no_password(self, myapp_api_client_no_auth):
        """
        Отправка невалидного запроса на авторизацию (без поля password) в обход клиентской валидации.

        Шаг 1. Отправляем POST запрос на /login
            Body:
                username:some_username
                submit:Login

        Ожидаемое поведение: flash сообщение с текстом на АНГЛИЙСКОМ языке
        """
        myapp_api_client_no_auth.username = 'some_username'
        myapp_api_client_no_auth.password = None
        response = myapp_api_client_no_auth.auth()

        assert self._get_flash_message_text(response.text) == 'You must fill password field', \
            'Текст сообщения должен быть на английском'

    @allure.title('Принудительная отправка неправильного запроса (без username) на авторизацию'
                  ' в обход браузерной валидации')
    def test_login_no_username(self, myapp_api_client_no_auth):
        """
        Отправка невалидного запроса на авторизацию (без поля password) в обход клиентской валидации.

        Шаг 1. Отправляем POST запрос на /login
            Body:
                password:some_password
                submit:Login

        Ожидаемое поведение: flash сообщение с текстом на АНГЛИЙСКОМ языке
        """
        myapp_api_client_no_auth.username = None
        myapp_api_client_no_auth.password = 'some_password'
        response = myapp_api_client_no_auth.auth()

        assert self._get_flash_message_text(response.text) == 'You must fill username field', \
            'Текст сообщения должен быть на английском'

    def _get_flash_message_text(self, html):
        soup = BeautifulSoup(html, 'lxml')
        flash_message = soup.find('div', {'id': 'flash'})

        if flash_message is None:
            raise NoFlashMessageException

        return flash_message.text
