import allure

from ui.locators.locators import LoginPageLocators
from ui.pages.base.base_page import BasePage
from ui.pages.error_404_page import Error404Page
from ui.pages.registration_page import RegistrationPage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Вводим в форму авторизации {username}, {password} и нажимаем кнопку LOGIN')
    def auth(self, username, password):
        """ Метод для авторизации """
        self.send_keys(self.locators.USERNAME_INPUT, username)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)

    @allure.step('Получаем текст flash сообщения')
    def get_flash_message_text(self):
        """ Текст flash сообщения """
        return self.find(self.locators.FLASH_MESSAGE, should_be_visible=True).text

    @allure.step('Переход на страницу регистрации')
    def go_to_registration_page(self):
        self.click(self.locators.GO_TO_REGISTRATION)
        return RegistrationPage(self.driver)

    @allure.step('Переход на несуществующую страницу')
    def go_to_404(self):
        self.driver.get(self.driver.current_url + 'wrong_page')
        return Error404Page(self.driver)

    @allure.step('Проверяем, обязательно ли поле username для заполнения')
    def is_username_required(self):
        return self.is_required(self.locators.USERNAME_INPUT)

    @allure.step('Проверяем, обязательно ли поле password для заполнения')
    def is_password_required(self):
        return self.is_required(self.locators.PASSWORD_INPUT)
