import pytest

from tests.base_test_case import BaseTestCase


class TestSegment(BaseTestCase):
    @pytest.mark.UI
    def test_create_segment(self, dashboard, random_string):
        segment_title = random_string
        self._create_segment_helper(dashboard, segment_title)
        self.segments_list_page.check_if_segment_exists(segment_title)

    @pytest.mark.UI
    def test_delete_segment(self, dashboard, random_string):
        segment_title = random_string
        self._create_segment_helper(dashboard, segment_title)

        self.segments_list_page.delete_segment(segment_title)
        self.segments_list_page.check_if_segment_not_found(segment_title)

    def _create_segment_helper(self, dashboard, segment_title: str):
        segments_list_page = dashboard.go_to_segments_list()
        new_segment_page = segments_list_page.go_to_create_segment()
        new_segment_page.create_new_segment(segment_title)
