import json


class Response:
    """ Объект ответа на запрос"""

    def __init__(self, body, status_code, headers):
        self.body = body
        self.status_code = status_code
        self.headers = headers

    def json(self):
        """ Парсинг json ответа """
        return json.loads(self.body)

    def __repr__(self):
        """ Вывод ответа в формате json """
        return json.dumps({
            'status_code': self.status_code,
            'body': self.body,
            'headers': self.headers,
        })
