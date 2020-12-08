import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Авторизация пользователя')
class TestLogin(BaseUITestCase):
    @pytest.fixture(scope='function', autouse=True)
    def set_user(self, new_user):
        self.username = new_user.username
        self.password = new_user.password

    @allure.title('Позитивный тест на авторизацию')
    @pytest.mark.UI
    def test_login_positive(self):
        """
        Позитивный тест на авторизацию.

        Шаг 1. Создаем пользователя в бд.
        Шаг 2. Переходим на главную страницу
        Шаг 3. Заполняем поле username
        Шаг 4. Заполняем поле password
        Шаг 5. Нажимаем кнопку LOGIN

        Ожидаемое поведение: на странице есть блок "Logged as <username>"
        """
        self.login_page.auth(self.username, self.password)

        allure.attach(name='Welcome page', body=self.login_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)
        assert self.welcome_page.get_logged_as() == f'Logged as {self.username}', 'Не найден блок Logged as'

    @allure.title('Проверка заголовка страницы авторизации')
    @pytest.mark.UI
    def test_login_page_title(self):
        """
        Проверяем, что у страницы логина заполнен тег <title>

        Шаг 1. Переходим на /

        Ожидаемое поведение: заголовок страницы не пустой
        """
        assert self.driver.title != '', 'Пустой <title> у страницы'
