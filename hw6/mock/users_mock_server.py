import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import CONFIG
from mock.database.database_client import DatabaseConnection, DatabaseError


class MockHttpProcessor(BaseHTTPRequestHandler):
    """ Обработчик HTTP запросов """

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _get_request_data(self):
        content_length = int(self.headers['Content-Length'])
        return self.rfile.read(content_length).decode()

    def do_GET(self):
        """ Обработчик GET запросов """
        if self.path == '/':  # По GET запросу на корень выдаем список пользователей
            try:
                db = DatabaseConnection()
                users = db.get_users().encode()
                self._set_headers(status_code=200)
                self.wfile.write(users)
            except DatabaseError:
                self._set_headers(status_code=500)

        elif self.path == '/timeout':  # Запрос с искусственным таймаутом
            time.sleep(5)
            self._set_headers(status_code=200)

        elif self.path == '/500':  # Запрос, который возвращает 500
            self._set_headers(status_code=500)

        else:
            self._set_headers(status_code=404)

    def do_POST(self):
        """ Обработчик POST запросов """
        if self.path == '/':  # При POST запросе на корень добавляем нового пользователя
            username = self._get_request_data()

            try:
                db = DatabaseConnection()
                db.add_user(username)
                self._set_headers()
            except DatabaseError:
                self._set_headers(status_code=500)

        elif self.path == '/auth':  # Проверка авторизации
            auth_header = self.headers.get('Authorization')
            if not auth_header:  # Если нет хедера с авторизацией
                self._set_headers(status_code=412)
                return

            username = self._get_request_data()
            if username != auth_header:  # Если запрашиваемый пользователь не совпадает с заголовком
                self._set_headers(status_code=400)
                return

            db = DatabaseConnection()
            if db.does_user_exist(username):  # Если пользователь сущесвует
                self._set_headers(status_code=200)
            else:
                self._set_headers(status_code=403)

        else:
            self._set_headers(status_code=404)

    def do_DELETE(self):
        """ Обработчик DELETE запросов """
        if self.path == '/':  # По DELETE запросу на корень удаляем пользователя
            username = self._get_request_data()
            try:
                db = DatabaseConnection()
                db.delete_user(username)
                self._set_headers()
            except DatabaseError:
                self._set_headers(status_code=400)
        else:
            self._set_headers(status_code=404)


class UsersHTTPServer:
    """ Moсk HTTP сервер"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHttpProcessor

        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        server = threading.Thread(target=self.server.serve_forever, daemon=True)
        server.start()

        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()


def start_mock(host, port):
    """ Запуск mock-сервера """
    server = UsersHTTPServer(host, port)
    server.start()

    return server

if __name__ == '__main__':
    start_mock(host=CONFIG['mock']['host'], port=CONFIG['mock']['port'])
    while True:
        pass
