import urllib.parse

import allure
import pytest
import requests
from bs4 import BeautifulSoup


class NoResourceException(Exception):
    pass


@allure.feature('Resources')
@allure.story('Тесты статичных ресурсов')
class TestResources:
    @allure.title('Проверяем, что доступны все js скрипты с welcome page')
    @pytest.mark.UI
    def test_resources_on_welcome(self, app_full_url, myapp_api_client):
        """
        Проверяем, что все js скрипты с welcome page существуют

        Шаг 1. Авторизация через POST запрос
        Шаг 2. Парсим содержимое welcome page и выбираем оттуда все <script src="<src>">
        Шаг 3. Отправляем запросы на все <src> и проверяем код ответа

        Ожидаемое поведение: запросы на все <src> отдают не 404 код
        """
        response = myapp_api_client.auth()
        html = response.text

        soup = BeautifulSoup(html, 'lxml')
        srcs = []
        for script_tag in soup.find_all('script', {'src': True}):
            srcs.append(urllib.parse.urljoin(app_full_url, script_tag['src']))

        for link in srcs:
            response = requests.get(link)
            if response.status_code == 404:
                raise NoResourceException(f'Resource {link} not found')
