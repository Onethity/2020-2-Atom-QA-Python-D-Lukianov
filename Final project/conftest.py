from datetime import datetime, timedelta
import os
import random
import string
from datetime import datetime

import allure
from _pytest.config.argparsing import Parser
from allure_commons.types import AttachmentType
import docker

from db.fixtures import *
from ui.fixtures import *
from api.fixtures import *
from db.models.user import UserModel
from mock.client.mock_client import MockApiClient
from tests.config import CONFIG, APP_FULL_URL, MOCK_FULL_URL


def pytest_addoption(parser: Parser):
    parser.addoption('--selenoid', default=None)


@pytest.fixture()
def config():
    return CONFIG


@pytest.fixture()
def app_full_url():
    return APP_FULL_URL


@pytest.fixture()
def mock_full_url():
    return MOCK_FULL_URL


@pytest.fixture(scope='function')
def random_username():
    """ Генерация случайного username """
    letters = string.ascii_letters
    result = 'test_' + ''.join(random.choice(letters) for i in range(random.randint(4, 7)))
    return result


@pytest.fixture(scope='function')
def random_password():
    """ Генерация случайного пароля """
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(random.randint(8, 10)))
    return result


@pytest.fixture(scope='function')
def random_email():
    """ Генерация случайного email """
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(random.randint(8, 10))) + '@mail.ru'
    return result


@pytest.fixture(scope='function')
def new_user(db_connection, random_username, random_password, random_email):
    """ Фикстура для создания нового пользователя через БД """
    user = UserModel(
        username=random_username,
        password=random_password,
        email=random_email,
        active=True,
        access=True,
        start_active_time=datetime.now()
    )
    db_connection.builder.create_user(user)

    return user


@pytest.fixture(scope='function')
def new_root_user(db_connection):
    """ Фикстура для создания root пользователя (для отправки api запросов) через БД """
    letters = string.ascii_letters
    root_user = UserModel(
        username='root_' + ''.join(random.choice(letters) for i in range(random.randint(4, 7))),
        password=''.join(random.choice(letters) for i in range(random.randint(8, 10))),
        email=''.join(random.choice(letters) for i in range(random.randint(8, 10))) + '@mail.ru',
        active=True,
        access=True,
        start_active_time=datetime.now()
    )
    db_connection.builder.create_user(root_user)

    return root_user


@pytest.fixture(scope='function')
def mock_client(mock_full_url):
    """ Фикстура для доступа к клиенту мока """
    return MockApiClient(mock_full_url)


@pytest.fixture(scope='function', autouse=True)
def attach_logs():
    # Берем время для логов с запасом по 1 секунде до и после старта теста
    start_time = datetime.now() - timedelta(seconds=1)
    yield
    stop_time = datetime.now() + timedelta(seconds=1)

    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    container = client.containers.get('finalproject_myapp_1')
    logs = container.logs(
        since=start_time,
        until=stop_time,
    ).decode("utf-8")

    allure.attach(name='App logs',
                  body=logs,
                  attachment_type=AttachmentType.TEXT)
