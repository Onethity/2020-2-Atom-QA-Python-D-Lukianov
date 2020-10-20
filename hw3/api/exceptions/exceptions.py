class SegmentDoesNotExist(Exception):
    """ Сегмент не существует """
    pass


class ApiErrorException(Exception):
    """ Внутренняя ошибка API """
    pass


class ResponseStatusCodeException(Exception):
    """ Код ответа сервера не соответсвует ожидаемому """
    def __init__(self, status_code, message=''):
        self.status_code = status_code
        super().__init__(message)

