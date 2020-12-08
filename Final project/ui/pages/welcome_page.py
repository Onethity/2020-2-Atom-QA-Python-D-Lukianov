import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from ui.locators.locators import WelcomePageLocators
from ui.pages.base.base_page import BasePage
from ui.pages.login_page import LoginPage


class NoVkIdException(Exception):
    pass


class WelcomePage(BasePage):
    locators = WelcomePageLocators()

    @allure.step('Проверка логина пользователя')
    def get_logged_as(self):
        """ Возвращает строку Logged as <username> """
        elem = self.find(self.locators.LOGGED_AS)
        return elem.text

    @allure.step('Проверка vk id пользователя')
    def get_vk_id(self):
        """ Возвращает строку VK ID: <vk_id> """
        try:
            elem = self.find(self.locators.VK_ID)
            return elem.text
        except TimeoutException:
            raise NoVkIdException

    @allure.step('Клик на кнопку API')
    def go_to_api(self):
        self.click(self.locators.WHATS_AN_API_ICON)

    @allure.step('Клик на кнопку Future of internet')
    def go_to_future_of_internet(self):
        self.click(self.locators.FUTURE_OF_INTERNET_ICON)

    @allure.step('Клик на кнопку Lets talk about SMTP?')
    def go_to_smtp(self):
        self.click(self.locators.SMTP_ICON)

    @allure.step('Клик на логотип')
    def click_to_logo(self):
        self.click(self.locators.LOGO_BUTTON)

    @allure.step('Клик на кнопку меню HOME')
    def click_to_home(self):
        self.click(self.locators.MENU_HOME_BUTTON)

    @allure.step('Клик на кнопку меню Python')
    def click_to_python(self):
        self.click(self.locators.MENU_PYTHON_BUTTON)

    @allure.step('Клик на кнопку меню Linux')
    def click_to_linux(self):
        self.click(self.locators.MENU_LINUX_BUTTON)

    @allure.step('Клик на кнопку меню Network')
    def click_to_network(self):
        self.click(self.locators.MENU_NETWORK)

    @allure.step('Наводим курсор на Python и нажимаем Python history')
    def click_to_python_history(self):
        self._click_on_submenu(self.locators.MENU_PYTHON_BUTTON, self.locators.MENU_PYTHON_HISTORY)

    @allure.step('Наводим курсор на Python и нажимаем About flask')
    def click_to_about_flask(self):
        self._click_on_submenu(self.locators.MENU_PYTHON_BUTTON, self.locators.MENU_ABOUT_FLASK)

    @allure.step('Наводим курсор на Linux и нажимаем Download Centos 7')
    def click_to_download_centos(self):
        self._click_on_submenu(self.locators.MENU_LINUX_BUTTON, self.locators.CENTOS_DOWNLOAD)

    @allure.step('Наводим курсор на Network и нажимаем Wireshark News')
    def click_to_wireshark_news(self):
        self._click_on_submenu(self.locators.MENU_NETWORK, self.locators.WIRESHARK_NEWS)

    @allure.step('Наводим курсор на Network и нажимаем Wireshark Download')
    def click_to_wireshark_download(self):
        self._click_on_submenu(self.locators.MENU_NETWORK, self.locators.WIRESHARK_DOWNLOAD)

    @allure.step('Наводим курсор на Network и нажимаем Tcpdump examples')
    def click_to_tcpdump_examples(self):
        self._click_on_submenu(self.locators.MENU_NETWORK, self.locators.TCP_DUMP_EXAMPLES)

    @allure.step('Нажимаем кнопку Logout')
    def click_to_logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
        return LoginPage(self.driver)

    @allure.step('Получаем цитату о python из футера')
    def get_zen_of_python(self):
        elem = self.find(self.locators.ZEN_OF_PYTHON)
        return elem.text

    def _click_on_submenu(self, menu_button_locator, submenu_button_locator):
        """ Клик в выпадающем меню """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find(menu_button_locator))
        actions.click(self.find(submenu_button_locator))
        actions.perform()
