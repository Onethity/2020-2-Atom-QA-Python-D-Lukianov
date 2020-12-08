import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Тесты страницы 404')
class Test404(BaseUITestCase):
    @allure.title('На странице 404 ошибки есть изображение и текст ошибки')
    @pytest.mark.UI
    def test_404(self):
        """
        Проверяем, что страница с 404 ошибкой отображается корректно

        Шаг 1. Переход на http://<app_url>/wrong_page

        Ожидаемое поведение:
            1. Текст ошибки - Page Not Found
            2. Отображается изображение из /static/images/404_errors/

        """
        error_404_page = self.login_page.go_to_404()

        allure.attach(name='404 error page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert error_404_page.get_error_text() == 'Page Not Found', 'Неверный текст ошибки'
        assert '/static/images/404_errors/' in error_404_page.get_error_img_src(), 'Неправильное изображение'
