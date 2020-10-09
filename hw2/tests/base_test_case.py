import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.create_new_campaign_page import CreateNewCampaignPage
from ui.pages.create_new_segment_page import CreateNewSegmentPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.main_page import MainPage
from selenium import webdriver

from ui.pages.segments_list_page import SegmentsListPage


class BaseTestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver: webdriver = driver

        self.main_page: MainPage = MainPage(driver)
        self.dashboard_page: DashboardPage = DashboardPage(driver)
        self.create_new_campaign_page:CreateNewCampaignPage = CreateNewCampaignPage(driver)
        self.segments_list_page: SegmentsListPage = SegmentsListPage(driver)
        self.create_new_segment_page: CreateNewSegmentPage = CreateNewSegmentPage(driver)
