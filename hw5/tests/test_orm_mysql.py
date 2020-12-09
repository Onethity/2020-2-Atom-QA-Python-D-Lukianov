import pytest

from mysql.orm.models.log_data import LogDataModel
from mysql.orm.query_builder import OrmQueryBuilder


class TestOrmMysql:
    """ Тесты на orm MySQL """
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_connection):
        self.connection = mysql_orm_connection
        self.query_builder: OrmQueryBuilder = self.connection.builder

    def test_example(self):
        """ Добавляем лог в базу и проверяем, что он добавлен """
        fake_log = LogDataModel.fake()
        self.query_builder.insert_log(fake_log)
        log_inserted = self.query_builder.select_logs()[0]

        assert fake_log == log_inserted
