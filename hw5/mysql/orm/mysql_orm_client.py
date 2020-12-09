from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mysql.base_mysql_client import BaseMysqlConnection
from mysql.orm.query_builder import OrmQueryBuilder


class MysqlOrmConnection(BaseMysqlConnection):
    """ Клиент для работы с базой в orm """
    def __init__(self, host, port, user, password, db_name, logs_table_name):
        super().__init__(host, port, user, password, db_name)

        session = sessionmaker(bind=self.connection)
        self.session = session()

        self.builder = OrmQueryBuilder(
            connection=self.connection,
            session=self.session,
            logs_table_name=logs_table_name,
        )

        self.init_tables()

    def connect(self):
        connection = self._get_connection(is_db_created=False)

        connection.execute(f'DROP DATABASE IF EXISTS `{self.db_name}`')
        connection.execute(f'CREATE DATABASE IF NOT EXISTS `{self.db_name}`')
        connection.close()

        return self._get_connection(is_db_created=True)

    def _get_connection(self, is_db_created=False):
        engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db_name=self.db_name if is_db_created else ''
        ))

        return engine.connect()

    def init_tables(self):
        """ Инициирует таблицы для начала работы """
        self.builder.create_logs_table()
