"""Тесты для проверки строк"""
import pytest


class TestString:
    @pytest.mark.smoke
    def test_string_type(self, random_string):
        """Проверяем, что случайная строка имеет тип str"""
        assert isinstance(random_string, str)

    @pytest.mark.smoke
    def test_get_by_index(self):
        """Проверяем возможность получения элемента по индексу"""
        data = 'foo'
        assert data[2] == 'o'

    @pytest.mark.smoke
    def test_get_by_wrong_index(self):
        """Проверка получения элемента по несуществующему индексу"""
        data = 'bar'
        with pytest.raises(IndexError):
            assert data[5]

    def test_multiple(self):
        """Проверяем умножение строки на число"""
        data = 'foo'
        assert data * 3 == 'foofoofoo'

    @pytest.mark.parametrize(
        'str_lower, expected',
        [
            ('abc', 'ABC'),
            ('Foo Bar', 'FOO BAR'),
            ('', ''),
        ],
    )
    def test_string_upper(self, str_lower, expected):
        """Проверяем метод .upper() для строки"""
        assert str_lower.upper() == expected
