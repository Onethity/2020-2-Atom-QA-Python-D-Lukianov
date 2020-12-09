import pymysql
from pymysql.cursors import DictCursor

from mysql.base_mysql_client import BaseMysqlConnection
from mysql.plain.query_builder import PlainQueryBuilder


class MysqlPlainConnection(BaseMysqlConnection):
    """ Mysql клиент для работы с базой через чистые запросы """
    def __init__(self, host, port, user, password, db_name, logs_table_name):
        super().__init__(host, port, user, password, db_name)

        self.builder = PlainQueryBuilder(
            logs_table_name=logs_table_name
        )

        self.init_tables()

    def connect(self):
        connection = self._get_connection()

        connection.query(f'DROP DATABASE IF EXISTS {self.db_name}')
        connection.query(f'CREATE DATABASE IF NOT EXISTS {self.db_name}')

        connection.close()

        return self._get_connection(is_db_created=True)

    def _get_connection(self, is_db_created=False):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if is_db_created else None,
            cursorclass=DictCursor,
            autocommit=True,
            charset='utf8',
        )

    def execute_query(self, query):
        """ Выполнить запрос """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def init_tables(self):
        """ Инициализация таблиц """
        self.execute_query(self.builder.create_logs_table())
