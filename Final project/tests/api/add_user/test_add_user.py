import random

import allure
import pytest

from tests.api.base_api_test_case import BaseApiTestCase


@allure.feature('API')
@allure.story('Добавление пользователя')
class TestAddUser(BaseApiTestCase):
    @allure.title('Добавление валидного пользователя через API')
    @pytest.mark.API
    def test_add_user(self, random_username, random_email, random_password):
        """
         Добавление валидного пользователя через API.

         Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
        {
           "username": "<username>",
           "password": "<password>",
           "email": "<email>"
        }

        Ожидаемое поведение:
            1. Статус код 201
            2. Сообщение "User was added!"
            3. Пользователь добавлен в БД
        """

        response = self.myapp_client.add_user(random_username, random_email, random_password)

        assert self.mysql_client.builder.does_user_exist(random_username), 'Пользователь не добавлен в бд'
        assert response.status_code == 201, 'Неверный код ответа'
        assert response.text == 'User was added!', 'Неверное тело ответа'

    @allure.title('Добавление пользователя через API несколько раз')
    @pytest.mark.API
    def test_add_user_twice(self, random_username, random_email, random_password):
        """
         Добавление одного и того же валидного пользователя через API несколько раз

         Шаг 1. JSON POST запрос на http://<app_url>/api/add_user

         Body:
        {
           "username": "<username>",
           "password": "<password>",
           "email": "<email>"
        }


        Шаг 2. Такой же запрос еще несколько раз


        Ожидаемое поведение: первый запрос возвращает 201, а остальные 304
        """

        for i in range(random.randint(3, 5)):
            response = self.myapp_client.add_user(
                random_username,
                random_email,
                random_password,
            )

            if i == 0:
                assert response.status_code == 201, 'Неверный код ответа первого запроса'
            else:
                assert response.status_code == 304, 'Неверный код ответа дальнейших запросов'
