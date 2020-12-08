import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from ui.pages.login_page import LoginPage
from ui.pages.welcome_page import WelcomePage


@pytest.fixture(scope='function')
def driver(app_full_url, request: FixtureRequest):
    selenoid = request.config.getoption('--selenoid')

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "87.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://{}/wd/hub".format(selenoid),
            desired_capabilities=capabilities)
    else:
        manager = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, log_level=0)
        driver = webdriver.Chrome(manager.install())

    driver.maximize_window()
    driver.get(app_full_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def welcome_page(new_user, driver):
    LoginPage(driver).auth(new_user.username, new_user.password)

    return WelcomePage(driver)
