import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Пользователь заблокирован')
class TestAccess(BaseUITestCase):
    @allure.title('Пользователю с access=False запрещен вход')
    @pytest.mark.UI
    def test_user_block(self, new_user):
        """
        Проверяем, что пользователю с access=False запрещен вход

        Шаг 1. Создаем пользователя
        Шаг 2. Блокируем его (access=0 в бд)
        Шаг 3. Открываем форму авторизации, вводим логин и пароль

        Ожидаемое поведение: flash сообщение "Your account is blocked" на английском! языке
        """
        self.mysql_client.builder.block_user(new_user.username)
        self.login_page.auth(new_user.username, new_user.password)

        allure.attach(name='Login error', body=self.login_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)
        assert self.login_page.get_flash_message_text() == 'Your account is blocked', \
            'Неверное сообщение о блокировке, оно должно быть на английском языке'
