import time

import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Проверка start_active_time')
class TestStartActiveTime(BaseApiTestCase):

    @allure.title('Время авторизации записывается в start_active_time БД')
    @pytest.mark.API
    def test_active_time_increase(self):
        """
        Проверяем, что время авторизации пользователя действительно записывается в базу

        Шаг 1. Авторизуемся
        Шаг 2. Логаут
        Шаг 3. Ждем 5 секунд
        Шаг 3. Еще раз авторизуемся

        Ожидаемое поведение: разница delta между временами первой и второй
         авторизации лежит в диапазоне 3 <= delta <= 7 (смотрим с запасом на возможные задержки)
        """
        old_active_time = self.mysql_client.builder.get_active_time(self.myapp_client.username)
        self.myapp_client.logout()
        time.sleep(5)
        self.myapp_client.auth()
        new_active_time = self.mysql_client.builder.get_active_time(self.myapp_client.username)

        delta_time = new_active_time - old_active_time
        assert 3 <= delta_time.seconds <= 7, 'Новое время авторизации неверное'
