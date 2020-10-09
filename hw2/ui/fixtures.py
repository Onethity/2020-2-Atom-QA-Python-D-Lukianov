import pytest
import random
import string

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from ui.pages.create_new_campaign_page import CreateNewCampaignPage
from ui.pages.create_new_segment_page import CreateNewSegmentPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.main_page import MainPage
from ui.pages.segments_list_page import SegmentsListPage
from ui.secret import ACCOUNT_CREDENTIALS


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "80.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://{}/wd/hub".format(selenoid),
            desired_capabilities=capabilities)
    else:
        if browser == 'chrome':
            manager = ChromeDriverManager(version=version, log_level=0)
            driver = webdriver.Chrome(manager.install())
        elif browser == 'chromium':
            manager = ChromeDriverManager(version=version, chrome_type=ChromeType.CHROMIUM, log_level=0)
            driver = webdriver.Chrome(manager.install())
        elif browser == 'firefox':
            manager = GeckoDriverManager(version=version, log_level=0)
            driver = webdriver.Firefox(executable_path=manager.install())
        else:
            raise UnsupportedBrowserException(f'Unsupported browser "{browser}". You must type one of "chrome", "chromium" or "firefox"')

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def dashboard(driver, secrets):
    """ Фикстура для авторизации """
    MainPage(driver).auth(secrets['login'], secrets['password'])
    return DashboardPage(driver)


@pytest.fixture(scope='function')
def secrets():
    """ Фикстура, содержащая секретные данные """
    return ACCOUNT_CREDENTIALS


@pytest.fixture(scope='function')
def random_string():
    """ Генерация случайной строки """
    letters = string.ascii_letters
    result = 'test_' + ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    return result
