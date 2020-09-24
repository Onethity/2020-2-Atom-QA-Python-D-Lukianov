"""Тесты для проверки списков"""
import pytest


class TestList:
    @pytest.mark.smoke
    def test_get_by_index(self):
        """Проверяем возможность получения элемента по индексу"""
        array = [1, 3, 5]
        assert array[1] == 3

    def test_list_merge(self):
        """Проверяем возможность слияния списоков"""
        array1 = [1, 3, 5]
        array2 = [4, 5, 6]
        assert array1 + array2 == [1, 3, 5, 4, 5, 6]

    def test_out_of_range(self):
        """Проверяем обращение к несущестующему индексу"""
        array = [1, 2, 3]
        with pytest.raises(IndexError):
            assert array[5]

    def test_pop_removes_item(self, random_list):
        """Проверяем, что .pop() уменьшает размер списка на 1"""
        source_length = len(random_list)
        random_list.pop()
        assert len(random_list) == source_length - 1

    @pytest.mark.parametrize(
        'array, expected_sum',
        [
            ([1, 2, 3, 4], 10),
            ([3, 4], 7),
            ([1], 1),
        ]
    )
    def test_sum_of_list(self, array, expected_sum):
        """Проверяем сумму элементов списка"""
        assert sum(array) == expected_sum
