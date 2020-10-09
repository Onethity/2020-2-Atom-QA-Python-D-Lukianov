import pytest
from tests.base_test_case import BaseTestCase


class TestCampaign(BaseTestCase):
    @pytest.mark.UI
    def test_create_campaign(self, dashboard, random_string):
        campaign_title = random_string
        new_campaign_page = dashboard.go_to_new_campaign()
        new_campaign_page.create_new_campaign(campaign_title)
        dashboard.check_if_campaign_exists(campaign_title)
