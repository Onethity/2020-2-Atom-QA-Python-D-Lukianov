import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
    """ Orm модель лога """
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), default='', nullable=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(Boolean, default='')
    active = Column(Boolean, default='')
    start_active_time = Column(DateTime, default=sqlalchemy.sql.null(), nullable=True)

    def __init__(self, username, password, email, access, active, start_active_time):
        self.username = username
        self.password = password
        self.email = email
        self.access = access
        self.active = active
        self.start_active_time = start_active_time

    def __repr__(self):
        """ Красивый вывод модели для отладки """
        return "User(" \
               f"id = {self.id}, " \
               f"username = {self.username}, " \
               f"password = {self.password}, " \
               f"email = {self.email}, " \
               f"access = {self.access}, " \
               f"active = {self.active}, " \
               f"start_active_time = {self.start_active_time}, " \
               f");"
