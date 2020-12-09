#!/usr/bin/python3
import os.path
import sys
from datetime import datetime

import sqlalchemy

from config import CONFIG
from mysql.orm.models.log_data import LogDataModel
from mysql.orm.mysql_orm_client import MysqlOrmConnection
from mysql.orm.query_builder import OrmQueryBuilder

# Выводим ошибку, если нет аргументов
if len(sys.argv) == 1:
    print(
        "Ошибка: вы должны передать путь к лог-файлу или к папке с логами",
        f"Для получения справки введите {sys.argv[0]} -h",
        sep="\n"
    )
    sys.exit(1)

# Вывод справки по команде -h
if '-h' in sys.argv:
    print(
        f"Использование: {sys.argv[0]} (<file>|<dir>...)",
        "Если передан путь к лог-файлу, то выполняется париснг этого файла",
        "Если передан путь к папке, то скрипт выбирает все лог-файлы из папки и парисит их",
        "Данные доступа к БД настраиваются в файле config.py",
        " ",
        "Примеры:",
        f"{sys.argv[0]} access.log",
        f"{sys.argv[0]} /var/log/nginx",
        sep="\n"
    )
    sys.exit(0)


def parse_and_insert_logs(path, builder: OrmQueryBuilder):
    """ Читает файл с логами и вставляет их базу """
    with open(path) as log:
        total_logs_counter = len(log.readlines()) - 1  # Посчитали количество логов для вывода прогресса

    with open(path) as log:
        log_counter = 0
        for line in log.readlines():
            if line == '\n':
                continue

            line_data = line.split(' ')
            try:
                # Создаем ORM модель на основе данных лога
                log_data = LogDataModel(
                    ip=line_data[0],
                    time=datetime.strptime(line_data[3][1:], '%d/%b/%Y:%H:%M:%S'),
                    method=line_data[5][1:],
                    url=line_data[6],
                    status_code=int(line_data[8]),
                    bytes_sent=int(line_data[9]) if line_data[9] != '-' else 0
                )
            except IndexError:
                print(f'Неверный формат лог-файла {path}')
                sys.exit(1)

            builder.insert_log(log_data) # Вставляем ORM модель в базу
            log_counter += 1
            sys.stdout.write('\r')
            print(f'  Обработано: [{log_counter}/{total_logs_counter}]', end='', flush=True)
            sys.stdout.flush()


try:
    client = MysqlOrmConnection(
        host=CONFIG['host'],
        port=CONFIG['port'],
        user=CONFIG['user'],
        password=CONFIG['password'],
        db_name=CONFIG['parser_db']['db_name'],
        logs_table_name=CONFIG['parser_db']['logs_table_name']
    )
except sqlalchemy.exc.OperationalError as e:
    print("Невозможно подключиться к базе данных. Проверьте данные доступа в файле 'config.py'")
    print(e.orig)
    sys.exit(1)

builder = client.builder

for path in sys.argv[1:]:
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f'Файл {path}:')
            parse_and_insert_logs(path, builder)
            print('\n')

        elif os.path.isdir(path):
            for filename in os.listdir(path):
                if filename.endswith('.log'):
                    file_path = os.path.join(path, filename)
                    parse_and_insert_logs(file_path, builder)
                    print(os.path.join(path, file_path))
    else:
        print(f'Путь не существует: {path}')
        sys.exit(1)
