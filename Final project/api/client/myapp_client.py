import warnings

import allure
import requests
from allure_commons.types import AttachmentType

from api.endpoints.myapp_api_endpoints import MyappApiEndpoints
from api.exceptions.exceptions import ApiErrorException


class MyappApiClient:
    def __init__(self, base_url, auth=True, username=None, password=None):
        self.status_codes = [  # Возможные статус коды, предусмотренные документацией
            200, 201, 204, 304, 400, 401, 404
        ]
        self.endpoints = MyappApiEndpoints(base_url)

        self.username = username
        self.password = password

        self.session = requests.Session()

        if auth:
            self.auth()

    @allure.step('POST запрос на авторизацию в API')
    def auth(self):
        data = {'submit': 'Login'}
        if self.username:
            data.update({'username': self.username})
        if self.password:
            data.update({'password': self.password})

        return self._request(
            'POST',
            self.endpoints.auth(),
            json=False,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data=data,
            json_response=False
        )

    @allure.step('POST API запрос на добавление пользователя {username}, {email}, {password}')
    def add_user(self, username, email, password):
        return self._request(
            'POST',
            self.endpoints.get_add_user_url(),
            data={
                'username': username,
                'password': password,
                'email': email
            },
            json=True,
            json_response=False
        )

    @allure.step('GET API запрос на удаление пользователя {username}')
    def del_user(self, username):
        return self._request(
            'GET',
            self.endpoints.get_delete_user_url(username),
            json=False,
            json_response=False,
        )

    @allure.step('GET API запрос на блокировку пользователя {username}')
    def block_user(self, username):
        return self._request(
            'GET',
            self.endpoints.get_block_user_url(username),
            json=False,
            json_response=False,
        )

    @allure.step('GET API запрос на разблокировку пользователя {username}')
    def accept_user(self, username):
        return self._request(
            'GET',
            self.endpoints.get_accept_user_url(username),
            json=False,
            json_response=False,
        )

    @allure.step('GET API запрос на статус приложения')
    def get_status(self):
        """ Проверка статуса приложения """
        response = self._request('GET', self.endpoints.get_status_url())
        return response['status']

    @allure.step('Запрос на /logout')
    def logout(self):
        self._request('GET', self.endpoints.logout(), json=False, json_response=False)

    @allure.step('HTTP запрос: {method} {url}')
    def _request(self, method, url, data=None, headers=None, json=True, json_response=True):
        """ Отправка HTTP запроса """
        if json:
            response = self.session.request(method, url, headers=headers, json=data)
        else:
            response = self.session.request(method, url, headers=headers, data=data)

        self._attach_request_and_response(response)

        if response.status_code not in self.status_codes:
            warnings.warn('Unexpected status code')

        if json_response:
            json_response = response.json()

            if json_response.get('error'):
                error_message = json_response['error']
                raise ApiErrorException(f'Got API error: {response.status_code} "{error_message}"')

            return json_response

        return response

    def _attach_request_and_response(self, response):
        """ Добавление HTTP запроса и ответа в отчет allure """
        # Attach request
        allure.attach(
            name='Request',
            body=f'{response.request.method} to {response.request.url}'
                 f'\n\n'
                 f'Headers:\n'
                 f'{response.request.headers}'
                 f'\n\n'
                 f'Body:\n'
                 f'{response.request.body}',
            attachment_type=AttachmentType.TEXT
        )

        # Attach response
        allure.attach(
            name='Response',
            body=f'Headers:\n'
                 f'{response.headers}'
                 f'\n\n'
                 f'Body:\n'
                 f'{response.text}',
            attachment_type=AttachmentType.TEXT
        )
