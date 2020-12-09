import pytest

from config import CONFIG
from mysql.orm.mysql_orm_client import MysqlOrmConnection
from mysql.plain.mysql_plain_client import MysqlPlainConnection


@pytest.fixture(scope='session')
def config():
    return CONFIG


@pytest.fixture(scope='session')
def mysql_plain_connection(config):
    return MysqlPlainConnection(
        host=config['host'],
        port=config['port'],
        user=config['user'],
        password=config['password'],
        db_name=config['plain_sql']['db_name'],
        logs_table_name=config['plain_sql']['logs_table_name'],
    )


@pytest.fixture(scope='session')
def mysql_orm_connection(config):
    return MysqlOrmConnection(
        host=config['host'],
        port=config['port'],
        user=config['user'],
        password=config['password'],
        db_name=config['orm_sql']['db_name'],
        logs_table_name=config['orm_sql']['logs_table_name'],
    )
