import allure
import pytest

from tests.ui.base_ui_test_case import BaseUITestCase
from tests.ui.zen_of_python import ZEN_OF_PYTHON


@allure.feature('UI')
@allure.story('Тесты welcome page')
class TestWelcomePage(BaseUITestCase):
    @allure.title('Кнопка "What is an API?" ведет на статью об API')
    @pytest.mark.UI
    def test_what_is_an_api(self, welcome_page):
        """
        Проверка на то, что кнопка "What is an API?" ведет на статью об API

        Шаг 1. Авторизация в приложении
        Шаг 2. Нажимаем на кнопку "What is an API?"

        Ожидаемое поведение: открывается статья Википедии об API в новой вкладке
        """
        welcome_page.go_to_api()
        self._switch_to_second_tab()

        assert self.driver.current_url == 'https://en.wikipedia.org/wiki/API'

    @allure.title('Кнопка "Future of internet" ведет на статью в popular mechanics')
    @pytest.mark.UI
    def test_future_of_interntet(self, welcome_page):
        """
        Проверка на то, что кнопка "Future of internet" ведет на статью в popular mechanics

        Шаг 1. Авторизация в приложении
        Шаг 2. Нажимаем на кнопку "Future of internet"

        Ожидаемое поведение: открывается статья "What Will the Internet Be Like in the Next 50 Years?" в новой вкладке
        """
        welcome_page.go_to_future_of_internet()
        self._switch_to_second_tab()

        assert self.driver.current_url == 'https://www.popularmechanics.com' \
                                          '/technology/infrastructure/a29666802/future-of-the-internet/', \
            'Открылся неверный сайт'

    @allure.title('Кнопка "Lets talk about SMTP?" ведет на статью об SMTP')
    @pytest.mark.UI
    def test_smtp(self, welcome_page):
        """
        Проверка на то, что кнопка "Lets talk about SMTP?" ведет на статью об SMTP

        Шаг 1. Авторизация в приложении
        Шаг 2. Нажимаем на кнопку "Lets talk about SMTP?"

        Ожидаемое поведение: открывается статья Википедии об SMTP в новой вкладке
        """
        welcome_page.go_to_smtp()
        self._switch_to_second_tab()

        assert self.driver.current_url == 'https://ru.wikipedia.org/wiki/SMTP', 'Открылся неверный сайт'

    @allure.title('Внизу страницы отображается случайная цитата о Python')
    @pytest.mark.UI
    def test_python_zen(self, welcome_page):
        """
        Проверяем, что внизу страницы отображается случайная цитата о Python

        Шаг 1. Авторизация в приложении

        Ожидаемое поведение: на странице /welcome внизу отображается одна из цитат Zen of Python
        """
        quote = welcome_page.get_zen_of_python()
        assert quote in ZEN_OF_PYTHON, 'Цитата не из Zen of Python'
