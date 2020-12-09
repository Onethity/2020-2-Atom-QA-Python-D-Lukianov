from ui.locators.locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def auth(self, login, password):
        """ Авторизация с главной страницы """
        self.click(self.locators.OPEN_LOGIN_FORM_BUTTON)
        self.send_keys(self.locators.EMAIL_FIELD, login)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON)


