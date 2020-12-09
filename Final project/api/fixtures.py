import pytest

from api.client.myapp_client import MyappApiClient


@pytest.fixture(scope='function')
def myapp_api_client(app_full_url, new_root_user):
    return MyappApiClient(
        app_full_url,
        auth=True,
        username=new_root_user.username,
        password=new_root_user.password,
    )


@pytest.fixture(scope='function')
def myapp_api_client_no_auth(app_full_url):
    return MyappApiClient(app_full_url, auth=False)
