""" Тесты по условию домашнего задания """
from tests.base_test_case import BaseTestCase


class TestUsersAppFromTask(BaseTestCase):
    def test_mock_is_down(self):
        """ Приложение поднято, а мок не поднят """
        response = self.client.get('/users')
        assert response.status_code == 200

        response = self.client.get('/mock_is_down')
        assert response.status_code == 421
        assert response.json()['message'] == 'mock is down'

    def test_mock_timeout(self):
        """ Приложение поднято, а мок не отвечает (timeout) """
        response = self.client.get('/timeout')

        assert response.status_code == 408
        assert response.json()['message'] == 'users service timeout'

    def test_mock_500(self):
        """ Приложение сходило в мок, а мок отдал 500 """
        response = self.client.get('/mock_500')

        assert response.status_code == 424
        assert response.json()['message'] == 'mock service internal error'

    def test_auth_positive(self, random_username):
        """ Позитивный тест на авторизацию"""
        self.client.put('/user/create', data={'username': random_username})  # Создали пользователя

        # И авторизуемся с ним
        response = self.client.post(
            f'/check_auth/{random_username}',
            data={'username': random_username},
            headers={'Authorization': random_username}
        )

        assert response.status_code == 200
        assert response.json()['status'] == 'ok'

    def test_auth_negative(self, random_username):
        """ Негативный тест на авторизацию """
        response = self.client.post(  # Запрос на авторизацию с несуществующим пользователем
            f'/check_auth/{random_username}',
            data={'username': random_username},
            headers={'Authorization': random_username}
        )

        assert response.status_code == 403
        assert response.json()['message'] == 'User does not exist'

    def test_auth_no_header(self, random_username):
        """ Тест на авторизацию без заголовка Authorization"""
        response = self.client.post(  # Запрос на авторизацию без нужного заголовка
            f'/check_auth/{random_username}',
            data={'username': random_username},
        )

        assert response.status_code == 412
        assert response.json()['message'] == 'No auth header'

    def test_auth_different_username(self, random_username):
        """ Тест на авторизацию, когда имя пользователя в URL и заголовке не совпадают """
        response = self.client.post(
            f'/check_auth/{random_username}',
            data={'username': random_username},
            headers={'Authorization': 'Wrong_user_name'}
        )

        assert response.status_code == 400
        assert response.json()['message'] == 'Username in url and in header must be the same'


