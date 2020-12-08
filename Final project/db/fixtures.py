import pytest

from db.mysql_client import MysqlConnection


@pytest.fixture
def db_connection(config):
    return MysqlConnection(
        config['db']['host'],
        config['db']['port'],
        config['db']['user'],
        config['db']['password'],
        config['db']['db_name']
    )
