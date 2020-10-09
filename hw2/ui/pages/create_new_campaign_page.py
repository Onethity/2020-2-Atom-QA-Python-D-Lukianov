import os

import pytest

from ui.locators.locators import CreateNewCampaignLocators
from ui.pages.base_page import BasePage


class CreateNewCampaignPage(BasePage):
    locators = CreateNewCampaignLocators()

    def create_new_campaign(self, campaign_title):
        self.click(self.locators.TARGET_TRAFFIC_BUTTON)
        self.send_keys(self.locators.URL_FIELD, 'example.com')
        self.send_keys(self.locators.CAMPAIGN_TITLE_FIELD, campaign_title)
        self.click(self.locators.TEASER_FORMAT_ITEM_BUTTON)

        self.send_keys(self.locators.TEASER_TITLE_FIELD, 'Test teaser title')
        self.send_keys(self.locators.TEASER_TEXT_FIELD, 'Test teaser text')
        self.send_keys(self.locators.TEASER_IMAGE_UPLOAD_FILE_FIELD,
                       os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'resources', 'teaser_img.jpg')),
                       to_clear=False,
                       should_be_visible=False)

        self.click(self.locators.IMAGE_CROPPER_SAVE_BUTTON)
        self.click(self.locators.SAVE_CAMPAIGN_BUTTON)
