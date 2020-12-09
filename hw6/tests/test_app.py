""" Тесты, которые придумал я сам """
import random

from tests.base_test_case import BaseTestCase


class TestUsersApp(BaseTestCase):

    def test_add_user(self, random_username):
        """ Добавялем пользователя и проверяем, что он действительно добавлен """
        self.client.put('/user/create',
                        data={'username': random_username})  # Отправка запроса на создание пользователя

        users = self._get_users()

        assert random_username in users

    def test_add_several_users(self, random_username):
        """ Добавляем одинакового пользователя несколько раз и проверяем, что добавлен только один"""
        for _ in range(random.randint(2, 5)):
            response = self.client.put('/user/create', data={'username': random_username})

        assert response.status_code == 204

        users = self._get_users()
        assert users.count(random_username) == 1

    def test_delete_user(self, random_username):
        """ Удаляем пользователя и проверяем, что он удален"""
        # Сначала пользователя необходимо создать
        self.client.put('/user/create', data={'username': random_username})

        # А потом удалить
        self.client.delete(f'/user/{random_username}')

        # Проверяем, что его больше нет в списке
        users = self._get_users()

        assert random_username not in users

    def test_delete_user_negative(self, random_username):
        """ Удаляем несуществующего пользователя и проверяем ошибку """
        response = self.client.delete(f'/user/{random_username}')

        assert response.status_code == 400
        assert 'user does not exist' in response.json()['message']

    def test_wrong_endpoint_json_message(self):
        """ Проверка сообщения о 404 ошибке """
        response = self.client.get('/this-is-wrong-endpoint')
        assert response.status_code == 404
        assert response.json()['message'] == 'not found'

    def _get_users(self) -> list:
        """ Получение списка пользователей """
        response = self.client.get('/users')
        users = response.json()['users']
        return users
