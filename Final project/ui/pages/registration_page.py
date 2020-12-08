import allure

from ui.locators.locators import RegistrationPageLocators
from ui.pages.base.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    @allure.step('Заполняем форму регистрации:'
                 'username={username}, '
                 'email={email}, '
                 'password={password}, '
                 'password_repeat={password_repeat}'
                 )
    def registration(self, username, password, email, password_repeat=None):
        if not password_repeat:
            password_repeat = password

        self.send_keys(self.locators.USERNAME_INPUT, username)
        self.send_keys(self.locators.EMAIL_INPUT, email)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.send_keys(self.locators.PASSWORD_REPEAT_INPUT, password_repeat)
        self.click(self.locators.ACCEPT_CHECKBOX)
        self.click(self.locators.SUBMIT_BUTTON)

    @allure.step('Получаем текст flash сообщения')
    def get_flash_message_text(self):
        """ Текст flash сообщения """
        return self.find(self.locators.FLASH_MESSAGE, should_be_visible=True).text

    def is_username_required(self):
        return self.is_required(self.locators.USERNAME_INPUT)

    def is_password_required(self):
        return self.is_required(self.locators.PASSWORD_INPUT)

    def is_password_repear_required(self):
        return self.is_required(self.locators.PASSWORD_REPEAT_INPUT)

    def is_sdet_checkbox_required(self):
        return self.is_required(self.locators.ACCEPT_CHECKBOX)

    def is_email_required(self):
        return self.is_required(self.locators.EMAIL_INPUT)


