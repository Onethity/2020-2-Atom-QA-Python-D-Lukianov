import pytest

from api.exceptions.exceptions import SegmentDoesNotExist
from tests.base_test_case import BaseTestCase


class TestSegment(BaseTestCase):
    @pytest.mark.API
    def test_create_segment(self, random_string):
        """ Тест на создание сегмента """
        segment_id = self.client.create_segment(segment_title=random_string)
        self.client.check_if_segment_exists(segment_id)

    @pytest.mark.API
    def test_delete_segment(self, random_string):
        """ Тест на удаление сегмента """
        segment_id = self.client.create_segment(segment_title=random_string)
        self.client.check_if_segment_exists(segment_id)

        self.client.delete_segment(segment_id)
        with pytest.raises(SegmentDoesNotExist):
            self.client.check_if_segment_exists(segment_id)
