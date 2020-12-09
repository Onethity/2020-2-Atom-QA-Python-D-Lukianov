import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase
from ui.pages.welcome_page import NoVkIdException


@allure.feature('UI')
@allure.story('Тестирование VK ID')
class TestVkId(BaseUITestCase):
    @allure.title('Vk id не отображается, если микросервис возвращает 404')
    @pytest.mark.UI
    def test_no_vk_id(self, welcome_page):
        """
        Проверяем, что если микросервис vk_id возвращает приложению 404,
        то Vk id пользователя не отображается

        Шаг 1. Авторизация

        Ожидаемое поведение: пункт списка <li>VK ID: <vk_id></li> не отображается
        """
        allure.attach(name='Vk id', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        with pytest.raises(NoVkIdException):
            welcome_page.get_vk_id()

    @allure.title('Vk id отображается корректно, если микросервис возвращает 200')
    @pytest.mark.UI
    def test_vk_id(self, new_user, mock_client, welcome_page):
        """
        Vk id должен отображаться, если микросервис возвращает 200

        Шаг 1. Добавялем vk_id пользователя в мок
        Шаг 2. Авторизуемся в приложении
        Шаг 3. Проверяем, что vk id отображается верно

        Ожидаемое поведение: на странице отображается VK ID: <vk_id>

        """
        username = new_user.username
        vk_id = '123456'
        mock_client.add_vk_id(username, vk_id)
        self.driver.refresh()

        allure.attach(name='Vk id', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert self.welcome_page.get_vk_id() == f'VK ID: {vk_id}', 'vk id из мока и в приложении не совпадают'
