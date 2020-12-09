import json
import os


class DatabaseError(Exception):
    pass


class DatabaseConnection:
    """ Небольшой клиент для работы с БД в виде JSON файла """

    def __init__(self, path=None):
        if not path:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database.json'))
            # Это стандартный путь к файлу с БД

        self.path = path
        self.data = self._get_data()  # Информация из БД

    def get_users(self):
        """ Получение списка пользователей """
        return json.dumps(self.data)

    def add_user(self, username):
        """ Добавляение пользователя в базу """
        self.data['users'].append(username)
        self._save_data()

    def delete_user(self, username):
        """ Удаление пользователя из базы """
        try:
            self.data['users'].remove(username)
            self._save_data()
        except ValueError:
            raise DatabaseError

    def does_user_exist(self, username):
        """ Проверяет, существует ли пользователь в БД """
        return username in self.data['users']

    def _get_data(self):
        """ Получение информации из базы """
        try:
            with open(self.path) as database:
                return json.load(database)

        except (FileNotFoundError, TypeError):
            raise DatabaseError

    def _save_data(self):
        """ Сохранение данных в базу """
        try:
            with open(self.path, 'w') as database_file:
                json.dump(self.data, database_file, indent=4)

        except FileNotFoundError:
            raise DatabaseError
