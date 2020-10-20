import json
import requests

from api.endpoints.mytarget_api_endpoints import MytargetApiEndpoints
from api.exceptions.exceptions import ResponseStatusCodeException, SegmentDoesNotExist, ApiErrorException


class MytargetApiClient:
    def __init__(self, base_url, login, password):
        self.endpoints = MytargetApiEndpoints(base_url)

        self.session = requests.Session()
        self.auth(login, password)
        self.csrf_token = self._get_csrf_token()

    def auth(self, login, password):
        """ Отправка запроса на авторизацию """
        headers = {
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': login,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login',
            'failure': 'https://account.my.com/login/',
        }

        response = self._request(
            'POST',
            url=self.endpoints.AUTH,
            headers=headers,
            data=data,
            json=False,
        )

        return response

    def create_segment(self, segment_title):
        """
        Отправка запроса на создание сегмента

        :return: ID нового сегмента
        """

        headers = {
            'X-CSRFToken': self.csrf_token
        }

        data = json.dumps({
            'name': segment_title,
            'pass_condition': 1,
            'relations': [
                {
                    'object_type': 'remarketing_player',
                    'params': {
                        'type': 'positive',
                        'left': 365,
                        'right': 0
                    }
                }
            ],
            'logicType': 'or'
        })

        response = self._request(
            'POST',
            url=self.endpoints.get_create_segment_endpoint(),
            headers=headers,
            data=data,
        )

        return response['id']

    def check_if_segment_exists(self, segment_id):
        """ Проверка сегмента на существование """
        try:
            self._request('GET', self.endpoints.get_segment_data_endpoint(segment_id), status_code=200)
        except ResponseStatusCodeException as e:
            # Если код ответа 404, то значит, что сегмент не существует
            if e.status_code == 404:
                raise SegmentDoesNotExist
            else:
                raise e

    def delete_segment(self, segment_id):
        """ Отправка запроса на удаление сегмента """
        headers = {
            'X-CSRFToken': self.csrf_token
        }

        response = self._request(
            'DELETE',
            url=self.endpoints.get_segment_data_endpoint(segment_id),
            headers=headers,
            status_code=204,
            json=False,
        )

        return response

    def _get_csrf_token(self):
        """ Получение CSRF токена """
        response = self._request('GET', self.endpoints.get_csrf_endpoint(), json=False)
        return response.cookies['csrftoken']

    def _request(self, method, url, status_code=200, data=None, headers=None, json=True):
        """ Отправка HTTP запроса """
        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(
                status_code=response.status_code,
                message='Got {response.status_code} {response.reason} for URL {url}, but expected {status_code}'
            )

        if json:
            json_response = response.json()

            if json_response.get('error'):
                error_code = json_response['error']['code']
                error_message = json_response['error']['message']
                raise ApiErrorException(f'Got API error: {error_code} "{error_message}"')

            return json_response

        return response
