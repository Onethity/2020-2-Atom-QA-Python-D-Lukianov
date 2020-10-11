from selenium.common.exceptions import TimeoutException

from ui.locators.locators import DashboardLocators
from ui.pages.base_page import BasePage
from ui.pages.create_new_campaign_page import CreateNewCampaignPage
from ui.pages.segments_list_page import SegmentsListPage


class DashboardPage(BasePage):
    locators = DashboardLocators()

    def get_user_login(self):
        return self.find(self.locators.EMAIL_BOX).get_attribute('title')

    def go_to_new_campaign(self):
        """ Переход на страницу создания кампании """
        try:
            self.click(self.locators.CREATE_NEW_CAMPAIGN_BUTTON)
        except TimeoutException:
            self.click(self.locators.CREATE_FIRST_CAMPAIGN_BUTTON)

        return CreateNewCampaignPage(self.driver)

    def go_to_segments_list(self):
        """ Переход к списку сегментов """
        self.click(self.locators.SEGMENTS_LIST_BUTTON)
        return SegmentsListPage(self.driver)

    def check_if_campaign_exists(self, campaign_title: str):
        """ Проверка существования кампании """
        self.send_keys(self.locators.SEARCH_FIELD, campaign_title)

        # Кампания существует если suggestions box отображается
        self.find(self.locators.SEARCH_SUGGESTIONS_BOX)
