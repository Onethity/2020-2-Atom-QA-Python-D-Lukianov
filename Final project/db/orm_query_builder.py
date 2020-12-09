import allure
from sqlalchemy.engine import Connection

from db.models.user import UserModel


class OrmQueryBuilder:
    def __init__(self, connection: Connection, session):
        self.connection = connection
        self.engine = self.connection.engine
        self.session = session

    @allure.step('Запрос в БД на добавление пользователя')
    def create_user(self, user: UserModel):
        self.session.add(user)
        self.session.commit()

    @allure.step('Удаление пользователя из БД')
    def delete_user(self, user: UserModel):
        self.session.delete(user)
        self.session.commit()

    @allure.step('Проверка пользователя на существование в БД')
    def does_user_exist(self, username):
        user = self._get_user_by_username(username)
        return False if user is None else True

    @allure.step('Блокировка пользователя в БД')
    def block_user(self, username):
        user = self._get_user_by_username(username)
        user.access = False
        self.session.commit()

    @allure.step('Проверка пользователя на блокировку в БД')
    def is_user_accepted(self, username):
        user = self._get_user_by_username(username)
        return user.access

    @allure.step('Проверка пользователя на активность ("active" в бд)')
    def is_user_active(self, username):
        user = self._get_user_by_username(username)
        return user.active

    @allure.step('Получение active_time из базы')
    def get_active_time(self, username):
        user = self._get_user_by_username(username)
        return user.start_active_time

    @allure.step('Получение данных о пользователе {username} из базы')
    def _get_user_by_username(self, username):
        self.session.commit()  # Транзакцию нужно закоммитить, чтобы подгрузить свежие данные
        user = self.session.query(UserModel).filter(UserModel.username == username).first()
        return user
