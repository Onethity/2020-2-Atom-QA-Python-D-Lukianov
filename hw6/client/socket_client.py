import json
import socket
import urllib.parse

from client.response import Response

RETRY_COUNT = 3


class HTTPClient:
    """ HTTP клиент на основе сокетов """

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, endpoint, headers={}):
        """ GET запрос """
        request = f'GET {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n'
        request += self._add_headers_to_request(headers)
        return self._send_request(request)

    def post(self, endpoint, data={}, headers={}):
        """ POST запрос """
        if data == {}:
            encoded_data = ''
        else:
            encoded_data = urllib.parse.urlencode(data)

        request = f'POST {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n' \
                  f'Content-Type: application/x-www-form-urlencoded\r\n' \
                  f'Content-Length: {len(encoded_data)}\r\n'
        request += self._add_headers_to_request(headers)
        request += f'{encoded_data}'

        return self._send_request(request)

    def put(self, endpoint, data={}, headers={}):
        """ PUT запрос """
        if data == {}:
            encoded_data = ''
        else:
            encoded_data = urllib.parse.urlencode(data)

        request = f'PUT {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n' \
                  f'Content-Type: application/x-www-form-urlencoded\r\n' \
                  f'Content-Length: {len(encoded_data)}\r\n'
        request += self._add_headers_to_request(headers)
        request += f'{encoded_data}'

        return self._send_request(request)

    def delete(self, endpoint, headers={}):
        request = f'DELETE {endpoint} HTTP/1.1\r\n' \
                  f'Host: {self.host}:{self.port}\r\n'
        request += self._add_headers_to_request(headers)

        return self._send_request(request)

    def _send_request(self, request) -> Response:
        """ Отправка запроса на сервер """
        self._init_socket()
        self.socket.send(request.encode())
        response = self._get_response()
        self._stop_socket()

        # По условию задания необходимо вывести ответ на экран
        print(response.body)

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
        self.socket.settimeout(1.5)

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

    def _add_headers_to_request(self, headers):
        """ Добавление заголовков к запросу """
        request = ''
        for header_name, header_value in headers.items():
            request += f'{header_name}: {header_value}\r\n'
        request += '\r\n'
        return request
