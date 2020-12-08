import allure
import pytest

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Валидация формы регистрации')
class TestRegFieldsRequired(BaseUITestCase):
    @allure.title('Поля формы регистрации обязательны для заполнения')
    @pytest.mark.UI
    def test_auth_fields_are_required(self):
        """
        Проверка, что поля формы регистрации обязательны для заполнения.

        Шаг 1. Переход на /
        Шаг 2. Нажимаем "Create an account"


        Ожидмаемое поведение:
         - у элемента USERNAME_INPUT есть аттрибут 'required'
         - у элемента EMAIL_INPUT есть аттрибут 'required'
         - у элемента PASSWORD_INPUT есть аттрибут 'required'
         - у элемента PASSWORD_REPEAT_INPUT есть аттрибут 'required'
         - у элемента ACCEPT_CHECKBOX есть аттрибут 'required'
        """
        self.login_page.go_to_registration_page()

        assert self.registration_page.is_username_required(), 'Username не обязателен для заполнения'
        assert self.registration_page.is_email_required(), 'Email не обязателен для заполнения'
        assert self.registration_page.is_password_required(), 'Password не обязателен для заполнения'
        assert self.registration_page.is_password_repear_required(), 'Password repeat не обязателен для заполнения'
        assert self.registration_page.is_sdet_checkbox_required(), 'SDET checkbox не обязателен для заполнения'
