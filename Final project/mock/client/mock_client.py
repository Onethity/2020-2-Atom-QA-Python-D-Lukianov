import urllib.parse

import requests


class MockApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_vk_id(self, username, vk_id):
        requests.post(
            urllib.parse.urljoin(self.base_url, '/vk_id/add_user'),
            json={
                'username': username,
                'vk_id': vk_id
            }
        )

        return True
