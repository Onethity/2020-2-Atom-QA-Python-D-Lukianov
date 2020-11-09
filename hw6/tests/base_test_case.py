import pytest

from client.socket_client import HTTPClient


class BaseTestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, http_client):
        self.client: HTTPClient = http_client