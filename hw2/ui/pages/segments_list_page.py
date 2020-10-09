from selenium.common.exceptions import TimeoutException

from ui.locators.locators import SegmentsListLocators
from ui.pages.base_page import BasePage
from ui.pages.create_new_segment_page import CreateNewSegmentPage


class SegmentsListPage(BasePage):
    locators = SegmentsListLocators()

    def go_to_create_segment(self):
        """ Переход к созданию нового сегмента """
        try:
            self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON)
        except TimeoutException:
            self.click(self.locators.CREATE_FIRST_SEGMENT_BUTTON)

        return CreateNewSegmentPage(self.driver)

    def check_if_segment_exists(self, segment_title):
        """ Проверка сегмента на существование """
        self.send_keys(self.locators.SEARCH_FIELD, segment_title)
        # Сегмент существует, если в suggestions box есть опции
        self.find(self.locators.SEARCH_SUGGESTION_OPTION)

    def delete_segment(self, segment_title):
        """ Удаление сегмента """
        self.send_keys(self.locators.SEARCH_FIELD, segment_title)
        self.click(self.locators.SEARCH_SUGGESTION_OPTION)
        self.click(self.locators.SEGMENT_DELETE_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def check_if_segment_not_found(self, segment_title):
        """ Проверка, что сегмент не существует """
        self.send_keys(self.locators.SEARCH_FIELD, segment_title)
        self.find(self.locators.SEARCH_NOT_FOUND)
