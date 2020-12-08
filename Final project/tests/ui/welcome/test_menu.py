import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Тесты меню на welcome page')
class TestMenu(BaseUITestCase):
    @allure.title('Нажатие на логотип ведет на главную страницу')
    @pytest.mark.UI
    def test_click_logo(self, welcome_page):
        """
        Проверяем, что при нажатии на логотип открывается главная страниа приложения

        Шаг 1. Авторизация в приложении
        Шаг 2. Клик на логотип

        Ожидаемое поведение: заголовок страниы - "Test Server | Welcome!"
        """
        self.welcome_page.click_to_logo()

        allure.attach(name='welcome_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert self.driver.title == "Test Server | Welcome!", 'Открылась неверная страница'

    @allure.title('Нажатие на кнопку меню HOME ведет на главную страницу')
    @pytest.mark.UI
    def test_click_home(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню HOME открывается главная страниа приложения

        Шаг 1. Авторизация в приложении
        Шаг 2. Клик на кнопку HOME в меню

        Ожидаемое поведение: заголовок страниы - "Test Server | Welcome!"
        """
        self.welcome_page.click_to_home()

        allure.attach(name='welcome_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert self.driver.title == "Test Server | Welcome!", 'Открылась неверная страница'

    @allure.title('Нажатие на кнопку меню Python открывает сайт python.org в новой вкладке')
    @pytest.mark.UI
    def test_click_python(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Python открывается python.org в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Клик на кнопку Python в меню

        Ожидаемое поведение: открывается сайт python.org в новой вкладке
        """
        self.welcome_page.click_to_python()
        self._switch_to_second_tab()
        allure.attach(name='python_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'python.org' in self.driver.current_url, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню Linux открывает сайт о linux в новой вкладке')
    @pytest.mark.UI
    def test_click_linux(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Linux открывается сайт о linux в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Клик на кнопку Linux в меню

        Ожидаемое поведение: открывается сайт о linux в новой вкладке
        """
        self.welcome_page.click_to_linux()
        self._switch_to_second_tab()
        allure.attach(name='linux_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'Linux' in self.driver.title, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню Network открывает сайт о сетях в новой вкладке')
    @pytest.mark.UI
    def test_click_network(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Linux открывается сайт о сетях в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Клик на кнопку Network в меню

        Ожидаемое поведение: открывается сайт о сетях в новой вкладке
        """
        self.welcome_page.click_to_network()
        self._switch_to_second_tab()
        allure.attach(name='linux_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'network' in self.driver.title, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню Python history открывает статью'
                  ' в википедии History of Python в новой вкладке')
    @pytest.mark.UI
    def test_click_python_history(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Python history открываеся
        статья в википедии History of Python в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Python
        Шаг 2. Клик на кнопку Python history

        Ожидаемое поведение: открываеся статья в википедии History of Python в новой вкладке
        """
        self.welcome_page.click_to_python_history()
        self._switch_to_second_tab()
        allure.attach(name='history_of_python_page', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert self.driver.current_url == 'https://en.wikipedia.org/wiki/History_of_Python', 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню About flask открывает документацию flask в новой вкладке')
    @pytest.mark.UI
    def test_click_about_flask(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню About flask открывается документация flask в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Python
        Шаг 2. Клик на кнопку About flask

        Ожидаемое поведение: открываеся документация по Flask (flask.palletsprojects.com) в новой вкладке
        """
        self.welcome_page.click_to_about_flask()
        self._switch_to_second_tab()
        allure.attach(name='about_flask', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'flask.palletsprojects.com' in self.driver.current_url, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку подменю Download Centos7 открывает страницу загрузки Centos')
    @pytest.mark.UI
    def test_click_download_centos(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Download Centos7 открывается страницу загрузки Centos в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Linux
        Шаг 2. Клик на кнопку Download Centos7

        Ожидаемое поведение: открываеся страница загрузки Centos в новой вкладке
        """
        self.welcome_page.click_to_download_centos()
        self._switch_to_second_tab()

        allure.attach(name='download_centos', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'centos.org' in self.driver.current_url, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню News (wireshark) открывает wireshark.org/news/ в новой вкладке')
    @pytest.mark.UI
    def test_click_wireshark_news(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню News (wireshark) открывается wireshark.org/news/ в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Network
        Шаг 2. Клик на кнопку News

        Ожидаемое поведение: открываеся страница новостей wireshark.org/news/ в новой вкладке
        """
        self.welcome_page.click_to_wireshark_news()
        self._switch_to_second_tab()
        allure.attach(name='wireshark_news', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'wireshark.org/news/' in self.driver.current_url, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню Download (wireshark) открывает wireshark.org/#download в новой вкладке')
    @pytest.mark.UI
    def test_click_wireshark_download(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Download (wireshark) открывается wireshark.org/#download в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Network
        Шаг 2. Клик на кнопку Download

        Ожидаемое поведение: открываеся страница загрузки wireshark в новой вкладке
        """
        self.welcome_page.click_to_wireshark_download()
        self._switch_to_second_tab()
        allure.attach(name='wireshark_download', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'wireshark.org/#download' in self.driver.current_url, 'Открылся неверный сайт'

    @allure.title('Нажатие на кнопку меню Examples (tcpdump) открывает '
                  'hackertarget.com/tcpdump-examples/ в новой вкладке')
    @pytest.mark.UI
    def test_click_tcpdump_examples(self, welcome_page):
        """
        Проверяем, что при нажатии на кнопку меню Examples (Tcpdump)
        открывается hackertarget.com/tcpdump-examples/ в новой вкладке

        Шаг 1. Авторизация в приложении
        Шаг 2. Наводим курсор на меню Network
        Шаг 2. Клик на кнопку Examples

        Ожидаемое поведение: открываеся страница hackertarget.com/tcpdump-examples/ в новой вкладке
        """
        self.welcome_page.click_to_tcpdump_examples()
        self._switch_to_second_tab()
        allure.attach(name='tcpdump_example', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert 'hackertarget.com/tcpdump-examples' in self.driver.current_url, 'Открылся неверный сайт'
