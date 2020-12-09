from dataclasses import dataclass
from datetime import datetime

from mysql.fakeble_log import FakeableLog


@dataclass
class LogDataEntity(FakeableLog):
    """ Представление данных из лога в виде dataclass """
    ip: str
    time: datetime
    method: str
    url: str
    status_code: int
    bytes_sent: int
