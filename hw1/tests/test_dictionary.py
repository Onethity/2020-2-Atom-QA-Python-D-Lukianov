"""Тесты для проверки словарей"""
import pytest


class TestDictionary:
    @pytest.mark.smoke
    def test_get_by_index(self):
        """Проверка получения элемента по индексу"""
        data = {
            'foo': 'bar',
            'fuzz': 'buzz'
        }
        assert data['foo'] == 'bar'

    @pytest.mark.smoke
    def test_get_by_wrong_index(self):
        """Проверка получения элемента по несуществующему индексу"""
        data = {'foo': 'bar'}
        with pytest.raises(KeyError):
            assert data['wrong_key']

    def test_update_values(self):
        """Проверка возможности обновления словаря"""
        data1 = {'foo': 'bar'}
        data2 = {'fuzz': 'buzz'}
        data1.update(data2)
        assert data1 == {'foo': 'bar', 'fuzz': 'buzz'}

    def test_popitem(self, random_dict):
        """Провереряем, что .pop() уменьшает размер словаря на 1"""
        source_length = len(random_dict)
        random_dict.popitem()
        assert len(random_dict) == source_length - 1

    @pytest.mark.parametrize(
        'source_data, pop_key, expected_data',
        [
            ({'foo': 'bar', 'fuzz': 'buzz'}, 'foo', {'fuzz': 'buzz'}),
            ({'bar': 'foo'}, 'bar', {}),
        ],
    )
    def test_pop(self, source_data, pop_key, expected_data):
        """Проверяем, что метод .popitem() убирает элемент из словаря"""
        source_data.pop(pop_key)
        assert source_data == expected_data
