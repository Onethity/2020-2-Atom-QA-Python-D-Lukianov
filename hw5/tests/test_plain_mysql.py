import pytest

from mysql.plain.entity.log_data import LogDataEntity
from mysql.plain.mysql_plain_client import MysqlPlainConnection
from mysql.plain.query_builder import PlainQueryBuilder


class TestPlainMysql:
    """ Тесты с 'чистым' sql клиентом"""
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_plain_connection):
        self.connection: MysqlPlainConnection = mysql_plain_connection
        self.query_builder: PlainQueryBuilder = mysql_plain_connection.builder

    def test_insert_log(self):
        """ Добавляем лог в базу и проверяем, что он добавлен """
        fake_log = LogDataEntity.fake()
        self.connection.execute_query(self.query_builder.insert_log(fake_log))

        log_inserted = self.connection.execute_query(self.query_builder.select_logs())[0]
        
        assert log_inserted['ip'] == fake_log.ip
        assert log_inserted['time'] == fake_log.time
        assert log_inserted['method'] == fake_log.method
        assert log_inserted['url'] == fake_log.url
        assert log_inserted['status_code'] == fake_log.status_code
        assert log_inserted['bytes_sent'] == fake_log.bytes_sent
