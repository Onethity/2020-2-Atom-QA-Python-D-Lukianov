import urllib.parse

import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Тесты на logout')
class TestLogout(BaseUITestCase):
    @allure.title('После нажатия кнопки Logout открывается форма авторизации')
    @pytest.mark.UI
    def test_logout(self, welcome_page):
        """
        Проверка на то, что после нажатия кнопки Logout открывается форма авторизации

        Шаг 1. Авторизация
        Шаг 2. Нажимаем кнопку Logout

        Ожидаемое поведение: открывается форма авторизации
        """
        welcome_page.click_to_logout()

        allure.attach(name='auth_form', body=self.login_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)
        assert "Welcome to the TEST SERVER" in self.driver.page_source, \
            'Редирект должен быть на форму авторизации'

    @allure.title('Эндпоинт /welcome недоступен неавторизованным пользователям')
    @pytest.mark.UI
    def test_unauthorized(self, app_full_url):
        """
        Проверяем, что http://<app_url>/welcome доступен только авторизованным пользователям

        Шаг 1. Заходим на /welcome без авторизации

        Ожидаемое поведение: flash сообщение "This page is available only to authorized users"
        """

        self.driver.get(urllib.parse.urljoin(app_full_url, '/welcome'))

        allure.attach(name='Page not available error', body=self.login_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)
        assert self.login_page.get_flash_message_text() == 'This page is available only to authorized users', \
            'Неверное сообщение об ошибке'
