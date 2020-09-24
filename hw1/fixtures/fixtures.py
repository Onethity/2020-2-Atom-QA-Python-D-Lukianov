"""Фикстуры для тестов стандартных типов данных"""
import random
import string
import pytest


@pytest.fixture
def random_list():
    """Генерация случайного списка"""
    return [random.randint(-100, 100) for x in range(random.randint(2, 10))]


@pytest.fixture
def random_set():
    """Генерация случайного множества"""
    return {random.randint(-100, 100) for x in range(random.randint(2, 10))}


@pytest.fixture
def random_dict():
    """Генерация случайного словаря"""
    values = ['value1', 'value2']
    return {'key' + str(x): random.choice(values) for x in range(random.randint(2, 10))}


@pytest.fixture
def random_string():
    """Генерация случайной строки"""
    letters = string.ascii_lowercase  # Все символы ASCII
    result = ''.join(random.choice(letters) for i in range(random.randint(2, 10)))
    return result


@pytest.fixture
def random_int():
    """Генерация случайного числа типа int"""
    return random.randint(-100, 100)
