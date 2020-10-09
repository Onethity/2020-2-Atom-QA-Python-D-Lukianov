from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions

from ui.locators.locators import DashboardLocators
from ui.pages.base_page import BasePage
from ui.pages.create_new_campaign_page import CreateNewCampaignPage
from ui.pages.segments_list_page import SegmentsListPage


class DashboardPage(BasePage):
    locators = DashboardLocators()

    def go_to_new_campaign(self):
        try:
            self.click(self.locators.CREATE_NEW_CAMPAIGN_BUTTON)
        except TimeoutException:
            self.click(self.locators.CREATE_FIRST_CAMPAIGN_BUTTON)

        return CreateNewCampaignPage(self.driver)

    def go_to_segments_list(self):
        self.click(self.locators.SEGMENTS_LIST_BUTTON)
        return SegmentsListPage(self.driver)

    def check_if_campaign_exists(self, campaign_title: str):
        self.send_keys(self.locators.SEARCH_FIELD, campaign_title)

        # A campaign exists if search suggestions box is shown
        self.find(self.locators.SEARCH_SUGGESTIONS_BOX)
