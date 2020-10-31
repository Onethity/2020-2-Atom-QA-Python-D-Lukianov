""" Конфигурация базы данных """
CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': '123',

    # База для тестов чистого sql
    'plain_sql': {
        'db_name': 'py_logs_test_plain',
        'logs_table_name': 'logs',
    },

    # База для тестов orm
    'orm_sql': {
        'db_name': 'py_logs_test_orm',
        'logs_table_name': 'logs',
    },

    # База для реальных логов из скрипта
    'parser_db': {
        'db_name': 'py_logs',
        'logs_table_name': 'logs'
    },
}
