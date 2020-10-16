from dataclasses import dataclass

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest

from api.fixtures import *


def pytest_addoption(parser: Parser):
    parser.addoption('--url', default='https://target.my.com')


@dataclass
class Settings:
    url: str


@pytest.fixture(scope='function')
def settings(request: FixtureRequest):
    return Settings(
        url=request.config.getoption('--url')
    )
