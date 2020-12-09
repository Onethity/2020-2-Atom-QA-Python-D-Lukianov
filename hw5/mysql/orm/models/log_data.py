from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from config import CONFIG
from mysql.fakeble_log import FakeableLog

Base = declarative_base()


class LogDataModel(Base, FakeableLog):
    """ Orm модель лога """
    __tablename__ = CONFIG['orm_sql']['logs_table_name']
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), nullable=False)
    time = Column(DateTime, nullable=False)
    method = Column(String(20), nullable=False)
    url = Column(String(255), nullable=False)
    status_code = Column(Integer, nullable=False)
    bytes_sent = Column(Integer, nullable=False)

    def __init__(self, ip, time, method, url, status_code, bytes_sent):
        self.ip = ip
        self.time = time
        self.method = method
        self.url = url
        self.status_code = status_code
        self.bytes_sent = bytes_sent

    def __repr__(self):
        """ Красивый вывод модели для отладки """
        return "Log Data(" \
               f"id = {self.id}, " \
               f"ip = {self.ip}, " \
               f"time = {self.time}, " \
               f"method = {self.method}, " \
               f"url = {self.url}, " \
               f"status_code = {self.status_code}, " \
               f"bytes_sent = {self.bytes_sent}, " \
               f");"
