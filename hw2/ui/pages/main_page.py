from ui.locators.locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.locators import locators


class MainPage(BasePage):
    locators = MainPageLocators()

    def auth(self, login, password):
        self.click(self.locators.OPEN_LOGIN_FORM_BUTTON)
        self.send_keys(self.locators.EMAIL_FIELD, login)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON)
