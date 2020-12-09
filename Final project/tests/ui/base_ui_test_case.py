import pytest
from selenium import webdriver

from ui.pages.login_page import LoginPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.welcome_page import WelcomePage


class NewTabException(Exception):
    pass


class BaseUITestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, db_connection):
        self.driver: webdriver = driver

        self.login_page: LoginPage = LoginPage(driver)
        self.registration_page: RegistrationPage = RegistrationPage(driver)
        self.welcome_page: WelcomePage = WelcomePage(driver)

        self.mysql_client = db_connection

    def _switch_to_second_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except IndexError:
            raise NewTabException('Новая вкладка не найдена')
