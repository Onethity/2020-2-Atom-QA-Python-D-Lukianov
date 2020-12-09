CONFIG = {
    'app': {
        'host': 'localhost',
        'port': 4210,
    },

    'mock': {
        'host': 'localhost',
        'port': 4212,
    },
}

APP_FULL_URL = f"http://{CONFIG['app']['host']}:{CONFIG['app']['port']}/"
MOCK_FULL_URL = f"http://{CONFIG['mock']['host']}:{CONFIG['mock']['port']}/"

