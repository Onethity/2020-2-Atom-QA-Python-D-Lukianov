import urllib.parse


class MyappApiEndpoints:
    """ Эндпоинты api приложения Myapp """
    def __init__(self, base_url):
        self.base_url = base_url

    def get_add_user_url(self):
        """ Добавление пользователя """
        return self._join_url('/api/add_user')

    def get_delete_user_url(self, username):
        """ Удаление пользователя """
        return self._join_url(f'/api/del_user/{username}')

    def get_block_user_url(self, username):
        """ Блокировка пользователя """
        return self._join_url(f'/api/block_user/{username}')

    def get_accept_user_url(self, username):
        """ Разблокировка пользователя """
        return self._join_url(f'/api/accept_user/{username}')

    def get_status_url(self):
        """ Статус приложения """
        return self._join_url('/status')

    def auth(self):
        return self._join_url('/login')

    def logout(self):
        return self._join_url('/logout')

    def _join_url(self, endpoint):
        """ Добавление эндпоинта к базовому url"""
        return urllib.parse.urljoin(self.base_url, endpoint)


