import allure

from ui.locators.locators import Error404PageLocators
from ui.pages.base.base_page import BasePage


class Error404Page(BasePage):
    locators = Error404PageLocators()

    @allure.step('Получаем текст 404 ошибки')
    def get_error_text(self):
        return self.find(self.locators.ERROR_TEXT).text

    @allure.step('Получаем путь к изображению 404 ошибки')
    def get_error_img_src(self):
        return self.find(self.locators.ERROR_IMG).get_attribute('src')
