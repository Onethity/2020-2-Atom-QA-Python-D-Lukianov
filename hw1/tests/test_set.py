"""Тесты для проверки множеств"""
import pytest


class TestSet:
    @pytest.mark.smoke
    def test_get_by_index(self):
        """Проверяем возможность получения по индексу"""
        data = {1, 4, 7, 89}
        with pytest.raises(TypeError):
            assert data[3] == 7

    def test_add_already_exists(self):
        """Проверяем уникальность элементов множества"""
        data = {5, 6, 4, 3}
        data.add(5)
        assert data == {5, 6, 4, 3}

    def test_discard(self):
        """Проверяем метод .discard()"""
        data = {6, 43}
        data.discard(43)
        assert data == {6}

    def test_pop_removes_item(self, random_set):
        """Проверяем, что метод .pop() уменьшает размер множества на 1"""
        source_length = len(random_set)
        random_set.pop()
        assert len(random_set) == source_length - 1

    @pytest.mark.parametrize(
        'data1, data2, expected_difference',
        [
            ({3, 4, 5}, {3, 4}, {5}),
            ({1, 5, 7, 8}, {1, 8}, {5, 7})
        ],
    )
    def test_difference(self, data1, data2, expected_difference):
        """Проверяем разницу между множествами"""
        assert data1.difference(data2) == expected_difference
