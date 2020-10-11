from selenium.webdriver.common.by import By


class MainPageLocators:
    OPEN_LOGIN_FORM_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')


class DashboardLocators:
    EMAIL_BOX = (By.XPATH, '//div[@class="right-module-userNameWrap-34ibLS"]')
    CREATE_NEW_CAMPAIGN_BUTTON = (By.XPATH, '//div[@class="button-module-textWrapper-3LNyYP"'
                                            ' and text()="Создать кампанию"]')
    CREATE_FIRST_CAMPAIGN_BUTTON = (By.XPATH, '//a[@href="/campaign/new"]')
    SEARCH_FIELD = (By.XPATH, '//input[contains(@class, "multiSelectSuggester-module-searchInput-34I1ra")]')
    SEARCH_SUGGESTIONS_BOX = (By.XPATH, '//div[@class="suggesterOptionsList-module-suggesterMode-2L4ezq"]')
    SEGMENTS_LIST_BUTTON = (By.XPATH, '//a[@href="/segments"]')


class CreateNewCampaignLocators:
    TARGET_TRAFFIC_BUTTON = (By.XPATH, '//div[@class="column-list-item__title js-title" and text()="Трафик"]')
    URL_FIELD = (By.XPATH, '//input[contains(@data-gtm-id, "ad_url_text")]')
    CAMPAIGN_TITLE_FIELD = (By.XPATH, '//div[contains(@class, "campaign-name")]//input')
    TEASER_FORMAT_ITEM_BUTTON = (By.XPATH, '//div[@id="149"]')
    TEASER_TITLE_FIELD = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')
    TEASER_TEXT_FIELD = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')
    TEASER_IMAGE_UPLOAD_FILE_FIELD = (By.XPATH, '//input[@data-gtm-id="load_image_btn_90_75"]')
    IMAGE_CROPPER_SAVE_BUTTON = (By.XPATH, '//input[contains(@class, "js-save")]')
    SAVE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class, "js-save-button-wrap")]/button')


class SegmentsListLocators:
    CREATE_NEW_SEGMENT_BUTTON = (By.XPATH, '//div[contains(@class, "js-create-button-wrap")]/button')
    CREATE_FIRST_SEGMENT_BUTTON = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    SEARCH_FIELD = (By.XPATH, '//input[contains(@class, "suggester-module-searchInput-1dyLvN ")]')
    SEARCH_SUGGESTION_OPTION = (By.XPATH, '//li[contains(@class, "suggester-module-option-1kQRIM")]')
    SEARCH_NOT_FOUND = (By.XPATH, '//li[@class="optionsList-module-optionNothing-1pecr_"]')
    SEGMENT_DELETE_BUTTON = (By.XPATH, '//span[contains(@class, "cells-module-removeCell-2tweYp")]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')


class CreateNewSegmentLocators:
    APPS_AND_GAMES_BUTTON = (By.XPATH, '//div[text() = "Приложения и игры в соцсетях"]')
    PLAYED_AND_PAID_CHECKBOX = (By.XPATH, '//div[contains(@class, "adding-segments-source__header")]/input')
    ADD_NEW_SEGMENT_BUTTON = (By.XPATH, '//div[contains(@class, "js-add-button")]/button')
    CREATE_NEW_SEGMENT_BUTTON = (By.XPATH, '//div[contains(@class, "create-segment-form__btn-wrap")]/button')
    SEGMENT_TITLE_FIELD = (By.XPATH, '//div[@class="js-segment-name"]//input')
