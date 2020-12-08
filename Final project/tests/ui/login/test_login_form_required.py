import allure
import pytest

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Валидация формы авторизации')
class TestRequired(BaseUITestCase):
    @allure.title('Поля username и password обязательны для заполнения')
    @pytest.mark.UI
    def test_auth_fields_are_required(self):
        """
        Проверка, что поля username и password обязательны для заполнения.

        Шаг 1. Переход на /

        Ожидмаемое поведение:
         - у элемента USERNAME_INPUT есть аттрибут 'required'
         - у элемента PASSWORD_INPUT есть аттрибут 'required'
        """
        assert self.login_page.is_username_required()
        assert self.login_page.is_password_required()
