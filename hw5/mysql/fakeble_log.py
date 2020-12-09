import random
from abc import abstractmethod

from faker import Faker


class FakeableLog:
    """ Класс, позволяющий создавать фейковые логи """
    @abstractmethod
    def __init__(self, ip, time, method, url, status_code, bytes_sent):
        pass

    @classmethod
    def fake(cls):  # Что-то типа фабрики, которая производит фейковый лог
        faker = Faker()
        return cls(
            ip=faker.ipv4(),
            time=faker.date_time_between(start_date='-30d', end_date='now'),
            method=faker.http_method(),
            url=faker.uri(),
            status_code=random.choice([200, 302, 404, 500]),
            bytes_sent=random.randint(1, 10000),
        )
