from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    FLASH_MESSAGE = (By.XPATH, '//div[@id="flash"]')
    GO_TO_REGISTRATION = (By.XPATH, '//a[@href="/reg"]')


class RegistrationPageLocators:
    USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    PASSWORD_REPEAT_INPUT = (By.XPATH, '//input[@name="confirm"]')
    ACCEPT_CHECKBOX = (By.XPATH, '//input[@name="term"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@type="submit"]')
    FLASH_MESSAGE = (By.XPATH, '//div[@id="flash"]')


class WelcomePageLocators:
    LOGGED_AS = (By.XPATH, '//div[@id="login-name"]/ul/li[1]')
    WHATS_AN_API_ICON = (By.XPATH, '(//img[@class="uk-overlay-scale"])[1]')
    FUTURE_OF_INTERNET_ICON = (By.XPATH, '(//img[@class="uk-overlay-scale"])[2]')
    SMTP_ICON = (By.XPATH, '(//img[@class="uk-overlay-scale"])[3]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    LOGO_BUTTON = (By.XPATH, '//a[contains(@class, "uk-navbar-brand")]')
    MENU_HOME_BUTTON = (By.XPATH, '//a[text()="HOME"]')
    MENU_PYTHON_BUTTON = (By.XPATH, '//a[text()="Python"]')
    MENU_PYTHON_HISTORY = (By.XPATH, '//a[text()="Python history"]')
    MENU_ABOUT_FLASK = (By.XPATH, '//a[text()="About Flask"]')
    MENU_LINUX_BUTTON = (By.XPATH, '//a[text()="Linux"]')
    CENTOS_DOWNLOAD = (By.XPATH, '//a[text()="Download Centos7"]')
    MENU_NETWORK = (By.XPATH, '//a[text()="Network"]')
    WIRESHARK_NEWS = (By.XPATH, '//a[text()="News"]')
    WIRESHARK_DOWNLOAD = (By.XPATH, '//a[text()="Download"]')
    TCP_DUMP_EXAMPLES = (By.XPATH, '//a[text()="Examples"]')
    VK_ID = (By.XPATH, '//div[@id="login-name"]/ul/li[2]')
    ZEN_OF_PYTHON = (By.XPATH, '//footer//p[2]')


class Error404PageLocators:
    ERROR_TEXT = (By.XPATH, '//span[@id="text"]')
    ERROR_IMG = (By.XPATH, '//div[@id="error"]/img')
