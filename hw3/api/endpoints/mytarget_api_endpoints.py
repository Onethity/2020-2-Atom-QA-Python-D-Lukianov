from urllib.parse import urljoin


class MytargetApiEndpoints:
    def __init__(self, base_url):
        self.base_url = base_url

    AUTH = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

    def get_csrf_endpoint(self):
        """ Эндпоинт для получения csrf токена """
        return urljoin(self.base_url, 'csrf/')

    def get_create_segment_endpoint(self):
        """ Эндпоинт для создания нового сегмента """
        return urljoin(self.base_url, 'api/v2/remarketing/segments.json?'
                                      'fields=relations__object_type,relations__object_id,relations__params,'
                                      'relations_count,id,name,pass_condition,created,campaign_ids,users,flags')

    def get_segment_data_endpoint(self, segment_id):
        """ Эндпоинт для удаления сегмента """
        return urljoin(self.base_url, f'api/v2/remarketing/segments/{segment_id}.json')
