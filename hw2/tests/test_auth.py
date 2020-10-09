import time

from tests.base_test_case import BaseTestCase
import pytest


class TestAuth(BaseTestCase):
    @pytest.mark.UI
    def test_auth_negative(self):
        self.main_page.auth('wrong_login', 'wrong_pass')
        assert 'Введите email или телефон' in self.driver.page_source

    @pytest.mark.UI
    def test_auth_positive(self, secrets):
        self.main_page.auth(secrets['login'], secrets['password'])
        assert secrets['login'] in self.driver.page_source
