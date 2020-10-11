import pytest

from tests.base_test_case import BaseTestCase


class TestAuth(BaseTestCase):
    """ Тесты на авторизацию """
    @pytest.mark.UI
    def test_auth_negative(self):
        """ Негативный тест на авторизацию с неверным форматом логина """
        self.main_page.auth('wrong_login', 'wrong_pass')
        assert 'Введите email или телефон' in self.driver.page_source

    @pytest.mark.UI
    def test_auth_positive(self, secrets):
        """ Позитивный тест на авторизацию """
        self.main_page.auth(secrets['login'], secrets['password'])
        assert self.dashboard_page.get_user_login() == secrets['login']
