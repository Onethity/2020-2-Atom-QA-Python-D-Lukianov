#!/usr/bin/python3
import datetime
import json
import os.path
import sys
import re

OUTPUT_FILE = 'output_py.txt' # Путь к выходному файлу
OUTPUT_FILE_JSON = 'output_py.json' # Путь в выходному json файлу

if len(sys.argv) == 1:
    print(
        "Ошибка: вы должны передать путь к лог-файлу или к папке с логами",
        f"Для получения справки введите {sys.argv[0]} -h",
        sep="\n"
    )
    sys.exit(1)

if '-h' in sys.argv:
    print(
        f"Использование: {sys.argv[0]} (<file>|<dir>...)",
        "Если передан путь к лог-файлу, то выполняется анализ этого файла",
        "Если передан путь к папке, то скрипт выбирает все лог-файлы из папки и анализирует их",
        " ",
        "Примеры:",
        f"{sys.argv[0]} access.log",
        f"{sys.argv[0]} /var/log/nginx",
        sep="\n"
    )
    sys.exit(0)


def uniq_and_count(data: list) -> list:
    """ Считает количество уникальных элементов в списке и группирует их"""
    output = []
    uniq = list(set(data))
    uniq_and_count = []
    for uniq_value in uniq:
        count = data.count(uniq_value)
        uniq_and_count.append({'count': count, 'value': uniq_value})

    for line in sorted(uniq_and_count, key=lambda log: log['count'], reverse=True)[:10]:
        output.append({'count': line['count'], 'value': line['value']})

    return output


def read_log(path):
    """ Читает файл с логами """
    with open(path) as log:
        log_data = []
        for line in log.readlines():
            if line == '\n':
                continue

            line_data = line.split(' ')
            try:
                log_data.append({
                    'ip': line_data[0],
                    'method': line_data[5],
                    'url': line_data[6],
                    'status_code': line_data[8],
                    'size': line_data[9]
                })
            except IndexError:
                print(f'Неверный формат лог-файла {path}')
                sys.exit(1)

    return log_data

# Читаем все логи в list
log_data = []
for path in sys.argv[1:]:
    if os.path.exists(path):
        if os.path.isfile(path):
            log_data += read_log(path)

        elif os.path.isdir(path):
            for filename in os.listdir(path):
                if filename.endswith('.log'):
                    file_path = os.path.join(path, filename)
                    log_data += read_log(file_path)
                    print(os.path.join(path, file_path))
    else:
        print(f'Путь не существует: {path}')
        sys.exit(1)

# Если выходной файл существует, то дополняем его
if os.path.exists(OUTPUT_FILE):
    mode = 'a'
else:
    mode = 'w'

# Перенаправляем поток вывода в файл
orig_stdout = sys.stdout
f = open(OUTPUT_FILE, mode)
sys.stdout = f

print('\n========== Новый анализ {} {} =========='.format(
    ' '.join(sys.argv[1:]),
    datetime.datetime.today(),
))
total_requests = len(log_data)
print('Total count: {}'.format(total_requests))
print('-------------------')

print('Requests by type:')
log_filtered = [log['method'][1:] for log in log_data if re.match('"[A-Z]+', log['method'])]
requests_by_type = uniq_and_count(log_filtered)
for line in requests_by_type:
    print(line['count'], line['value'])
print('-------------------')


print('Top 10 biggest requests')
log_filtered = [log for log in log_data if log['size'] != '-']
log_sorted = sorted(log_filtered, key=lambda log: int(log['size']), reverse=True)
biggest_requests =[]
for line in log_sorted[:10]:
    print(line['url'], line['size'])
    biggest_requests.append({'url': line['url'], 'size': line['size']})
print('-------------------')


print('Top 10 client errors:')
log_with_client_errors = filter(lambda log: re.match(r'4[0-9][0-9]', log['status_code']), log_data)
log_with_client_errors = [log['url'] + ' ' + log['status_code'] + ' ' + log['ip'] for log in log_with_client_errors]
client_errors = uniq_and_count(log_with_client_errors)
for line in client_errors:
    print(line['count'], line['value'])
print('-------------------')

print('Top 10 server errors:')
log_with_client_errors = filter(lambda log: re.match(r'5[0-9][0-9]', log['status_code']), log_data)
log_with_client_errors = [log['url'] + ' ' + log['status_code'] + ' ' + log['ip'] for log in log_with_client_errors]
server_errors = uniq_and_count(log_with_client_errors)
for line in server_errors :
    print(line['count'], line['value'])
print('-------------------')

sys.stdout = orig_stdout
f.close()
print("Анализ успешно завершен. Результаты добавлены в output_py.txt и output.json")

json_structure = {
    'Total requests': total_requests,
    'Requests types': requests_by_type,
    'Biggest requests': biggest_requests,
    'Client errors': client_errors,
    'Server errors': server_errors,
}

with open(OUTPUT_FILE_JSON, 'w') as f:
    json.dump(json_structure, f, indent=4)
