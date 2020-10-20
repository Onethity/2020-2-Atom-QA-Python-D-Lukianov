import pytest

from api.client.mytarget_api_client import MytargetApiClient


class BaseTestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, settings, secrets):
        self.client: MytargetApiClient = MytargetApiClient(
            base_url=settings.url,
            login=secrets['login'],
            password=secrets['password']
        )
