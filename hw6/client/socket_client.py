import socket
import urllib.parse

from client.response import Response

RETRY_COUNT = 3


class HTTPClient:
    """ HTTP клиент на основе сокетов """

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, endpoint):
        """ GET запрос """
        request = f'GET {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n' \
                  f'\r\n'
        return self._send_request(request)

    def post(self, endpoint, data: dict):
        """ POST запрос """
        encoded_data = urllib.parse.urlencode(data)
        request = f'POST {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n' \
                  f'Content-Type: application/x-www-form-urlencoded\r\n' \
                  f'Content-Length: {len(encoded_data)}\r\n' \
                  f'\r\n' \
                  f'{encoded_data}'

        return self._send_request(request)

    def delete(self, endpoint):
        request = f'DELETE {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n\r\n'

        return self._send_request(request)

    def _send_request(self, request) -> Response:
        """ Отправка запроса на сервер """
        self._init_socket()
        self.socket.send(request.encode())
        response = self._get_response()
        self._stop_socket()

        print(response.json())
        return response

    def _get_response(self):
        """ Чтение ответа """
        total_data = []
        while True:
            data = self.socket.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()

        response = Response(
            body=data[-1],
            status_code=int(data[0].split(' ')[1])
        )

        return response

    def _init_socket(self):
        """ Инициализация сокета """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.5)

        count = 0
        while count < RETRY_COUNT:
            try:
                self.socket.connect((self.host, self.port))
            except ConnectionRefusedError:
                count += 1

            break

    def _stop_socket(self):
        """ Остановка сокета """
        self.socket.close()