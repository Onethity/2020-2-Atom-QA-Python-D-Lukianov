import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Регистрация пользователя')
class TestRegistration(BaseUITestCase):
    @allure.title('Позитивный тест на регистрацию')
    @pytest.mark.UI
    def test_registration(self, random_username, random_password, random_email):
        """
        Позитивный тест на регистрацию.

        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username случайным именем
        Шаг 3. Заполняем поле email случайным адресом
        Шаг 4. Заполняем password случайным паролем
        Шаг 5. Заполняем password repeat тем же самым паролем
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: после редиректа на welcome page есть блок "Logged as {username}"
            и пользователь добавлен в бд
        """
        registration_page = self.login_page.go_to_registration_page()

        registration_page.registration(random_username, random_password, random_email)

        allure.attach(name='Welcome page', body=self.registration_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)

        assert self.welcome_page.get_logged_as() == f'Logged as {random_username}', 'Не найден блок Logged as'
        assert self.mysql_client.builder.does_user_exist(random_username), 'Пользователь не существует в БД'
