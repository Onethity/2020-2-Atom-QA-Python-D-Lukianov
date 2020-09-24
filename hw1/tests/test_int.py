"""Тесты для проверки типа int"""
import pytest


class TestInt:
    @pytest.mark.smoke
    def test_int_type(self, random_int):
        """Проверяем, что случайное число действительно типа int"""
        assert isinstance(random_int, int)

    def test_sum(self):
        """Проверяем работу оператора суммы"""
        assert 5 + 5 == 10

    def test_pow(self):
        """Проверяем работу опрератора возведения в степень"""
        assert 3 ** 2 == 9

    def test_bin(self):
        """Проверяем двоичное представление числа"""
        assert bin(56) == '0b111000'

    @pytest.mark.parametrize(
        'data_int, expected',
        [
            (3, 3),
            (-8, 8),
            (0, 0),
        ],
    )
    def test_abs(self, data_int, expected):
        """Тестируем функцию получения модуля числа"""
        assert abs(data_int) == expected
