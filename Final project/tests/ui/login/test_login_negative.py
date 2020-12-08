import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Негативные кейсы на авторизацию')
class TestLoginNegative(BaseUITestCase):
    @allure.title('Негативный тест на авторизацию с несуществующими username и password.')
    @pytest.mark.UI
    def test_auth_negative(self):
        """
        Негативный тест на авторизацию с несуществующими username и password.

        Шаг 1. Переход на /
        Шаг 2. Вводим в поле username "wrong_username"
        Шаг 3. Вводим в поле password "wrong_password"
        Шаг 4. Нажимаем кнопку "LOGIN"

        Ожидаемое поведение: вывод flash сообщения "Invalid username or password"
        """
        self.login_page.auth(
            username='wrong_username',
            password='wrong_password'
        )

        allure.attach(name='Login error', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)
        assert self.login_page.get_flash_message_text() == 'Invalid username or password', \
            'Неверное сообщение об ошибке'

    @allure.title('Негативный тест на авторизацию с некорректной длиной username')
    @pytest.mark.UI
    @pytest.mark.parametrize('username', ['aaa', 'a' * 17])
    def test_auth_username_length(self, username):
        """
        Негативный тест на авторизацию с некорректной длиной username

        Шаг 1. Переход на /
        Шаг 2. Вводим в поле username 3 символа (слишком мало) или 17 символов (слишком много)
        Шаг 3. Вводим в поле password "123"

        Ожидаемое поведение: вывод flash сообщения "Incorrect username length"
        """
        self.login_page.auth(
            username=username,
            password='123'
        )

        allure.attach(name='Login error', body=self.login_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)
        assert self.login_page.get_flash_message_text() == 'Incorrect username length', 'Неверное сообщение об ошибке'
