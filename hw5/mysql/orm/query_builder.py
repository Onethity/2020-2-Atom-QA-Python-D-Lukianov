from sqlalchemy.engine import Connection

from mysql.base_builder import BaseQueryBuilder
from mysql.orm.models.log_data import Base, LogDataModel


class OrmQueryBuilder(BaseQueryBuilder):
    def __init__(self, connection: Connection, session, logs_table_name):
        self.connection = connection
        self.engine = self.connection.engine
        self.session = session
        self.table_name = logs_table_name

    def create_logs_table(self):
        """ Создание таблицы для логов """
        if not self.engine.dialect.has_table(self.engine, self.table_name):
            Base.metadata.tables[self.table_name].create(self.engine)

    def insert_log(self, log: LogDataModel):
        """ Вставка лога в таблицу """
        self.session.add(log)
        self.session.commit()

    def select_logs(self):
        """ Выбирает все логи """
        return self.session.query(LogDataModel).all()
