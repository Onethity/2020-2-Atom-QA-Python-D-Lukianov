import time

from ui.locators.locators import CreateNewSegmentLocators
from ui.pages.base_page import BasePage


class CreateNewSegmentPage(BasePage):
    locators = CreateNewSegmentLocators()

    def create_new_segment(self, segment_title: str):
        self.click(self.locators.APPS_AND_GAMES_BUTTON)
        self.click(self.locators.PLAYED_AND_PAID_CHECKBOX)
        self.click(self.locators.ADD_NEW_SEGMENT_BUTTON)
        self.send_keys(self.locators.SEGMENT_TITLE_FIELD, segment_title)
        self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON)
