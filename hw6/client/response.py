import json


class Response:
    """ Объект ответа на запрос"""
    def __init__(self, body, status_code):
        self.body = body
        self.status_code = status_code

    def json(self):
        return json.loads(self.body)
