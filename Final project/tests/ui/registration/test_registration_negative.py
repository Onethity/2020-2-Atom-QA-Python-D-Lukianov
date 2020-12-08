import allure
import pytest
from allure_commons.types import AttachmentType

from tests.ui.base_ui_test_case import BaseUITestCase


@allure.feature('UI')
@allure.story('Негативные кейсы на регистрацию')
class TestRegistration(BaseUITestCase):
    @allure.title('Негативный тест на регистрацию: пароли не совпадают')
    @pytest.mark.UI
    def test_registration_different_passwords(self, random_username, random_password, random_email):
        """
        Негативный тест на регистрацию: пароли не совпадают

        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username случайным именем
        Шаг 3. Заполняем поле email случайным адресом
        Шаг 4. Заполняем password случайным паролем
        Шаг 5. Заполняем password repeat строкой 'wrong_password'
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: флеш-сообщение "Passwords must match", пользователь не добавлен в базу
        """
        registration_page = self.login_page.go_to_registration_page()

        registration_page.registration(random_username, random_password, random_email, password_repeat='wrong_password')

        allure.attach(name='Reg error', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert not self.mysql_client.builder.does_user_exist(random_username), 'Пользователь добавлен в базу'
        assert self.registration_page.get_flash_message_text() == 'Passwords must match', 'Неверное сообщение об ошибке'

    @allure.title('Негативный тест на регистрацию: неверный формат email')
    @pytest.mark.UI
    def test_registration_wrong_email(self, random_username, random_password):
        """
        Негативный тест на регистрацию: неверный формат email

        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username случайным именем
        Шаг 3. Заполняем поле email строкой "this_is_wrong_email"
        Шаг 4. Заполняем password случайным паролем
        Шаг 5. Заполняем password repeat тем же паролем
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: флеш-сообщение "Invalid email address", пользователь не добавлен в базу
        """
        registration_page = self.login_page.go_to_registration_page()

        registration_page.registration(random_username, random_password, 'this_is_wrong_email')

        allure.attach(name='Reg error', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert not self.mysql_client.builder.does_user_exist(random_username), 'Пользователь добавлен в базу'
        assert self.registration_page.get_flash_message_text() == 'Invalid email address', \
            'Неверное сообщение об ошибке'

    @allure.title('Негативный тест на регистрацию: пользователь с таким email уже существует')
    @pytest.mark.UI
    def test_registration_same_email(self, new_user):
        """
        Негативный тест на регистрацию: пользовователь с таким email уже есть в базе

        Шаг 1. Создаем пользователя в бд: <random_username>, <random_email>, <random_password>
        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username другим именем - <random_username>_2
        Шаг 3. Заполняем поле email тем же самым значением - <random_email>
        Шаг 4. Заполняем password тем же самым паролем <random_password>
        Шаг 5. Заполняем password repeat тем же паролем
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: флеш-сообщение "Email address already in use", пользователь не добавлен в базу
        """
        username = new_user.username + '_2'
        password = new_user.password
        email = new_user.email

        registration_page = self.login_page.go_to_registration_page()
        registration_page.registration(username, password, email)

        allure.attach(name='Reg error', body=self.registration_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)

        assert not self.mysql_client.builder.does_user_exist(username), 'Пользователь добавлен в базу'
        assert self.registration_page.get_flash_message_text() == 'Email address already in use', \
            'Неверное сообщение об ошибке'

    @allure.title('Негативный тест на регистрацию: слишком длинный пароль (260 символов)')
    @pytest.mark.UI
    def test_registration_long_password(self, random_username, random_email):
        """
        Негативный тест на регистрацию: неверный формат email

        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username случайным именем
        Шаг 3. Заполняем поле email случайным адресом
        Шаг 4. Заполняем password строкой 270 символов
        Шаг 5. Заполняем password repeat тем же паролем
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: флеш-сообщение "Password too long", пользователь не добавлен в базу
        """
        registration_page = self.login_page.go_to_registration_page()

        registration_page.registration(random_username, 'a' * 260, random_email)

        allure.attach(name='Reg error', body=self.driver.get_screenshot_as_png(),
                      attachment_type=AttachmentType.PNG)

        assert not self.mysql_client.builder.does_user_exist(random_username), 'Пользователь добавлен в базу'
        assert self.registration_page.get_flash_message_text() == 'Password too long', \
            'Неверное сообщение об ошибке'

    @allure.title('Негативный тест на регистрацию: пользователь с таким username уже существует')
    @pytest.mark.UI
    def test_registration_same_username(self, new_user):
        """
        Негативный тест на регистрацию: пользовователь с таким email уже есть в базе

        Шаг 1. Создаем пользователя в бд: <random_username>, <random_email>, <random_password>
        Шаг 1. Переходим с главной на страницу регистрации
        Шаг 2. Заполняем поле username тем же самым именем - <random_username>
        Шаг 3. Заполняем поле email другим значением - '2_' + <random_email>
        Шаг 4. Заполняем password тем же самым паролем <random_password>
        Шаг 5. Заполняем password repeat тем же паролем
        Шаг 6. Нажимаем чекбокс  "I accept that I want to be a SDET"
        Шаг 7. Нажимаем кнопку REGISTER

        Ожидаемое поведение: флеш-сообщение "User already exist"
        """
        username = new_user.username
        password = new_user.password
        email = '2_' + new_user.email

        registration_page = self.login_page.go_to_registration_page()
        registration_page.registration(username, password, email)

        allure.attach(name='Reg error', body=self.registration_page.get_screenshot(),
                      attachment_type=AttachmentType.PNG)

        assert self.registration_page.get_flash_message_text() == 'User already exist', \
            'Неверное сообщение об ошибке'


