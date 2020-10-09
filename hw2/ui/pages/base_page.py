from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


CLICK_RETRY_COUNT = 3


class BasePage:
    def __init__(self, driver):
        self.driver: webdriver = driver

    def find(self, locator, timeout=15) -> WebElement:
        """ Поиск элемента на странице """
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

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

    def send_keys(self, locator, keys, timeout=10, to_clear=True, should_be_visible=True):
        """ Отправка нажатия клавиш """
        field = self.find(locator)
        if should_be_visible:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
        if to_clear:
            field.clear()

        field.send_keys(keys)
