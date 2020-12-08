import urllib.parse

import allure
import pytest
import requests

from api.client.myapp_client import MyappApiClient


@allure.feature('ENV')
@allure.story('Проверка, что окружение готово к запуску тестов')
class TestEnvironment:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, app_full_url, myapp_api_client):
        self.myapp_client: MyappApiClient = myapp_api_client

    @allure.title('Проверка того, что приложение запущено')
    @pytest.mark.ENV
    def test_app_is_up(self, app_full_url):
        """
        Проверка того, что приложение запущено.

        Шаг 1. GET запрос на http://<app_url>/status

        Ожидаемый результат: JSON ответ {"status": "ok"}
        """
        assert self.myapp_client.get_status() == 'ok', 'Приложение не запущено'

    @allure.title('Проверка того, что мок запущен')
    @pytest.mark.ENV
    def test_mock_is_up(self, mock_full_url):
        """
        Проверка того, что мок запущен.

        Шаг 1. GET запрос на http://<mock_url>/is_mock_up

        Ожидаемый результат: ответ OK
        """
        url = urllib.parse.urljoin(mock_full_url, '/is_mock_up')
        response = requests.get(url)

        assert response.text == 'OK', 'Мок не запущен'
