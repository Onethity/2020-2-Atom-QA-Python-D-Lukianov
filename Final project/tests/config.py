""" Конфигурация для тестов """
CONFIG = {
    'app': {
        'host': 'myapp',
        'port': 4515,
    },

    'mock': {
        'host': 'vk_id_mock',
        'port': 4516,
    },

    'db': {
        'host': 'db',
        'port': 3306,
        'user': 'test_qa',
        'password': 'qa_test',
        'db_name': 'technoatom',
    },
}

APP_FULL_URL = f"http://{CONFIG['app']['host']}:{CONFIG['app']['port']}/"
MOCK_FULL_URL = f"http://{CONFIG['mock']['host']}:{CONFIG['mock']['port']}/"
