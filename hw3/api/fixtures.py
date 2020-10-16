import string
import random

import pytest

from api.secret import ACCOUNT_CREDENTIALS


@pytest.fixture(scope='function')
def secrets():
    """ Фикстура, содержащая секретные данные """
    return ACCOUNT_CREDENTIALS


@pytest.fixture(scope='function')
def random_string():
    """ Генерация случайной строки """
    letters = string.ascii_letters
    result = 'test_' + ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    return result
