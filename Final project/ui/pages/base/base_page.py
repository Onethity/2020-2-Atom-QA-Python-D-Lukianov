import time

import allure
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CLICK_RETRY_COUNT = 3


class BasePage:
    def __init__(self, driver):
        self.driver: webdriver = driver

    @allure.step('Ищем элемент {locator}')
    def find(self, locator, timeout=15, should_be_visible=False) -> WebElement:
        """ Поиск элемента на странице """
        waiter = self.wait(timeout)
        if should_be_visible:
            return waiter.until(EC.visibility_of_element_located(locator))
        else:
            return waiter.until(EC.presence_of_element_located(locator))

    @allure.step('Клик на {locator}')
    def click(self, locator, timeout=15):
        """ Клик по элементу """
        for i in range(CLICK_RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < CLICK_RETRY_COUNT - 1:
                    pass
        raise

    def wait(self, timeout=15):
        """ Явное ожидание """
        return WebDriverWait(self.driver, timeout)

    @allure.step('Отправляем {keys} в элемент {locator}')
    def send_keys(self, locator, keys, timeout=10, to_clear=True, should_be_visible=True):
        """ Отправка нажатия клавиш """
        field = self.find(locator)
        if should_be_visible:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
        if to_clear:
            field.clear()

        field.send_keys(keys)

    @allure.step('Получаем аттрибут {attribute} у элемента {locator}')
    def get_attribute(self, locator, attribute):
        """ Получение аттрибута элемента """
        return self.find(locator).get_attribute(attribute)

    @allure.step('Проверяем, есть ли у элемента {locator} аттрибут required')
    def is_required(self, locator):
        return self.get_attribute(locator, 'required')

    def get_screenshot(self):
        """ Создание скриншота """
        time.sleep(2.4)  # Задержка анимации
        return self.driver.get_screenshot_as_png()

