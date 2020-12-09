import random
import string

import pytest
import requests

from application.custom_app import start_app
from client.socket_client import HTTPClient
from config import CONFIG
from mock.users_mock_server import start_mock


@pytest.fixture(scope='session')
def config():
    return CONFIG


@pytest.fixture(scope='session', autouse=True)
def mock(config):
    start_app(host=config['app']['host'],  # Запускаем приложение
              port=config['app']['port'])

    mock_server = start_mock(host=config['mock']['host'],  # Запускаем mock
                             port=config['mock']['port'])

    yield

    mock_server.stop()
    requests.get('http://localhost:4210/stop')


@pytest.fixture(scope='function')
def http_client(config):
    return HTTPClient(
        host=config['app']['host'],
        port=config['app']['port'],
        print_json=True  # Вывод ответа на экран в формате JSON
    )


@pytest.fixture(scope='function')
def random_username():
    """ Генерация случайного имени пользователя """
    letters = string.ascii_letters
    result = 'test_' + ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    return result
