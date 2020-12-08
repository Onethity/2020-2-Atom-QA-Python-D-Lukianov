import pytest

from api.client.myapp_client import MyappApiClient
from db.mysql_client import MysqlConnection


class BaseApiTestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, myapp_api_client, db_connection):
        self.myapp_client: MyappApiClient = myapp_api_client
        self.mysql_client: MysqlConnection = db_connection
